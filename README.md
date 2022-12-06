# Sweethome3D texture library generator from ambientcg.com textures

A python script which download all textures from [ambientcg.com](https://ambientcg.com/) and build a [Sweethome3D](https://www.sweethome3d.com) texture library (`.sh3t`)
The texture are resized to 3 sizes, so you can choose quality. 

3 qualities available: 256, 512 and 1024 pixels width.

## Install

Just download the .sh3t file you want and use the texture library import feature from Sweethome3D from "Furniture" menu.

## Missing dimensions
Sadly a lot of textures haven't dimensions defined in ambientcg.com. The script default to 100cm×100cm.

## Build / update the library

In a python virtual environnement install pypi dependencies from `requirements.txt`:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Run script:

```
python build.py
```
⚠️: 🕑 Zip download take a long time !

## Run without cache

```
python build.py --no-json-cache --no-image-cache
```

## Preview

### Asphalt
<picture>
  <img alt="Asphalt.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Asphalt.webp">
</picture>

### Bark
<picture>
  <img alt="Bark.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Bark.webp">
</picture>

### Bricks
<picture>
  <img alt="Bricks.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Bricks.webp">
</picture>

### Cardboard
<picture>
  <img alt="Cardboard.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Cardboard.webp">
</picture>

### Carpet
<picture>
  <img alt="Carpet.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Carpet.webp">
</picture>

### Chainmail
<picture>
  <img alt="Chainmail.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Chainmail.webp">
</picture>

### Chipboard
<picture>
  <img alt="Chipboard.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Chipboard.webp">
</picture>

### Clay
<picture>
  <img alt="Clay.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Clay.webp">
</picture>

### Concrete
<picture>
  <img alt="Concrete.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Concrete.webp">
</picture>

### Cork
<picture>
  <img alt="Cork.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Cork.webp">
</picture>

### CorrugatedSteel
<picture>
  <img alt="CorrugatedSteel.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/CorrugatedSteel.webp">
</picture>

### DiamondPlate
<picture>
  <img alt="DiamondPlate.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/DiamondPlate.webp">
</picture>

### Fabric
<picture>
  <img alt="Fabric.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Fabric.webp">
</picture>

### GlazedTerracotta
<picture>
  <img alt="GlazedTerracotta.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/GlazedTerracotta.webp">
</picture>

### Grass
<picture>
  <img alt="Grass.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Grass.webp">
</picture>

### Gravel
<picture>
  <img alt="Gravel.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Gravel.webp">
</picture>

### Ground
<picture>
  <img alt="Ground.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Ground.webp">
</picture>

### Marble
<picture>
  <img alt="Marble.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Marble.webp">
</picture>

### Metal
<picture>
  <img alt="Metal.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Metal.webp">
</picture>

### Moss
<picture>
  <img alt="Moss.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Moss.webp">
</picture>

### OfficeCeiling
<picture>
  <img alt="OfficeCeiling.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/OfficeCeiling.webp">
</picture>

### Paint
<picture>
  <img alt="Paint.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Paint.webp">
</picture>

### Paper
<picture>
  <img alt="Paper.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Paper.webp">
</picture>

### PavingStones
<picture>
  <img alt="PavingStones.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/PavingStones.webp">
</picture>

### PineNeedles
<picture>
  <img alt="PineNeedles.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/PineNeedles.webp">
</picture>

### Planks
<picture>
  <img alt="Planks.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Planks.webp">
</picture>

### Plaster
<picture>
  <img alt="Plaster.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Plaster.webp">
</picture>

### Plastic
<picture>
  <img alt="Plastic.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Plastic.webp">
</picture>

### Porcelain
<picture>
  <img alt="Porcelain.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Porcelain.webp">
</picture>

### Road
<picture>
  <img alt="Road.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Road.webp">
</picture>

### Rocks
<picture>
  <img alt="Rocks.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Rocks.webp">
</picture>

### Rock
<picture>
  <img alt="Rock.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Rock.webp">
</picture>

### RoofingTiles
<picture>
  <img alt="RoofingTiles.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/RoofingTiles.webp">
</picture>

### Rust
<picture>
  <img alt="Rust.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Rust.webp">
</picture>

### Snow
<picture>
  <img alt="Snow.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Snow.webp">
</picture>

### SolarPanel
<picture>
  <img alt="SolarPanel.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/SolarPanel.webp">
</picture>

### Terrazzo
<picture>
  <img alt="Terrazzo.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Terrazzo.webp">
</picture>

### Tiles
<picture>
  <img alt="Tiles.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Tiles.webp">
</picture>

### WoodChips
<picture>
  <img alt="WoodChips.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/WoodChips.webp">
</picture>

### WoodFloor
<picture>
  <img alt="WoodFloor.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/WoodFloor.webp">
</picture>

### WoodSiding
<picture>
  <img alt="WoodSiding.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/WoodSiding.webp">
</picture>

### Wood
<picture>
  <img alt="Wood.webp" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/main/previews/Wood.webp">
</picture>
