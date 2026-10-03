from pxr import Usd, UsdGeom, Gf

stage = Usd.Stage.CreateNew("hello.usda")
UsdGeom.Xform.Define(stage, "/World")

cube = UsdGeom.Cube.Define(stage, "/World/Box")
cube.GetSizeAttr().Set(2.0)
UsdGeom.XformCommonAPI(cube).SetTranslate(Gf.Vec3d(0, 1, 0))

ball = UsdGeom.Sphere.Define(stage, "/World/Ball")
ball.GetRadiusAttr().Set(0.5)
UsdGeom.XformCommonAPI(ball).SetTranslate(Gf.Vec3d(0, 2.5, 0))

stage.SetDefaultPrim(stage.GetPrimAtPath("/World"))
stage.Save()