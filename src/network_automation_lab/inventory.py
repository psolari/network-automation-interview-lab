from pathlib import Path
import yaml


def load_inventory(path: str | Path) -> dict:
    with open(path, encoding="utf-8") as file:
        return yaml.safe_load(file)
