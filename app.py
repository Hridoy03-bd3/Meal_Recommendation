import streamlit as st
import numpy as np
import joblib

# Load your saved model
model = joblib.load("random_forest_model.pkl")  # replace with your model file

st.title("🍲 Meal Suggestion ML App")
st.write("Provide your details below to get a meal suggestion:")

# --- Input Fields ---
age = st.selectbox("Age", ["18-20", "21-23", "23-26"])
gender = st.selectbox("Gender", ["Male", "Female"])
height = st.selectbox("Height (in feet and inch)", [
    "Below 5 feet 0 inches", "5 feet 0 inches – 5 feet 3 inches",
    "5 feet 4 inches – 5 feet 7 inches", "5 feet 8 inches – 5 feet 11 inches"
])
weight = st.selectbox("Weight (kg)", [
    "Below 45 kg (Potentially Underweight)",
    "45 kg – 55 kg",
    "56 kg – 65 kg",
    "66 kg – 75 kg",
    "76 kg or Above (Potentially Overweight/Obese)"
])
smoking_status = st.selectbox("Smoking Status", ["Yes", "No"])
residential = st.selectbox("Are you a residential student?", ["Yes", "No"])
marital_status = st.selectbox("Marital Status", ["Married", "Unmarried"])
sleep = st.selectbox("How much sleep did you get last night?", [
    "Low Sleep (Less than 5 hours)",
    "Moderate (5-6 hours)",
    "Optimal (7-8 hours)",
    "Excessive (9+ hours)"
])
stress = st.selectbox("Current stress/anxiety level", ["Low/Calm", "Moderate", "High/Exam Stress"])
activity_level = st.selectbox("Physical activity level today", [
    "Sedentary (Mostly sitting/studying )",
    "Light (Walking to class/stairs)",
    "Moderate (Gym/Sports less than 60 mins)",
    "Vigorous (Sports more than 60 mins/Heavy labor)"
])
last_meal = st.selectbox("Last proper meal?", [
    "Less than 2 hours ago",
    "2-4 hours ago",
    "4-6 hours ago (Optimal hunger)",
    "More than 6 hours ago (Skipped meal/High hunger)"
])
hunger = st.selectbox("Current hunger level", [
    "Not hungry at all",
    "Slightly hungry",
    "Moderately hungry (Ready to eat)",
    "Very hungry (Feeling weak/distracted)"
])
skipped_meal = st.selectbox("Have you skipped a meal today?", [
    "No, I have not skipped a meal.",
    "Yes, I skipped Breakfast",
    "Yes, I skipped Lunch",
    "Yes, I skipped Dinner"
])

# --- Encoding Function ---
def encode_input():
    encoding = {
        "Age": {"18-20":0, "21-23":1, "23-26":2},
        "Gender": {"Male":2, "Female":1, "Other":0},
        "Height": {
            "Below 5 feet 0 inches":0,
            "5 feet 0 inches – 5 feet 3 inches":0,
            "5 feet 4 inches – 5 feet 7 inches":1,
            "5 feet 8 inches – 5 feet 11 inches":2
        },
        "Weight": {
            "Below 45 kg (Potentially Underweight)":0,
            "45 kg – 55 kg":1,
            "56 kg – 65 kg":2,
            "66 kg – 75 kg":3,
            "76 kg or Above (Potentially Overweight/Obese)":4
        },
        "Smoking Status":{"Yes":1, "No":0},
        "Residential":{"Yes":1, "No":0},
        "Marital Status":{"Married":1, "Unmarried":0},
        "Sleep":{
            "Low Sleep (Less than 5 hours)":0,
            "Moderate (5-6 hours)":1,
            "Optimal (7-8 hours)":2,
            "Excessive (9+ hours)":3
        },
        "Stress":{
            "Low/Calm":0,
            "Moderate":1,
            "High/Exam Stress":2
        },
        "Activity Level":{
            "Sedentary (Mostly sitting/studying )":0,
            "Light (Walking to class/stairs)":1,
            "Moderate (Gym/Sports less than 60 mins)":2,
            "Vigorous (Sports more than 60 mins/Heavy labor)":3
        },
        "Last Meal":{
            "Less than 2 hours ago":0,
            "2-4 hours ago":1,
            "4-6 hours ago (Optimal hunger)":2,
            "More than 6 hours ago (Skipped meal/High hunger)":3
        },
        "Hunger":{
            "Not hungry at all":0,
            "Slightly hungry":1,
            "Moderately hungry (Ready to eat)":2,
            "Very hungry (Feeling weak/distracted)":3
        },
        "Skipped Meal":{
            "No, I have not skipped a meal.":0,
            "Yes, I skipped Breakfast":1,
            "Yes, I skipped Lunch":2,
            "Yes, I skipped Dinner":3
        }
    }

    return [
        encoding["Age"][age],
        encoding["Gender"][gender],
        encoding["Height"][height],
        encoding["Weight"][weight],
        encoding["Smoking Status"][smoking_status],
        encoding["Residential"][residential],
        encoding["Marital Status"][marital_status],
        encoding["Sleep"][sleep],
        encoding["Stress"][stress],
        encoding["Activity Level"][activity_level],
        encoding["Last Meal"][last_meal],
        encoding["Hunger"][hunger],
        encoding["Skipped Meal"][skipped_meal]
    ]

# --- Prediction ---
if st.button("Get Meal Suggestion"):
    input_data = np.array([encode_input()])
    prediction = model.predict(input_data)
    st.success(f"🍽 Suggested meal: {prediction[0]}")
