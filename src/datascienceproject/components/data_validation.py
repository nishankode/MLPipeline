# data_validation.py
import os
from src.datascienceproject import logger
import pandas as pd

from src.datascienceproject.entity.config_entity import DataValidationConfig

class DataValidation:
	def __init__(self, config: DataValidationConfig):
		self.config = config
		
	def validate_all_columns(self) -> bool:

		try:
			# Checking validation status
			validation_status = True
			df = pd.read_csv(self.config.unzip_data_dir)
			schema = self.config.all_schema
			target_col = self.config.target.name

			all_columns = [i for i in df.columns if i != target_col]
			for col in all_columns:
				if str(df[col].dtype ) == self.config.all_schema[col]:
					pass
				else:
					validation_status = False

			# Writing validation status to txt file
			with open(self.config.STATUS_FILE, 'w') as f:
				f.write(str(validation_status))

			logger.info(f"Data validation completed and file saved at: {self.config.STATUS_FILE}")

		except Exception as e:
			logger.exception(e)