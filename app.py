import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Title
st.title("Freight Cost Predictor")

# Inputs
panels = st.number_input("Number of Panels", min_value=1)
miles = st.number_input("Loaded Miles", min_value=1)
trucks = st.number_input("Number of Trucks", min_value=1)

# Median fuel cost fallback
fuel_cost_median = 3.75  # You may update this after loading your real dataset

if st.button("Predict Cost"):
    weight = panels * 160
    weight_per_truck = weight / 13440
    trucks_x_miles = trucks * miles * (0.9 if trucks == 1 else 1)
    long_miles = int(miles > (400 if trucks == 1 else 500))
    miles_x_fuel = miles * fuel_cost_median

    # Dummy date values (model expects these)
    year, month, day, weekday = 2024, 1, 1, 0

    input_df = pd.DataFrame([
        [panels, weight, miles, weight_per_truck, trucks, fuel_cost_median,
         long_miles, miles_x_fuel, trucks_x_miles, year, month, day, weekday]
    ], columns=[
        'panels', 'weight', 'miles', 'weight_per_truck', 'trucks', 'fuel_cost',
        'long_miles', 'miles_x_fuel', 'trucks_x_miles', 'year', 'month', 'day', 'weekday'
    ])

    try:
        model = joblib.load("model_pipeline.pkl")
        prediction = model.predict(input_df)[0] * 1.08
        st.success(f"Predicted Freight Cost: ${prediction:.2f}") 
    except Exception as e:
        st.error(f"Failed to load model: {e}")