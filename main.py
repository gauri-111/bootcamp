from SRC.data_collection import datacollection

try:
    obj=datacollection()
    obj.data_collection()
    print("Stage data collection completed successfully")
except Exception as e:
    raise e


from SRC.data_cleaning import datacleaning

try:
    obj=datacleaning()
    obj.data_cleaning()
    print("Stage data cleaning completed successfully")
except Exception as e:
    raise e


from SRC.preprocessing import datapreprocessing

try:
    obj=datapreprocessing()
    obj.data_preprocessing()
    print("Stage data preprocessing completed successfully")
except Exception as e:
    raise e


from SRC.data_model import datamodel

try:
    obj=datamodel()
    obj.data_model()
    print("Stage data model completed successfully")
except Exception as e:
    raise e


from SRC.data_htuning import datahtuning

try:
    obj=datahtuning()
    obj.data_htuning()
    print("Stage data hyperparameter tuning  completed successfully")
except Exception as e:
    raise e