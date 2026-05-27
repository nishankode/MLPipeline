# data_ingestion.py
import os
import urllib.request as request
from src.datascienceproject import logger
import zipfile

from src.datascienceproject.entity.config_entity import DataIngestionConfig

class DataIngestion:
	def __init__(self, config:DataIngestionConfig):
		self.config = config
		
	def download_file(self):

		"Downloading a zipfile"

		if not os.path.exists(self.config.local_data_file):

			filename, headers = request.urlretrieve(
				url = self.config.source_url,
				filename = self.config.local_data_file
			)
			logger.info(f"{filename}: Downloaded Successfully")
		else:
			logger.info(f"File already exists")

	def extract_zip_file(self):

		"Extracting a zipfile"
		
		try:
			unzip_path = self.config.unzip_dir
			os.makedirs(unzip_path, exist_ok=True)
			with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
				zip_ref.extractall(unzip_path)
			logger.info(f"Zipfile extracted to: {unzip_path}")
		except:
			logger.info(f"Failed to extract Zipfile to: {unzip_path}")