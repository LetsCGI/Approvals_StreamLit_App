import streamlit as st
import snowflake.connector
import pandas as pd

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)



#from PIL import Image
#image = Image.open('C:\GitHub StreamLit Repository\Approvals_StreamLit_App/BankingAnalyticsLogo.png')
#st.image(image, caption='Sunrise by the mountains')

#st.image("C:\GitHub StreamLit Repository\Approvals_StreamLit_App/BankingAnalyticsLogo.png", use_column_width=True)


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
