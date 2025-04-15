import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker!", page_icon="🔐")

st.title("🔐Password Strength Checker")
st.write("""
## welcome to a basic password strength checker! 👋
use this tool to check the strength of your password and get extra suggestions on how to make it stronger
go ahead and give it a try!!!
""")

password = st.text_input("Enter you Password", type="password")

feedback = []

score = 0

# Set of conditional operators to check the strength of the password

if password:
  # Length Check
  if len(password) >= 8:
        score += 1
  else:
       feedback.append("❌Password must be at least 8 characters long.")
  # Capital and Small letter Check
  if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
  else:
        feedback.append("❌Password must contain both upper and lower case characters.")
  # Number check
  if re.search(r'[0-9]', password):
        score +=1
  else:
       feedback.append("❌Password must contain at least 1 number")
  # Special Character check
  if re.search(r'[!@#$%^&*]', password):
    score += 1
  else:
       feedback.append("❌Password must contain at least 1 special charater (!@#$%^&*)")
  
  # Password strength teller according to score
  if score == 4:
        feedback.append("✅Your password is strong!🎉")
  elif score == 3:
        feedback.append("🟡Your password is medium strength. It could be stronger.")
  else:
        feedback.append("🔴Your password is weak. Please make it stronger.") 
    
  # For loop to display content in Feedback

  if feedback:
      st.write("## suggestions: ")
      for word in feedback:
           st.write(word)
else:
    st.info("please type the password to Begin, press ENTER after you have writen the password!!")