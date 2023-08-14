import streamlit as st
import os
import openpyxl

# st.title("Name");
# st.sidebar.selectbox("Pick A Cuisine", ("Kenya","Uganda","Tanzania","Ethiopian","Egyptian","Iranian","Thailand","American","Italian","French","South African"))

st.title("Excel Upload and Dialog Box")
# Upload Excel file
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Save the uploaded file
    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File saved successfully!")

    # Display dialog box button
    if st.button("Show Dialog Box"):
        print("name")
# show_dialog()
