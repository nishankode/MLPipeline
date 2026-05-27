# model_evaluation.py
import os
from dotenv import load_dotenv
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
from pathlib import Path
import joblib

from src.datascienceproject import logger
from src.datascienceproject.utils.common import save_json
from src.datascienceproject.entity.config_entity import ModelEvaluationConfig

load_dotenv()


class ModelEvaluation:

    def __init__(self, config: ModelEvaluationConfig) -> ModelEvaluationConfig:
        self.config = config

    def eval_metrics(self, actual, pred):

        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rmse, mae, r2

    def evaluate(self):
        
        mlflow_tracking_uri = os.getenv("MLFLOW_TRACKING_URI")

        # Loading Data
        X_train = pd.read_csv(self.config.X_train_data)
        X_test = pd.read_csv(self.config.X_test_data)
        y_train = pd.read_csv(self.config.y_train_data)
        y_test = pd.read_csv(self.config.y_test_data)

        # Loading model
        model = joblib.load(self.config.model_path)

        # Computing test metrics
        test_pred = model.predict(X_test)
        rmse_test, mae_test, r2_test = self.eval_metrics(y_test, test_pred)

        # Computing train metrics
        train_pred = model.predict(X_train)
        rmse_train, mae_train, r2_train = self.eval_metrics(y_train, train_pred)
        
        # Computing r2 gap for finding overfitting
        r2_gap = r2_train - r2_test
        if r2_gap > 0.15:
            logger.warning(f"Possible Overfitting -- R2 Gap: {r2_gap}")
            
        # creating scores dict
        scores = {
            "Train": {
                "RMSE": rmse_train,
                "MAE": mae_train,
                "R2": r2_train
            },
            "Test": {
                "RMSE": rmse_test,
                "MAE": mae_test,
                "R2": r2_test 
            },
            'R2 Gap': r2_gap
        }

        # Setting Tracking URI
        mlflow.set_tracking_uri(mlflow_tracking_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            mlflow.log_params(
                {
                    **self.config.all_params,
                    "X_train_size": len(X_train),
                    "X_test_size": len(X_test),
                    "y_train_size": len(y_train),
                    "y_test_size": len(y_test),
                }
            )

            # Logging test metrics
            mlflow.log_metrics(
                {"test_rmse": rmse_test, "test_mae": mae_test, "test_r2": r2_test}
            )

            # Logging train metrics
            mlflow.log_metrics(
                {"train_rmse": rmse_train, "train_mae": mae_train, "train_r2": r2_train}
            )
            
            # Logging r2 gap
            mlflow.log_metric("r2_gap", round(r2_gap, 4))
            
            # Setting Tags
            mlflow.set_tags({
                "model_type": "ElasticNet",
                "dataset": "winequality-red",
            })

            # Saving scores as json artifact
            save_json(save_path=Path(self.config.metric_file_name), data=scores)

            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(
                    model, "model", registered_model_name="ElasticNet - Production"
                )
            else:
                mlflow.sklearn.log_model(model, "model")
