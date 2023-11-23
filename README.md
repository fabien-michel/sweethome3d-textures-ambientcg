# Sweethome3D texture library generator from ambientcg.com textures

A python script which download all textures from [ambientcg.com](https://ambientcg.com/) and build a [Sweethome3D](https://www.sweethome3d.com) texture library (`.sh3t`)
The texture are resized to 3 sizes, so you can choose quality. 

3 qualities available: 256, 512 and 1024 pixels width.

Current version: 2023.11.23<br>
Total textures: 1316

## Install

Just download the .sh3t file you want and use the texture library import feature from Sweethome3D from "Furniture" menu.


* [ambientcg_1024.sh3t](https://fenouil-drive.mycozy.cloud/public?sharecode=QyiDq6EIACQi) - 196.7 MB

* [ambientcg_512.sh3t](https://fenouil-drive.mycozy.cloud/public?sharecode=u2Ps0zAB8cij) - 51.0 MB

* [ambientcg_256.sh3t](https://fenouil-drive.mycozy.cloud/public?sharecode=3gsbVKG3PFBM) - 13.5 MB


## Missing dimensions
Sadly a lot of textures haven't dimensions defined in ambientcg.com. The script default to 100cm×100cm.

## Build / update the library

In a python virtual environnement install pypi dependencies using poetry:

```
poetry install
```
Run script:

```
poetry run python build.py
```
⚠️: 🕑 Zip download take a long time !

## Run without cache

```
poetry run python build.py --no-json-cache --no-image-cache
```

## Licence and Author

Created using assets from ambientCG.com, licensed under the Creative Commons CC0 1.0 Universal License.

Original textures author: Lennart Demes

The current code and content follow the same licence.

## Preview


### Asphalt
<picture>
  <img alt="Preview of Asphalt" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Asphalt.webp">
</picture>

### Bamboo
<picture>
  <img alt="Preview of Bamboo" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Bamboo.webp">
</picture>

### Bark
<picture>
  <img alt="Preview of Bark" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Bark.webp">
</picture>

### Bricks
<picture>
  <img alt="Preview of Bricks" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Bricks.webp">
</picture>

### Cardboard
<picture>
  <img alt="Preview of Cardboard" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Cardboard.webp">
</picture>

### Carpet
<picture>
  <img alt="Preview of Carpet" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Carpet.webp">
</picture>

### Chainmail
<picture>
  <img alt="Preview of Chainmail" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Chainmail.webp">
</picture>

### Chipboard
<picture>
  <img alt="Preview of Chipboard" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Chipboard.webp">
</picture>

### Clay
<picture>
  <img alt="Preview of Clay" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Clay.webp">
</picture>

### Concrete
<picture>
  <img alt="Preview of Concrete" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Concrete.webp">
</picture>

### Cork
<picture>
  <img alt="Preview of Cork" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Cork.webp">
</picture>

### CorrugatedSteel
<picture>
  <img alt="Preview of CorrugatedSteel" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/CorrugatedSteel.webp">
</picture>

### DiamondPlate
<picture>
  <img alt="Preview of DiamondPlate" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/DiamondPlate.webp">
</picture>

### Fabric
<picture>
  <img alt="Preview of Fabric" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Fabric.webp">
</picture>

### Foil
<picture>
  <img alt="Preview of Foil" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Foil.webp">
</picture>

### GlazedTerracotta
<picture>
  <img alt="Preview of GlazedTerracotta" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/GlazedTerracotta.webp">
</picture>

### Granite
<picture>
  <img alt="Preview of Granite" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Granite.webp">
</picture>

### Grass
<picture>
  <img alt="Preview of Grass" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Grass.webp">
</picture>

### Gravel
<picture>
  <img alt="Preview of Gravel" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Gravel.webp">
</picture>

### Ground
<picture>
  <img alt="Preview of Ground" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Ground.webp">
</picture>

### Logs
<picture>
  <img alt="Preview of Logs" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Logs.webp">
</picture>

### Marble
<picture>
  <img alt="Preview of Marble" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Marble.webp">
</picture>

### Metal
<picture>
  <img alt="Preview of Metal" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Metal.webp">
</picture>

### Moss
<picture>
  <img alt="Preview of Moss" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Moss.webp">
</picture>

### OfficeCeiling
<picture>
  <img alt="Preview of OfficeCeiling" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/OfficeCeiling.webp">
</picture>

### Paint
<picture>
  <img alt="Preview of Paint" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Paint.webp">
</picture>

### Paper
<picture>
  <img alt="Preview of Paper" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Paper.webp">
</picture>

### PavingStones
<picture>
  <img alt="Preview of PavingStones" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/PavingStones.webp">
</picture>

### Planks
<picture>
  <img alt="Preview of Planks" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Planks.webp">
</picture>

### Plaster
<picture>
  <img alt="Preview of Plaster" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Plaster.webp">
</picture>

### Plastic
<picture>
  <img alt="Preview of Plastic" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Plastic.webp">
</picture>

### Porcelain
<picture>
  <img alt="Preview of Porcelain" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Porcelain.webp">
</picture>

### Road
<picture>
  <img alt="Preview of Road" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Road.webp">
</picture>

### Rock
<picture>
  <img alt="Preview of Rock" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Rock.webp">
</picture>

### Rocks
<picture>
  <img alt="Preview of Rocks" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Rocks.webp">
</picture>

### RoofingTiles
<picture>
  <img alt="Preview of RoofingTiles" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/RoofingTiles.webp">
</picture>

### Rust
<picture>
  <img alt="Preview of Rust" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Rust.webp">
</picture>

### Snow
<picture>
  <img alt="Preview of Snow" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Snow.webp">
</picture>

### SolarPanel
<picture>
  <img alt="Preview of SolarPanel" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/SolarPanel.webp">
</picture>

### Tatami
<picture>
  <img alt="Preview of Tatami" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Tatami.webp">
</picture>

### Terrazzo
<picture>
  <img alt="Preview of Terrazzo" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Terrazzo.webp">
</picture>

### ThatchedRoof
<picture>
  <img alt="Preview of ThatchedRoof" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/ThatchedRoof.webp">
</picture>

### Tiles
<picture>
  <img alt="Preview of Tiles" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Tiles.webp">
</picture>

### Wallpaper
<picture>
  <img alt="Preview of Wallpaper" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Wallpaper.webp">
</picture>

### Wood
<picture>
  <img alt="Preview of Wood" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/Wood.webp">
</picture>

### WoodChips
<picture>
  <img alt="Preview of WoodChips" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/WoodChips.webp">
</picture>

### WoodFloor
<picture>
  <img alt="Preview of WoodFloor" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/WoodFloor.webp">
</picture>

### WoodSiding
<picture>
  <img alt="Preview of WoodSiding" src="https://raw.githubusercontent.com/fabien-michel/sweethome3d-textures-ambientcg/v2023.11.23/previews/WoodSiding.webp">
</picture>
