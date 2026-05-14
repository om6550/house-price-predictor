import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

house_size = np.array(
    [1000,1500,2000,2500,3000]
).reshape(-1,1)

house_price = np.array(
    [10,15,20,25,30]
)

model = LinearRegression()
model.fit(house_size, house_price)

st.title("HOUSE PRICE PREDICTOR")

st.write(
    "enter a house size to predict price"

)

size = st.number_input(
    "house size (sq ft)", 
    min_value=50
        
)
if st.button("predict price"):
    prediction = model.predict([[size]])
    
    st.success(
        f"Estimated Price: ₹ {prediction[0]:.2f} Lakh"
    )
