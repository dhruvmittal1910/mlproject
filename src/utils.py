# any utility code
#all common things or function we can use

import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
import pickle
import dill

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        
        logging.info("created a pkl file and stored it (utils,py) ")

    except Exception as e:
        raise CustomException(e, sys)