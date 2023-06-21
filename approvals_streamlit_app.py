import streamlit as st
from PIL import Image
image = Image.open('C:\GitHub StreamLit Repository\Approvals_StreamLit_App/BankingAnalyticsLogo.png')
st.image(image, caption='Sunrise by the mountains')


st.title('Data Classification Approvals App')
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

# button
st.button('Streamlit Button', help="Click here")
 
# check box
st.checkbox('Check Box')
 
# radio button
lang = st.radio(
    "What's your favorite programming language?",
    ('C++', 'Python'))
if lang == 'C++':
    st.write('You selected C++.')
else:
    st.write('You selected Python')
 
# slider
score = st.slider('Please specify your test score', 0, 100, 10)
st.write("My test score is ", score)
 
# Using object notation
add_selectbox = st.sidebar.radio(
    "Please choose an option",
    ("Option 1", "Option 2", "Option 3")
)
