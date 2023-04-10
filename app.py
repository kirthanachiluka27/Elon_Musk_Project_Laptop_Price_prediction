import streamlit as st
import pickle
import pandas as pd
import numpy as np

#Loading the Model
pickle_in = open("model.pkl","rb")
regressor=pickle.load(pickle_in)

def predict(Brand, Processor_name, Processor_generation,ram_type, ram_capacity, storage, screen_size_inch, OS):
    prediction = regressor.predict([[Brand, Processor_name, Processor_generation,ram_type, ram_capacity, storage, screen_size_inch, OS]])
    result = int(prediction)
    return result



#Giving a Title
st.title("Laptop Price Prediction Application")
st.title("Elon Musk Project")



#Getting the input data from the user

Brand = st.selectbox("Brand",('Lenovo', 'ASUS', 'HP', 'DELL', 'RedmiBook', 'realme', 'acer','MSI', 'APPLE', 'Infinix', 'SAMSUNG', 'Ultimus', 'Vaio',
       'GIGABYTE', 'Nokia', 'ALIENWARE'))
#BRAND
if Brand == "Lenovo":
    Brand = 7
if Brand == "ASUS":
    Brand = 2
if Brand == "HP":
    Brand = 5
if Brand =="DELL":
    Brand = 3
if Brand == "RedmiBook":
    Brand = 10
if Brand == "realme":
    Brand = 15
if Brand == "acer":
    Brand = 14
if Brand == "MSI":
    Brand = 8
if Brand =="APPLE":
    Brand = 1
if Brand == "Infinix":
    Brand = 6
if Brand == "SAMSUNG":
    Brand = 11
if Brand == "Ultimus":
    Brand = 12

#Processor
Processor_name = st.selectbox("Processor",('Intel', 'AMD', 'Others'))
if Processor_name == "Intel":
    Processor_name = 1
if Processor_name == "AMD":
    Processor_name = 0
if Processor_name == "Others":
    Processor_name = 2

#Processor_gen
Processor_generation=st.selectbox("Processor_generation",(1,2,3,4,5,6,7,8,9,10))

#RAM_TYPE
ram_type = st.selectbox("ram_type",('DDR4', 'DDR5', 'LPDDR4','LPDDR4X', 'LPDDR5', 'LPDDR3'))
if ram_type == "DDR4":
    ram_type = 0
if ram_type == "DDR5":
    ram_type = 1
if ram_type == "LPDDR4":
    ram_type = 3
if ram_type == "LPDDR4X":
    ram_type = 4
if ram_type == "LPDDR5":
    ram_type = 5
if ram_type == "LPDDR3":
    ram_type = 2

ram_capacity = st.selectbox("ram_capacity",( 8, 16,  4,  1, 32))
storage = st.selectbox("storage",(32, 128, 256, 512, 1024))

#Disk_Type
screen_size_inch= st.selectbox("screen_size_inch",('HDD','SSD'))
if screen_size_inch == "HDD":
    screen_size_inch = 0
if screen_size_inch == "SSD":
    screen_size_inch = 1



#OS_TYPE
OS = st.selectbox("OS",("Windows","Mac OS","Others"))
if OS == "Windows":
    OS = 2
if OS == "Mac OS":
    OS = 0
if OS == "Others":
    OS = 1

result = ""

button = st.button("Predict")

#if button is pressed:

if button:
    result = predict(Brand, Processor_name, Processor_generation,ram_type, ram_capacity, storage, screen_size_inch, OS)

st.success(f'The Predicted price of the laptop is ${result}.....HURRAYYyyyyy....Hurry up to grab it ')

