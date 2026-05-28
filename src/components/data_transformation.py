'''
for any kind of data transformation, this is the file which we are looking at.

Lable encoding , OHE , etc.
'''
import os
import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomeException
from src.logger import logging
from src.utils import save_object
@dataclass
class data_transformation_config:
    preprocessor_obj_file_path = os.path.join('artifact',"preprocessor.pkl")
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = data_transformation_config()
    
    def get_transformer_object(self):
        '''
        This function is responsible for Data transformation ( in train and test )
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            
            num_pipeline= Pipeline(                               # for numerical features we define this pipeline
                steps=[
                ("imputer",SimpleImputer(strategy="median")),     #for handeling missing values
                ("scaler",StandardScaler())                       # standerdize the data
                ]
            )
            
            cat_pipeline=Pipeline(                                # for categorical features we define this pipeline

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),    #for handeling the missing values ( using mode)
                ("one_hot_encoder",OneHotEncoder()),                    # ENCODING
                ("scaler",StandardScaler(with_mean=False)) #used to safely scale sparse one-hot encoded features. for models like (Linear Regression,Logistic Regression,SVM,Neural Networks)
                ]
            )
            
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")
            
            preprocessor=ColumnTransformer(                         # Column Transfer ( changes in numerical and categorical features )
                [
                ("num_pipeline",num_pipeline,numerical_columns),    # for numerical features
                ("cat_pipelines",cat_pipeline,categorical_columns)  # for categorical features
                ]
            )
            
            return preprocessor
        
        except Exception as e:
            raise CustomeException(e,sys)
        
    
    def initiate_data_transformation(self,train_path,test_path):
        '''
        
        '''
        try:
            train_df=pd.read_csv(train_path)       # reading the train.csv file
            test_df = pd.read_csv(test_path)       # reading the test.csv file
            
            logging.info('Read train and test data completed')     
            logging.info('Obtaining prepocessing data')
            
            prepocessing_obj = self.get_transformer_object()    # calling the method get_transformer_object from the class DataTransformation
            
            target_column_name = 'math_score'
            numerical_columns = ['writing_score','reading_score']
            
            input_feature_train_df = train_df.drop(columns=[target_column_name])    # temporary droping the Target column from training df ( X )
            target_feature_train_df = train_df[target_column_name]                         # seperated the (y)
            
            input_feature_test_df = test_df.drop(columns=[target_column_name])      # similarly for the test data seperating the ( X and y)
            target_feature_test_df = test_df[target_column_name]
            
            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe.") 
            
            input_feature_train_arr=prepocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=prepocessing_obj.transform(input_feature_test_df)
            
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=prepocessing_obj
                )
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomeException(e,sys)