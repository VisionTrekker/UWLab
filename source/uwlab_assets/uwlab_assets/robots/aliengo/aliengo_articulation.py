import re

from isaaclab.assets import Articulation
from isaacsim.core.utils.stage import get_current_stage
from pxr import PhysxSchema, Sdf, Usd, UsdGeom



class AliengoArticulation(Articulation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prepare_contact_sensors()

    def prepare_contact_sensors(self):
        stage = get_current_stage()
        pattern = "/World/envs/env_.*/Robot/.*(foot|calf|thigh|hip|trunk)$"
        matching_prims = []
        prim: Usd.Prim
        for prim in stage.Traverse():
            if prim.IsA(UsdGeom.Xform):
                prim_path: Sdf.Path = prim.GetPath()
                if re.match(pattern, prim_path.pathString):
                    matching_prims.append(prim_path)

        for prim in matching_prims:
            contact_api: PhysxSchema.PhysxContactReportAPI = \
                PhysxSchema.PhysxContactReportAPI.Get(stage, prim)
            # contact_api.CreateReportPairsRel().AddTarget("/World/terrain/obstacles/obstacles")
            contact_api.CreateReportPairsRel().AddTarget("/World/ground")