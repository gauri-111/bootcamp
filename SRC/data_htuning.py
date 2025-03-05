from sklearn.model_selection import RandomizedSearchCV
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
class datahtuning:
    def __init__(self):
        pass

    def data_htuning(self):
        model = joblib.load(r'C:\Users\Admin\Downloads\bootcamp\Models\model')
        str(model)
        param_grids = {
            "LogisticRegression()": {
                "penalty": ["l1", "l2", "elasticnet", None],
                "C": np.logspace(-4, 4, 20),
                "solver": ["liblinear", "lbfgs", "newton-cg", "saga"],
                "max_iter": [100, 200, 300, 500],
            },
            "RandomForestClassifier()": {
                "n_estimators": [50, 100, 200, 300, 500],
                "max_depth": [None, 10, 20, 30, 50],
                "min_samples_split": [2, 5, 10],
                "min_samples_leaf": [1, 2, 4],
                "max_features": ["sqrt", "log2", None],
                "bootstrap": [True, False],
            },
            "AdaBoostClassifier()": {
                "n_estimators": [50, 100, 200, 300, 500],
                "learning_rate": np.logspace(-3, 0, 10),
                "algorithm": ["SAMME", "SAMME.R"],    
            },
            "DecisionTreeClassifier()": {
                "criterion": ["gini", "entropy", "log_loss"],
                "splitter": ["best", "random"],
                "max_depth": [None, 10, 20, 30, 50],
                "min_samples_split": [2, 5, 10],
                "min_samples_leaf": [1, 2, 4],
                "max_features": ["auto", "sqrt", "log2", None],
            }
        }

        param_grids = param_grids[str(model)]
        df=pd.read_csv(r'C:\Users\Admin\Downloads\bootcamp\Data\preprocess_data\preprocess.csv')
        X=df.drop('Survived',axis=1)
        y=df['Survived']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

        random_search = RandomizedSearchCV(
            estimator=model,
            param_distributions=param_grids,
            cv=5,
            scoring='accuracy',
            n_jobs=-1,
            random_state=42
            )
        random_search.fit(X_train, y_train)
        best_model = random_search.best_estimator_
        joblib.dump(best_model,r'C:\Users\Admin\Downloads\bootcamp\Models\best_model')
        
if __name__=='__main__':
    try:
        obj=datahtuning()
        obj.data_htuning()
    except Exception as e:
        raise  e