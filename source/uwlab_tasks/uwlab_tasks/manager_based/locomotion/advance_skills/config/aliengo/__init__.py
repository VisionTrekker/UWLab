# Copyright (c) 2024-2025, The UW Lab Project Developers.
# All Rights Reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

from . import agents

gym.register(
    id="UW-Position-Advance-Skills-AlienGo-v0",
    entry_point="uwlab.envs:DataManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.aliengo_env_cfg:AdvanceSkillsAlienGoEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_cfg:AdvanceSkillsAlienGoPPORunnerCfg",
    },
)


gym.register(
    id="UW-Position-Pit-AlienGo-v0",
    entry_point="uwlab.envs:DataManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.aliengo_env_cfg:PitAlienGoEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_cfg:AdvanceSkillsAlienGoPPORunnerCfg",
    },
)

gym.register(
    id="UW-Position-Gap-AlienGo-v0",
    entry_point="uwlab.envs:DataManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.aliengo_env_cfg:GapAlienGoEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_cfg:AdvanceSkillsAlienGoPPORunnerCfg",
    },
)

gym.register(
    id="UW-Position-Inv-Slope-AlienGo-v0",
    entry_point="uwlab.envs:DataManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.aliengo_env_cfg:SlopeInvAlienGoEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_cfg:AdvanceSkillsAlienGoPPORunnerCfg",
    },
)

gym.register(
    id="UW-Position-Extreme-Stair-AlienGo-v0",
    entry_point="uwlab.envs:DataManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.aliengo_env_cfg:ExtremeStairAlienGoEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_cfg:AdvanceSkillsAlienGoPPORunnerCfg",
    },
)

gym.register(
    id="UW-Position-Square-Obstacle-AlienGo-v0",
    entry_point="uwlab.envs:DataManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.aliengo_env_cfg:SquarePillarObstacleAlienGoEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_cfg:AdvanceSkillsAlienGoPPORunnerCfg",
    },
)

gym.register(
    id="UW-Position-Irregular-Obstacle-AlienGo-v0",
    entry_point="uwlab.envs:DataManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.aliengo_env_cfg:IrregularPillarObstacleAlienGoEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_cfg:AdvanceSkillsAlienGoPPORunnerCfg",
    },
)
