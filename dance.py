import math
import trimesh
from pxr import Usd, UsdGeom, Vt, Gf

m = trimesh.load("enteheiz_bebek/ENTE HEINZ.stl")
print("bounds:", m.bounds, "triangles:", len(m.faces))

# STL has no units, so scale the longest side to 0.2 m, centered, sitting on z=0
c = m.bounds.mean(axis=0)
s = 0.2 / max(m.extents)
v = ((m.vertices - c) * s).astype("float32")
v[:, 2] -= v[:, 2].min()

stage = Usd.Stage.CreateNew("duck.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
UsdGeom.SetStageMetersPerUnit(stage, 1.0)
stage.SetStartTimeCode(0); stage.SetEndTimeCode(96); stage.SetTimeCodesPerSecond(24)
UsdGeom.Xform.Define(stage, "/World")

duck = UsdGeom.Xform.Define(stage, "/World/Duck")
mesh = UsdGeom.Mesh.Define(stage, "/World/Duck/Mesh")
mesh.GetPointsAttr().Set(Vt.Vec3fArray.FromNumpy(v))
mesh.GetFaceVertexCountsAttr().Set([3] * len(m.faces))
mesh.GetFaceVertexIndicesAttr().Set(Vt.IntArray.FromNumpy(m.faces.flatten()))

api = UsdGeom.XformCommonAPI(duck)
for t in range(0, 97):                      # 4 s at 24 fps, loops cleanly
    a = 2 * math.pi * t / 48                # one dance beat = 48 frames
    api.SetTranslate(Gf.Vec3d(0, 0, abs(math.sin(a)) * 0.03), t)      # bounce
    api.SetRotate(Gf.Vec3f(10 * math.sin(a), 0, 25 * math.sin(a / 2)),
                  UsdGeom.XformCommonAPI.RotationOrderXYZ, t)         # sway + tilt

stage.SetDefaultPrim(stage.GetPrimAtPath("/World"))
stage.Save()