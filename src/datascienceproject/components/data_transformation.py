# data_transformation.py
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.datascienceproject import logger
from src.datascienceproject.entity.config_entity import DataTransformationConfig

class DataTransformation:

    def __init__(self, config:DataTransformationConfig):
        self.config = config

    def train_test_split(self):

        # Loading the data and train test split
        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data)
        
        # Saving splitted data to root dir
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info(f"Train Test split completed & data saved to: {self.config.root_dir}")
        logger.info(f"Train Shape: {train.shape}")
        logger.info(f"Test Shape: {test.shape}")