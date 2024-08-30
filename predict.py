import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("CatBoost_adv_stars_class.pkl")

# Title of the web app
st.set_page_config(page_title="Star Classification App", page_icon="🌟🔭", layout="wide")
st.title("Star Classification App")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
            font-family: 'Arial', sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #f7f7f7;
        }
        .css-1lcbmhc {
            overflow: auto;
        }
        .stButton button {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }
        .prediction-box {
            background-color: #333;
            border: 1px solid #fff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
         .note-box {
            background-color: #333; /* Dark background */
            color: #fff; /* White text color */
            border: 1px solid #444; /* Slightly lighter border */
            border-radius: 10px;
            padding: 10px;
            margin-top: 20px;
        }
        .icon {
            font-size: 24px;
            vertical-align: middle;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for user input
st.sidebar.header("Input Features")

def user_input_features():
    alpha = st.sidebar.slider("Alpha", 0.0, 360.0, 180.0)
    delta = st.sidebar.slider("Delta", -90.0, 90.0, 0.0)
    u = st.sidebar.slider("u", 0.0, 30.0, 15.0)
    g = st.sidebar.slider("g", 0.0, 30.0, 15.0)
    r = st.sidebar.slider("r", 0.0, 30.0, 15.0)
    i = st.sidebar.slider("i", 0.0, 30.0, 15.0)
    z = st.sidebar.slider("z", 0.0, 30.0, 15.0)
    redshift = st.sidebar.slider("Redshift", 0.0, 10.0, 0.5)
    plate = st.sidebar.slider("Plate", 0, 9999, 1000)
    MJD = st.sidebar.slider("MJD", 0, 100000, 50000)

    data = {
        'alpha': alpha,
        'delta': delta,
        'u': u,
        'g': g,
        'r': r,
        'i': i,
        'z': z,
        'redshift': redshift,
        'plate': plate,
        'MJD': MJD
    }

    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
input_df = user_input_features()

# Display user input
st.subheader('User Input Features')
st.write(input_df)

# Make prediction
prediction = model.predict(input_df)

# Display the prediction result
st.subheader('Prediction Result')

# Customize the prediction message
prediction_message = ""
if prediction[0] == 'GALAXY':
    prediction_message = "🌌 It's  a  `Galaxy` "
elif prediction[0] == 'QSO':
    prediction_message = "🛰️🔭 It's  a  `QSO` "
else:
    prediction_message = "⭐ It's  a  `Star` "

st.markdown(f"<div class='prediction-box'>{prediction_message}</div>", unsafe_allow_html=True)

# Add more details or a description below the result
st.markdown("""
<div class="note-box">
    <strong>Note:</strong> The classification is based on the model's analysis of features like alpha, delta, magnitudes in different bands (u, g, r, i, z), redshift, and observation data (plate, MJD).
</div>
""", unsafe_allow_html=True)

this is
adv_stars_class_app.py

create more 6 multi page .py files 
and give one home page and navigation bar