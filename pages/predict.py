import streamlit as st
import pandas as pd
import pickle

# Load model and columns
model = pickle.load(open("D:/house_price/house_model.pkl", "rb"))
model_columns = pickle.load(open("D:/house_price/src/model_columns.pkl", "rb"))

st.markdown("""
    <style>

    /* Remove sidebar */
    [data-testid="stSidebar"] {
         display: none;
     }
                
     .css-1d391kg{
                 display:none;
                 }

     [data-testid="stSidebarNav"]{
     display:none;
     }

     /* Page background */
     .stApp {
         background: black;
         /background:#82AB7D;/
         font-family: 'Segoe UI', sans-serif;
     }

     /* Header title */
     .header-title {
         font-size: 35px;
         font-weight: 700;
         color: white;
         padding:20px;
         margin-bottom:20px;
         text-align: center;
     }
                
    .navbar{
       display:flex;
       justify-content:center;
       gap:15px;
       margin-bottom:25px;
    }

    /* Navigation buttons */
    div.stButton > button {
        /*background-color: #6A6B4E; */
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        padding: 8px 16px;
         font-weight: 600;
        border: none;
        transition: 0.3s ease;
        
    }

    div.stButton > button:hover {
        background-color: #1e40af;
        transform: scale(1.05);     }

    /* Cards */
    .card {
        background-color: black;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 8px 24px rgba(0,0,0,0.1);
        margin-top: 20px;
    }

    /* Section titles */
    .section-title {
        font-size: 22px;
        font-weight: 600;
        color: white;
        margin-bottom: 10px;
    }

    </style>
    """, unsafe_allow_html=True)

st.set_page_config(layout="wide")
st.markdown('<div class="header-title">Welcome to House Price Prediction.</div>', unsafe_allow_html=True)
st.markdown("")
# HEADER
col1, col2= st.columns([1,1])

 #with col1:
     # st.markdown('<div class="header-title">🚗 CO₂ Emission Prediction System</div>', unsafe_allow_html=True)

with col1:
    if st.button("🏠Home"):
       st.session_state.page = "home"
       st.switch_page("D:/house_price/Home.py")




with col2:
   if st.button("🔍 Predict"):
         st.session_state.page = "Predict"
         st.switch_page("D:/house_price/Pages/predict.py")


st.markdown("<hr>", unsafe_allow_html=True)

# st.title("House Price Prediction")

# Inputs
area = st.number_input("Area (sqft)", 500, 10000, 1200)
bed = st.number_input("Bedrooms", 1, 10, 2)

location = st.text_input("Location (example: Sarjapur)")
car_parking = st.selectbox("Car Parking", ["No", "Yes"])
swimming_pool = st.selectbox("Swimming Pool", ["No", "Yes"])

if st.button("Predict Price"):

    # Create empty input
    input_data = {col: 0 for col in model_columns}

    # Fill numeric fields
    if "Area" in input_data:
        input_data["Area"] = area

    if "BED" in input_data:
        input_data["BED"] = bed

    # Car parking
    if "CarParking" in input_data:
        input_data["CarParking"] = 1 if car_parking == "Yes" else 0

    # Swimming pool
    if "SwimmingPool" in input_data:
        input_data["SwimmingPool"] = 1 if swimming_pool == "Yes" else 0

    # Location (one-hot encoded columns)
    loc_column = f"Location_{location}"
    if loc_column in input_data:
        input_data[loc_column] = 1

    # Create dataframe
    df = pd.DataFrame([input_data])
    df = df[model_columns]

    prediction = model.predict(df)[0]

    st.success(f"Estimated Price: ₹ {prediction:,.2f}")