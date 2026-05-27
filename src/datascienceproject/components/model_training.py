# model_training.py
import pandas as pd
import numpy as np
import os
from sklearn.linear_model import ElasticNet
import joblib
from src.datascienceproject import logging
from src.datascienceproject.entity.config_entity import ModelTrainingConfig


class ModelTraining:
    
	def __init__(self, config:ModelTrainingConfig) -> ModelTrainingConfig:
		self.config = config

	def train(self):

		# Loading the data
		train_data = pd.read_csv(self.config.train_data)
		test_data = pd.read_csv(self.config.test_data)

		# Splitting to X and Y splits
		X_train = train_data.drop(columns=[self.config.target])
		y_train = train_data[self.config.target]
		X_test = test_data.drop(columns=[self.config.target])
		y_test = test_data[self.config.target]

		# Configuring the model
		model = ElasticNet(
			alpha=self.config.alpha,
			l1_ratio=self.config.l1_ratio,
			random_state=42
		)

		# Training the model
		model.fit(X_train, y_train)

		# Saving the model pickle
		joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))