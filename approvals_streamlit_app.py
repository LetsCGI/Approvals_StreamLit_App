import streamlit 
streamlit.title('Data Classification Approvals App')

class myProgram:
    global container
    global colors
    global i
   
   def __init__(self, root):
        self.container = root
        self.colors = ["blue", "yellow", "red", "black", "purple", "white"]
        self.i = 0
        self.createView()
