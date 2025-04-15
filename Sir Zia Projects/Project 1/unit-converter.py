import streamlit as st

st.title("Unit Coneverter App :computer:")
st.write("### Converts Length, Weight and Time Instantly!")
st.write("Note: the answers are correct to two significant figures!!!")

# Here the user chooses the category of which Unit he wants to convert. 
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Here is another selectbox of which properties change according to the category he choose above

if category == "Length":
  unit = st.selectbox("Select Your Units for Conversion", ["Kilometers to Miles","Miles to Kilometers"])
elif category == "Weight":
  unit = st.selectbox("Select Your Units for Conversion", ["Kilograms to Pounds","Pounds to Kilograms"])
elif category == "Time":
  unit = st.selectbox("Select Your Units for Conversion", ["Seconds to Minutes","Minutes to Seconds","Minutes to Hours","Hours to Minutes","Hours to Days","Days to Hours"])

# Here i take the vaule from the user to carry on with the conversion
value = st.number_input("Enter You Value For Conversion")

# Here is a function which carries out the calculation for the conversion
def converter_function(category, value, unit):
  if category == "Length":
    if unit == "Kilometers to Miles":
      return value * 0.621371
    elif unit == "Miles to Kilometers":
      return value / 0.621371
  
  elif category == "Weight":
    if unit == "Kilograms to Pounds":
      return value * 2.20462
    elif unit == "Pounds to Kilograms":
      return value / 2.20462
    
  elif category == "Time":
    if unit == "Seconds to Minutes":
      return value / 60
    elif unit == "Minutes to Seconds":
      return value * 60
    elif unit == "Minutes to Hours":
      return value / 60
    elif unit == "Hours to Minutes":
      return value * 60
    elif unit == "Hours to Days":
      return value / 24
    elif unit == "Days to Hours":
      return value * 24
  
  return "something went wrong"

# this is a Button, which when it is clicked it calls the function above to to carry out the conversion.
if st.button("convert"):
  result = converter_function(category, value, unit)
  st.success(f"the result is {result:.2f}")