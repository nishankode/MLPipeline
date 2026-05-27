# common.py
import os
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any
from src.datascienceproject import logger


@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:

    "Reads and Returns YAML file content"

    try:
        with open(file_path) as file:
            content = yaml.safe_load(file)
            logger.info(f"YAML file {file_path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_dirs: list, verbose=True):

    "Create multiple directories from a list of directories"

    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")


@ensure_annotations
def load_json(file_path: Path) -> ConfigBox:

    "Load JSON file as dict"

    with open(file_path, 'r') as f:
        data = json.load(f)
    logger.info(f"JSON file loaded successfully from: {file_path}")
    return ConfigBox(data)

@ensure_annotations
def save_json(save_path: Path, data: dict):

    "Save dict to JSON file"

    with open(save_path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {save_path}")

@ensure_annotations
def save_bin(data: Any, save_path: Path):

    "Save any binary file"

    joblib.dump(value=data, filename=save_path)
    logger.info(f"Binary file saved at: {save_path}")

@ensure_annotations
def load_bin(file_path: Path):

    "Load a Binary file"

    data = joblib.load(file_path)
    logger.info(f"Binary file loaded from: {file_path}")
    return data