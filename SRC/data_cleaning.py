import os
import pandas as pd
class datacleaning:
    def __init__(self):
        pass

    def data_cleaning(self):
        os.makedirs(r'C:\Users\Admin\Downloads\bootcamp\Data\raw_data', exist_ok=True)
        df=pd.read_csv(r'C:\Users\Admin\OneDrive\Documents\Artificail Intelligence\titanic_train.csv')
        df.to_csv(r'C:\Users\Admin\Downloads\bootcamp\Data\clean_data\clean.csv',index=False)
        round(df.isnull().sum()/len(df)*100,2)
        df[df['Embarked'].isnull()]
        df['Embarked']=df['Embarked'].fillna('S')
        df[df['Age']==df['Age'].min()]
        df[df['Age']==df['Age'].max()]
        df['Age'][df['Survived']==1].median()
        df['Sex'][df['Survived']==0].value_counts()
        df['Survived'][df['Age'].isnull()].value_counts()
        df['Age'][df['Pclass']==1].median()
        df['Age'][df['Pclass']==2].median()
        df['Age'][df['Pclass']==3].median()
        df['Age']=df['Age'].fillna(30)
        df=df[['Survived', 'Pclass','Sex', 'Age', 'SibSp','Parch','Fare','Embarked']]


if __name__=='__main__':
    try:
        obj=datacleaning()
        obj.data_cleaning()
    except Exception as e:
        raise  e

