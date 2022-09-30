import streamlit as st

from calculator import calculate

st.title("Hamburger Day Calculator App")

# taking user inputs
option = st.write("Select the numbers from slider below:")
guests = st.slider("Guests", 1, 30, 1)
portion_size = st.slider("Portion Size", 1., 5., 1., .5)

# converting the inputs into a json format
inputs = {"guests": guests, "portion_size": portion_size}

# when the user clicks on button it will fetch the API
if st.button("Calculate"):
    result = calculate(guests, portion_size)
    st.write("")
    st.subheader("---" * 10)
    st.text(f"Burger Quantity: {result.get('count_hamburgers')}")
    st.text(f"Meat Amount: {result.get('weight_meat'):.3f} kg")
    st.text(f"----- 80% Lean Meat: {result.get('weight_lean_meat'):.3f} kg")
    st.text(f"----- 20% Fat Meat: {result.get('weight_fat_meat'):.3f} kg")
    st.text(f"Cheese Amount: {result.get('weight_cheese'):.3f} kg")
    st.text(f"Amount of French Fries: {result.get('weight_french_fries'):.3f} kg")
    st.text(f"Amount of Hamburger Bun: {result.get('count_burger_bun')}")
