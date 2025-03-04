# ML-Based Automatic Solar Tracking System

## 🌞 Project Overview
This project utilizes **Machine Learning (XGBoost)** to predict the **optimal solar panel tilt angle** based on power generation and the hour of the day. The system helps improve solar energy efficiency by dynamically adjusting panel angles.

## 🚀 Features
- **Predicts Solar Elevation Angle** based on Power and Hour of the day.
- **Machine Learning Model:** XGBoost Regressor.
- **Web Application:** Built with Streamlit for user-friendly interaction.
- **Real-time Solar Computation** using `pysolar`.

## 📂 Project Structure
```
├── solar_tracking_data.csv      # Dataset
├── train_solar_model.py         # Model training script
├── app.py                       # Streamlit Web App
├── xgboost_solar_model.pkl      # Trained Model
├── scaler.pkl                   # Feature Scaler
├── README.md                    # Project Documentation

