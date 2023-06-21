import streamlit as st


# importing package
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

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('C:\GitHub StreamLit Repository\Approvals_StreamLit_App/BankingAnalyticsLogo.png')    
    
