# Copyright (c) 2024-2025, The UW Lab Project Developers.
# All Rights Reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import uwlab_assets.robots.aliengo as aliengo

from isaaclab.managers import RewardTermCfg as RewTerm
from isaaclab.managers import SceneEntityCfg
from isaaclab.utils import configclass

import uwlab_tasks.manager_based.locomotion.advance_skills.mdp as mdp
import uwlab_tasks.manager_based.locomotion.advance_skills.config.aliengo.mdp as aliengo_mdp

from ... import advance_skills_base_env, advance_skills_env


@configclass
class AlienGoActionsCfg:
    actions = aliengo.ALIENGO_JOINT_POSITION


@configclass
class SportRewardsCfg(advance_skills_base_env.RewardsCfg):
    move_forward = RewTerm(
        func=aliengo_mdp.reward_forward_velocity,
        weight=0.3,
        params={
            "std": 1,
            "max_iter": 200,
        },
    )

    air_time = RewTerm(
        func=aliengo_mdp.air_time_reward,
        weight=1.0,
        params={
            "mode_time": 0.3,
            "velocity_threshold": 0.5,
            "asset_cfg": SceneEntityCfg("robot"),
            "sensor_cfg": SceneEntityCfg("contact_forces", body_names=".*_foot"),
        },
    )

    gait = RewTerm(
        func=aliengo_mdp.GaitReward,
        weight=2.0,
        params={
            "std": 0.1,
            "max_err": 0.2,
            "velocity_threshold": 0.5,
            "synced_feet_pair_names": (("FL_foot", "RR_foot"), ("FR_foot", "RL_foot")),
            "asset_cfg": SceneEntityCfg("robot"),
            "sensor_cfg": SceneEntityCfg("contact_forces"),
            "max_iterations": 400.0,
        },
    )

    # -- penalties
    air_time_variance = RewTerm(
        func=aliengo_mdp.air_time_variance_penalty,
        weight=-1.0,
        params={"sensor_cfg": SceneEntityCfg("contact_forces", body_names=".*_foot")},
    )

    foot_slip = RewTerm(
        func=aliengo_mdp.foot_slip_penalty,
        weight=-0.2,
        params={
            "asset_cfg": SceneEntityCfg("robot", body_names=".*_foot"),
            "sensor_cfg": SceneEntityCfg("contact_forces", body_names=".*_foot"),
            "threshold": 1.0,
        },
    )

    joint_pos = RewTerm(
        func=aliengo_mdp.joint_position_penalty,
        weight=-0.4,
        params={
            "asset_cfg": SceneEntityCfg("robot", joint_names=".*"),
            "stand_still_scale": 5.0,
            "velocity_threshold": 0.5,
        },
    )


from isaaclab.managers import TerminationTermCfg as DoneTerm
@configclass
class AlienGoTerminationsCfg:
    time_out = DoneTerm(func=mdp.time_out, time_out=True)

    robot_drop = DoneTerm(
        func=mdp.root_height_below_minimum,
        params={
            "minimum_height": -20,
        },
    )

    base_contact = DoneTerm(
        func=mdp.illegal_contact,
        params={
            "sensor_cfg": SceneEntityCfg("contact_forces", body_names="trunk"),
            "threshold": 1.0,
        },
    )


@configclass
class AlienGoEnvMixin:
    actions: AlienGoActionsCfg = AlienGoActionsCfg()
    rewards: SportRewardsCfg = SportRewardsCfg()
    terminations: AlienGoTerminationsCfg = AlienGoTerminationsCfg()

    def __post_init__(self: advance_skills_base_env.AdvanceSkillsBaseEnvCfg):
        # Ensure parent classes run their setup first
        super().__post_init__()
        from uwlab_assets.robots.aliengo.aliengo_articulation import AliengoArticulation
        # overwrite as spot's body names for sensors
        self.scene.robot = aliengo.ALIENGO_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot",
                                                       class_type=AliengoArticulation)
        self.scene.height_scanner.prim_path = "{ENV_REGEX_NS}/Robot/trunk"
        self.scene.height_scanner.offset.pos = (0.0, 0.0, 0.5)
        self.scene.height_scanner.pattern_cfg.resolution = 0.15
        self.scene.height_scanner.pattern_cfg.size = (3.5, 1.5)

        # overwrite as spot's body names for events
        self.events.add_base_mass.params["asset_cfg"].body_names = "trunk"
        self.events.base_external_force_torque.params["asset_cfg"].body_names = "trunk"

        self.rewards.undesired_contact.params["sensor_cfg"].body_names = ["trunk", ".*_thigh", ".*_calf"]
        self.rewards.feet_lin_acc_l2.params["robot_cfg"].body_names = ".*_foot"
        self.rewards.feet_rot_acc_l2.params["robot_cfg"].body_names = ".*_foot"
        self.rewards.illegal_contact_penalty.params["sensor_cfg"].body_names = "trunk"

        self.terminations.base_contact.params["sensor_cfg"].body_names = "trunk"
        self.viewer.body_name = "trunk"

        self.sim.dt = 0.002
        self.decimation = 10


@configclass
class AdvanceSkillsAlienGoEnvCfg(AlienGoEnvMixin, advance_skills_env.AdvanceSkillsEnvCfg):
    pass


@configclass
class PitAlienGoEnvCfg(AlienGoEnvMixin, advance_skills_env.PitEnvConfig):
    pass


@configclass
class GapAlienGoEnvCfg(AlienGoEnvMixin, advance_skills_env.GapEnvConfig):
    pass


@configclass
class SlopeInvAlienGoEnvCfg(AlienGoEnvMixin, advance_skills_env.SlopeInvEnvConfig):
    pass


@configclass
class ExtremeStairAlienGoEnvCfg(AlienGoEnvMixin, advance_skills_env.ExtremeStairEnvConfig):
    pass


@configclass
class SquarePillarObstacleAlienGoEnvCfg(AlienGoEnvMixin, advance_skills_env.SquarePillarObstacleEnvConfig):
    pass


@configclass
class IrregularPillarObstacleAlienGoEnvCfg(AlienGoEnvMixin, advance_skills_env.IrregularPillarObstacleEnvConfig):
    pass
