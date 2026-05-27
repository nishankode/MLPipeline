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

        # Splitting X and y
        X = data.drop(self.config.target, axis=1)
        y = data[[self.config.target]]

        # Performing Train Test Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.config.test_size)
        
        # Saving splitted data to root dir
        X_train.to_csv(os.path.join(self.config.root_dir, "X_train.csv"), index=False)
        X_test.to_csv(os.path.join(self.config.root_dir, "X_test.csv"), index=False)
        y_train.to_csv(os.path.join(self.config.root_dir, "y_train.csv"), index=False)
        y_test.to_csv(os.path.join(self.config.root_dir, "y_test.csv"), index=False)

        logger.info(f"Train Test split completed & data saved to: {self.config.root_dir}")
        logger.info(f"X_train Shape: {X_train.shape}")
        logger.info(f"X_test Shape: {X_test.shape}")
        logger.info(f"y_train Shape: {y_train.shape}")
        logger.info(f"y_test Shape: {y_test.shape}")