import os
import urllib.parse
from pathlib import Path

from build import SIZES

VERSION = Path("VERSION").read_text()
GIT_VERSION = f"v{VERSION}"

if __name__ == "__main__":
    os.system(f"git tag -a {GIT_VERSION}")
    os.system(f"git push")
    os.system(f"git push --tags")

    download_versions = [
        f"- [ambientcg_{size}.sh3t](https://github.com/fabien-michel/sweethome3d-textures-ambientcg/raw/{GIT_VERSION}/ambientcg_{size}.sh3t)"
        for size in SIZES
    ]
    body = "\n".join(download_versions)

    params = urllib.parse.urlencode(
        {
            "tag": GIT_VERSION,
            "title": GIT_VERSION,
            "body": body,
        }
    )

    print(
        "https://github.com/fabien-michel/sweethome3d-textures-ambientcg/releases/new?"
        + params
    )