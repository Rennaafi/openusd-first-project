# OpenUSD with Python: first project

A hands-on learning log: authoring [OpenUSD](https://openusd.org) scenes from Python (`usd-core`) and checking them in Blender. No Omniverse or RTX GPU needed.

## Setup

```powershell
pip install -r requirements.txt
```

To view the output, use Blender 3.5+ (File > Import > Universal Scene Description). Switch the viewport to **Material Preview** to see colors.

## Scripts (run in this order)

| Script | What it does | Output |
|---|---|---|
| `hello_usd.py` | Cube + sphere: prims, attributes, transforms | `hello.usda` |
| `real_geometry.py` | A `Mesh` from raw points / face counts / indices | `mesh.usda` |
| `convert.py` | STL to USD mesh with `trimesh` (mm to m) | `part2.usda` |
| `color.py` | Binds a `UsdPreviewSurface` material (run after `convert.py`) | edits `part2.usda` |
| `assembly.py` | Three **references** to one part, one with a scale override | `assembly.usda` |
| `dance.py` | Bounce/sway animation with time samples | `duck.usda` |

`dance.py` needs an STL of your own at `enteheiz_bebek/ENTE HEINZ.stl` (not included; edit the path to use any STL).

## Things that bit me

- **STL has no units.** A 115 mm part imported as 115 m until I scaled the points by 0.001. Always check Blender's Dimensions panel.
- **Axis and units are file metadata.** `SetStageUpAxis(z)` and `SetStageMetersPerUnit(1.0)` make Blender import with no rotation or scale fix-up.
- **References are links, not copies.** `assembly.usda` has no mesh data: change `part2.usda` and every instance changes.
- `.usda` is data, not code. Run the `.py`, open the `.usda`.

## Roadmap

- [x] Prims, transforms, units
- [x] Mesh from raw arrays, STL conversion
- [x] References, per-instance overrides
- [x] Materials
- [x] Time-sampled animation
- [ ] `UsdPhysics` joints for a simple robot (wheel referenced 4x)
- [ ] URDF to USD, simulation in Isaac Sim (needs an RTX GPU)
