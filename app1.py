import streamlit as st
import pandas as pd
import joblib
import datetime
import pytz
from pysolar.solar import get_altitude

# Load trained XGBoost model
model = joblib.load("solar1_model.pkl")  # Ensure the model is saved after training
scaler = joblib.load("scaler.pkl")  # Load the StandardScaler used during training

# Set location details
LATITUDE = 28.6139  # Example: New Delhi
LONGITUDE = 77.2090
TIMEZONE = "Asia/Kolkata"

def compute_solar_elevation(hour):
    # Assume a fixed date for simplicity
    date = datetime.datetime.utcnow().date()
    timestamp = datetime.datetime.combine(date, datetime.time(hour=hour, minute=0)).replace(tzinfo=pytz.utc)
    altitude = get_altitude(LATITUDE, LONGITUDE, timestamp)  # Solar Elevation Angle
    return altitude

# Streamlit App Interface
st.title("☀️ ML-Based Solar Angle Prediction")
st.markdown("Predict the solar elevation using Machine Learning.")

def user_input_features():
    power = st.number_input("Power (Watts)", min_value=0.0, value=100.0)
    hour = st.slider("Hour of the Day", 0, 23, 12)
    
    # Compute Solar Elevation
    solar_elevation = compute_solar_elevation(hour)
    
    # Create DataFrame
    data = {
        "Power": [power],
        "Hour": [hour],
    }
    return pd.DataFrame(data), solar_elevation

# Get user inputs
df_input, solar_elevation = user_input_features()

# Scale input data
df_input_scaled = scaler.transform(df_input)

# Predict Solar Elevation
if st.button("Predict Solar Elevation"):
    st.success(f"🌞 Computed Solar Elevation: {solar_elevation:.2f} degrees")
