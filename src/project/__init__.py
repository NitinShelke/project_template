import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore")

import json
import os

import yaml
from box import Box

# Function to read YAML file
def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return Box(data)

def save_dataframe(df, file_path):
    """
    Save a DataFrame to the specified file path. Create directories if they do not exist.

    Parameters:
    - df (pandas.DataFrame): The DataFrame to be saved.
    - file_path (str): The path where the DataFrame will be saved.
    """
    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Save the DataFrame to the specified file path
    df.to_csv(file_path, index=False)

import logging
import os

class CustomLogger:
    def __init__(self, log_file="RUNNING_LOGGS.log"):
        self.logger = logging.getLogger("CustomLogger")
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create a console handler and set level to debug
        log_folder="logs"
        if log_folder:
            if not os.path.exists(log_folder):
                os.makedirs(log_folder)

        log_file=os.path.join(log_folder,log_file)
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message,exc_info=True)

    def critical(self, message):
        self.logger.critical(message)
        
logger=CustomLogger()

