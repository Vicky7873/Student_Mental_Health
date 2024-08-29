from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class DataloadingConfig:
    root_dir: Path
    data_path: Path
    X_train: Path
    X_test: Path
    y_train: Path
    y_test: Path
    test_size: float

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    X_train: Path
    X_test: Path
    y_train: Path
    y_test: Path
    X_train_processed: Path
    X_test_processed: Path
    y_train_processed: Path
    y_test_processed: Path

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir :Path
    model_path : Path
    criterion: str
    n_estimators: int
    X_train_processed: Path
    y_train_processed: Path