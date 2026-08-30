import json
from pathlib import Path


def load_test_data():
    file_path = (
        Path(__file__).parent.parent
        / "test_data"
        / "test_data.json"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)