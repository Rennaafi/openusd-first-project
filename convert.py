import trimesh
from pxr import Usd, UsdGeom, Vt

m = trimesh.load("Part_Studio_2.stl")                    # vertices + faces as numpy arrays

stage = Usd.Stage.CreateNew("part2.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
UsdGeom.SetStageMetersPerUnit(stage, 1.0)
UsdGeom.Xform.Define(stage, "/World")

mesh = UsdGeom.Mesh.Define(stage, "/World/Part")
mesh.GetPointsAttr().Set(Vt.Vec3fArray.FromNumpy(m.vertices * 0.001))   # STL is mm -> m
mesh.GetFaceVertexCountsAttr().Set([3] * len(m.faces))      # every face is a triangle
mesh.GetFaceVertexIndicesAttr().Set(Vt.IntArray.FromNumpy(m.faces.flatten()))

stage.SetDefaultPrim(stage.GetPrimAtPath("/World"))
stage.Save()
