from pxr import Usd, UsdGeom, Gf, Vt

stage = Usd.Stage.CreateNew("mesh.usda")
UsdGeom.Xform.Define(stage, "/World")

tri = UsdGeom.Mesh.Define(stage, "/World/Tri")
tri.GetPointsAttr().Set(Vt.Vec3fArray([(0, 0, 0), (1, 0, 0), (0, 1, 0)]))
tri.GetFaceVertexCountsAttr().Set([3])          # one face with 3 corners
tri.GetFaceVertexIndicesAttr().Set([0, 1, 2])   # which points make that face
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
UsdGeom.SetStageMetersPerUnit(stage, 1.0)

stage.SetDefaultPrim(stage.GetPrimAtPath("/World"))
stage.Save()