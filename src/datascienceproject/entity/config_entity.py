# config_entity.py

from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: Path
    all_schema: dict
    target: dict

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass
class ModelTrainingConfig:
  root_dir: Path
  train_data: Path
  test_data: Path
  model_name: str
  alpha: float
  l1_ratio: float
  target: str