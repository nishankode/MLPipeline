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
    target: str
    test_size: float


@dataclass
class ModelTrainingConfig:
    root_dir: Path
    X_train_data: Path
    y_train_data: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target: str


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    X_train_data: Path
    X_test_data: Path
    y_train_data: Path
    y_test_data: Path
    model_path: Path
    metric_file_name: Path
    target: str
    all_params: dict
