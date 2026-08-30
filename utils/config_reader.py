import json
from pathlib import Path


def load_config():
    file_path = (
        Path(__file__).parent.parent
        / "config"
        / "qa.json"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)