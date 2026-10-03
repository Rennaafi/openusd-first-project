from pxr import Usd, UsdShade, Sdf, Gf

stage = Usd.Stage.Open("part2.usda")

mat = UsdShade.Material.Define(stage, "/World/Looks/Orange")
sh = UsdShade.Shader.Define(stage, "/World/Looks/Orange/Surface")
sh.CreateIdAttr("UsdPreviewSurface")
sh.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f(1.0, 0.4, 0.0))
sh.CreateInput("metallic", Sdf.ValueTypeNames.Float).Set(0.9)
sh.CreateInput("roughness", Sdf.ValueTypeNames.Float).Set(0.4)
mat.CreateSurfaceOutput().ConnectToSource(sh.ConnectableAPI(), "surface")

UsdShade.MaterialBindingAPI(stage.GetPrimAtPath("/World/Part")).Bind(mat)
stage.Save()