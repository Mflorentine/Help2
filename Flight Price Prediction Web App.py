# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 14:45:20 2025

@author: pc
"""

# import necessary library
import numpy as np
import joblib
import streamlit as st


loaded_model = joblib.load('Model.pkl')


# Creating a function


def Flight_Price_Prediction(input_data):
    
    predicted_price = loaded_model.predict(input_data)
    return f"Predicted price: {predicted_price[0]:.2f} RWF"



#creating the main function here streamlit library is going to be used

def main():
    
    
    # 1st giving the Title of the web App
    
    st.title('Flight Price Prediction System Web App')
    st.write("Welcome to the app!")  

    
    
    # Getting the Input data to the system from the user
    
    
    airline = st.text_input('Enter the Air line Name')
    flight = st.text_input('Enter flight')
    source_city = st.text_input('Source city')
    departure_time = st.text_input('Time of Departure')
    stops = st.text_input('Stop point')
    arrival_time = st.text_input('Time of Arrival')
    destination_city = st.text_input('Destination City')
    #Class = st.text_input('Class (Business or Economy)')
    Class = st.selectbox("Class", ["Economy", "Business"])
    # duration = st.text_input('Time Duration')
    duration = st.slider('Flight Duration (hours)', 0.0, 20.0, step=0.5)
    days_left = st.text_input('Days Left for the Journey')
    
    
    # Code for the prediction 
    
    Pricing = ''
    
    # Creating the Button for Prediction
    
    if st.button('Get Price'):
        Pricing = Flight_Price_Prediction([airline, flight, source_city, departure_time,  stops, arrival_time, destination_city, Class, duration, days_left])
        
    st.success(Pricing)
    
    
    if __name__ == '__main__' :
        main()
    
        
        
        
        
        
        
    
    
    

    
