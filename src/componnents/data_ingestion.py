
import os
import zipfile
import urllib.request as request
import pandas as pd
from src.logging import logger
import shutil
from src.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def move_file_to_data_ingestion(self):
        if not os.path.exists(self.config.root_dir):
            shutil.move(self.config.data_path, self.config.root_dir)
        else:
            print(f"File {self.config.root_dir} already exists, skipping move.")

    def get_data(self):
        df = pd.read_csv(self.config.data_path)
        print(df.head())
        return df