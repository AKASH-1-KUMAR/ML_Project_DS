from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion


if __name__=="__main__":
    logging.info("The Logging execution has started")



    try:
        # data_ingestion_config = DataIngestion()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
        
    except Exception as e:
        logging.info("The exception has occurred")
        raise CustomException(e, sys)