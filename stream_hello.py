import streamlit as st

# Add a title to the app
st.title("Simple Streamlit App")

# Add a header
st.header("Welcome to Streamlit!")

# Add some text
st.write("This is a simple Streamlit app.")

# Add an interactive widget
user_input = st.text_input("Please enter your name:")
st.write(f"Hello, {user_input}!")

# Add a button
button_clicked = st.button("Click me!")
if button_clicked:
    st.write("Button clicked!")

# Add a checkbox
checkbox_state = st.checkbox("Check me!")
if checkbox_state:
    st.write("Checkbox checked!")

# Add a selectbox
option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")

# Add a slider
slider_value = st.slider("Select a value", 0, 10)
st.write(f"Slider value: {slider_value}")
