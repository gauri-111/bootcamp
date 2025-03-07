## End to End Data Science Project
# End-to-End Machine Learning Project

## Overview
This project is an end-to-end machine learning pipeline that covers data collection, preprocessing, model training, hyperparameter tuning, and deployment using Streamlit. The models trained include:

- **Logistic Regression**
- **Random Forest Classifier**
- **AdaBoost Classifier**
- **Decision Tree Classifier**

After training, the best-performing model was selected and deployed using a Streamlit web application.

---

## Project Structure
```
BOOTCAMP/
│── Data/
│   │── clean_data/
│   │   ├── clean.csv
│   │── preprocess_data/
│   │   ├── preprocess.csv
│   │── raw_data/
│   │   ├── raw.csv
│
│── Models/
│   │── best_model/
│   │── model/
│
│── Notebook/
│   │── Data_cleaning.ipynb
│   │── Data_collection.ipynb
│   │── Hyperparameter_tuning.ipynb
│   │── Model_train.ipynb
│   │── Preprocessing.ipynb
│
│── SRC/
│   │── data_cleaning.py
│   │── data_collection.py
│   │── data_htuning.py
│   │── data_model.py
│   │── preprocessing.py
│
│── app.py  # Streamlit application
│── requirements.txt  # Dependencies
│── README.md  # Documentation
```

---

## Steps in the ML Pipeline

### 1. Data Collection
- The raw data is collected and stored in the `Data/raw_data/raw.csv` file.
- Script: `data_collection.py`
- Notebook: `Data_collection.ipynb`

### 2. Data Cleaning & Preprocessing
- Handle missing values, duplicate entries, and inconsistencies.
- Feature engineering and transformations are applied.
- Store cleaned data in `Data/clean_data/clean.csv`.
- Script: `data_cleaning.py`
- Notebook: `Data_cleaning.ipynb`

### 3. Data Preprocessing
- Normalize and standardize numerical features.
- Encode categorical variables.
- Store preprocessed data in `Data/preprocess_data/preprocess.csv`.
- Script: `preprocessing.py`
- Notebook: `Preprocessing.ipynb`

### 4. Model Training
- Train four models: Logistic Regression, Random Forest Classifier, AdaBoost Classifier, and Decision Tree Classifier.
- Evaluate models using accuracy metrics.
- Save trained models.
- Script: `data_model.py`
- Notebook: `Model_train.ipynb`

Model Performance:
| Model                  | Accuracy |
|------------------------|----------|
| Logistic Regression    | 0.7488   |
| Random Forest          | 0.7668   |
| AdaBoost Classifier    | 0.7892   |
| Decision Tree          | 0.7488   |

### 5. Hyperparameter Tuning
- Optimize the best-performing model (AdaBoost Classifier) using hyperparameter tuning.
- Save the optimized model in `Models/best_model/`.
- Script: `data_htuning.py`
- Notebook: `Hyperparameter_tuning.ipynb`

### 6. Model Deployment
- Load the best model.
- Build a simple Streamlit web app (`app.py`) for predictions.
- Deploy the app to a hosting service.

---

## Running the Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit App
```bash
streamlit run app.py
```

---

## Future Improvements
- Add more feature engineering techniques.
- Experiment with additional models.
- Deploy the model using cloud services like AWS or GCP.

---

## Conclusion
This project provides a complete pipeline from data collection to deployment, demonstrating best practices in machine learning model development and deployment. 🚀

