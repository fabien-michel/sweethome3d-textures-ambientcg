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
