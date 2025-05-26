# Copyright (c) 2024-2025, The UW Lab Project Developers.
# All Rights Reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for the Boston Dynamics robot.

The following configuration parameters are available:

* :obj:`SPOT_CFG`: The Spot robot with delay PD and remote PD actuators.
"""

import isaaclab.sim as sim_utils
from isaaclab.actuators import DCMotorCfg
from isaaclab.assets.articulation import ArticulationCfg
import os

##
# Configuration
##

UNITREE_ALIENGO_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{os.getenv('USER_PATH_TO_USD')}/robots/aliengo/aliengo.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.5),
        joint_pos={
            # ".*L_hip_joint": 0.1,
            # ".*R_hip_joint": -0.1,
            # "F[L,R]_thigh_joint": 0.8,
            # "R[L,R]_thigh_joint": 1.0,
            # ".*_calf_joint": -1.5,
            ".*L_hip_joint": 0.0,
            ".*R_hip_joint": -0.0,
            "F[L,R]_thigh_joint": 0.8,
            "R[L,R]_thigh_joint": 0.8,
            ".*_calf_joint": -1.5,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "base_legs": DCMotorCfg(
            joint_names_expr=[".*_hip_joint", ".*_thigh_joint", ".*_calf_joint"],
            effort_limit=35,    # refer to Aliengo urdf
            saturation_effort=35,
            velocity_limit=13.0,
            stiffness=40.0,
            damping=2.0,
            friction=0.0,
        ),
    },
)
"""Configuration of Unitree A1 using DC motor."""
