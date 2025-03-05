import pandas as pd
import os

class datapreprocessing:
    def __init__(self):
        pass
    def data_preprocessing(self):
        os.makedirs(r'C:\Users\Admin\Downloads\bootcamp\Data\clean_data', exist_ok=True)
        df=pd.read_csv(r'C:\Users\Admin\Downloads\bootcamp\Data\clean_data\clean.csv')
        df.to_csv(r'C:\Users\Admin\Downloads\bootcamp\Data\preprocess_data\preprocess.csv',index=False)
        df['Male']=pd.get_dummies(df['Sex'],dtype=int,drop_first=True)
        df.drop('Sex',axis=1,inplace=True)
        df[['Q','S']]=pd.get_dummies(df['Embarked'],dtype=int,drop_first=True)
        df.drop('Embarked',axis=1,inplace=True)

if __name__=='__main__':
    try:
        obj=datapreprocessing()
        obj.data_preprocessing()
    except Exception as e:
        raise e
