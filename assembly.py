from pxr import Usd, UsdGeom, Gf

stage = Usd.Stage.CreateNew("assembly.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
UsdGeom.SetStageMetersPerUnit(stage, 1.0)
UsdGeom.Xform.Define(stage, "/World")

for i in range(3):
    xf = UsdGeom.Xform.Define(stage, f"/World/Part_{i}")
    xf.GetPrim().GetReferences().AddReference("./part2.usda")   # not a copy, a link
    api = UsdGeom.XformCommonAPI(xf)
    api.SetTranslate(Gf.Vec3d(i * 0.15, 0, 0))
    if i == 2:
        api.SetScale(Gf.Vec3f(2, 2, 2))                         # per-copy override

stage.SetDefaultPrim(stage.GetPrimAtPath("/World"))
stage.Save()
