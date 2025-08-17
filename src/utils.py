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
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        
        logging.info("created a pkl file and stored it (utils,py) ")

    except Exception as e:
        raise CustomException(e, sys)
    
    
def evaluate_model(X_train,y_train,X_test,y_test,models,params):
    
    try:
        logging.info("starting to evaluate the model")
        report={}
        
        logging.info("running through each model")
        
        for i in range(len(list(models))):
            
            model=list(models.values())[i]
            # get the hyper-parameter tuning parameter wrt to each model
            param=params[list(models.keys())[i]]
            
            gs=GridSearchCV(model,param,cv=3)
            gs.fit(X_train,y_train)
            # model.fit(X_train,y_train)
            
            logging.info("checking the best parameter after hyper param tuning")
            
            model.set_params(**gs.best_params_)
                    
            # evaluate the model
            model=model.fit(X_train,y_train)
            
            logging.info("predicted the y values based on x test")

            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)
            
            logging.info("Calculating the r2 score")
            
            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)
            
            logging.info("put the scores in the report")
            
            report[list(models.keys())[i]]=test_model_score
            
        return report
            
    except:
        pass
    
    
    