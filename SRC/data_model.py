import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix , classification_report , accuracy_score
import numpy as np
import joblib
import os
class datamodel:
    def __init__(self):
        pass

    def data_model(self):
        df=pd.read_csv(r'C:\Users\Admin\Downloads\bootcamp\Data\preprocess_data\preprocess.csv')
        X=df.drop('Survived',axis=1)
        y=df['Survived']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
        models=[LogisticRegression(), RandomForestClassifier(), AdaBoostClassifier(),DecisionTreeClassifier()]
        d={}
        for i in models:
            i.fit(X_train,y_train)
            pred= i.predict(X_test)
            acc=accuracy_score(y_test,pred)
            if acc not in d:
                d[i]=acc

        model = [a for a,b in d.items() if b ==max(d.values())][0]
        os.makedirs(r'C:\Users\Admin\Downloads\bootcamp\Models', exist_ok=True)
        joblib.dump(model,r'C:\Users\Admin\Downloads\bootcamp\Models\model')

if __name__=='__main__':
    try:
        obj=datamodel()
        obj.data_model()
    except Exception as e:
        raise  e