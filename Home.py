import streamlit as st


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



with col2:
   if st.button("🔍 Predict"):
         st.session_state.page = "Predict"
         st.switch_page("D:/house_price/Pages/predict.py")


st.markdown("<hr>", unsafe_allow_html=True)

# # CONTENT
st.markdown("""
<div class="card">
    <h2 class="section-title">Welcome to House Price Prediction. 👋</h2>
                 <p>The <b>House Price Prediction System</b> is a machine learning -based web application that
            helps users estimate properly prices using house details like location,area and features.
            It uses machine learning to analyze housing data and provide quick price estimates.
            This helps buyers and sellers make better real estate decisions easily.</p>
<div class="card2">            
    <h3>Key Features</h3>
    <ul>
           <li> Easy House price prediction</li>
           <li> Random Forest Machine Learning model</li>
           <li> Simple user input interface</li>
           <li> Helps buyers and seller compare prices</li>
   </ul>
   <h3>🌱Why This Project?</h3>
   <p>This project helps users understand the approximate value of a properly before buying or selling.It simplifies real estate decisions using data-driven predictions.</p>
  
 </div>

    
 </div>
""", unsafe_allow_html=True)