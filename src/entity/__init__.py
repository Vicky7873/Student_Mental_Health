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