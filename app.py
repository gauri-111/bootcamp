import streamlit as st
import pandas as pd
import joblib
import numpy as np 

model= joblib.load(r'C:\Users\Admin\Downloads\bootcamp\Models\best_model')
st.header("Titanic Prediction.App")


#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
ID=st.number_input("Enter your ID")
Pclass=st.number_input("Enter your class")
Name=st.text_input("Enter your name")
Sex = st.selectbox("Select Gender", ["Male", "Female"])
Age=st.number_input("Enter your age here")
SibSp=st.number_input("Enter the number of siblings/spouse")
Parch=st.number_input("enter the number of prents and childrens")
Tickets=st.text_input("enter your ticket number")
Fare=st.number_input("Enter fare amount")
Cabin=st.text_input("Enter your cabin id")
Embarked=st.text_input("Enter from where you embarked")

data = {
    "ID": [ID],
    "Pclass": [Pclass],
    "Name": [Name],
    "Sex": [Sex],
    "Age": [Age],
    "SibSp": [SibSp],
    "Parch": [Parch],
    "Tickets": [Tickets],
    "Fare": [Fare],
    "Cabin": [Cabin],
    "Embarked": [Embarked]
}

df = pd.DataFrame(data)
st.write(df)
df['Male']=pd.get_dummies(df['Sex'],dtype=int,drop_first=True)
df.drop('Sex',axis=1,inplace=True)
df[['Q','S']]=pd.get_dummies(df['Embarked'],dtype=int,drop_first=True)
df.drop('Embarked',axis=1,inplace=True)


pred=model.predict(df)
submit= st.button("Enter to see the prediction")
if submit:
    st.subheader("The prediction is:")
    st.write(pred)