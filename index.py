import streamlit as st
import requests 
import json

def search_patient(name):
    url = f"http://127.0.0.1:8000/api/patients/{name}/"
    response = requests.get(url)
    return response.json()['patients']

def upload_patient(name, phone, email, image):
    upload_url = f"http://127.0.0.1:8000/api/upload/"
    data = {
        'name': name,
        'phone': phone,
        'email': email,
    }
    files = {'image': image}
    response = requests.post(upload_url, data=data, files=files)

    if response.text:  # Check if the response is not empty
        try:
            response_data = response.json()
        except json.JSONDecodeError as e:
            st.error(f"Failed to decode JSON response: {str(e)}")
            response_data = {}
    else:
        st.error("Empty response received from the server.")
        response_data = {}

    return response_data

def display_patient_data(patient_data):
    st.header("Search Results:")
    for patient in patient_data:
        st.write(f"Name: {patient['name']}")
        st.write(f"Phone: {patient['phone']}")
        st.write(f"Email: {patient['email']}")
        st.write(f"Report ID: {patient['report_id']}")
        st.write(f"Report URL: {patient['report_url']}")
        st.write(f"Source URL: {patient['src_url']}")
        st.write("---")

st.title("Patient Search and Upload App")

# User input fields for search
search_name = st.text_input("Enter the name to search:")

# Button to trigger the search
if st.button("Search"):
    if search_name:
        # Call the backend API to get patient data
        patients = search_patient(search_name)

        # Display patient data
        if patients:
            display_patient_data(patients)
        else:
            st.warning("No matching patients found.")
    else:
        st.warning("Please enter a name to search.")

# User input fields for upload
st.title("Upload New Patient")

new_name = st.text_input("Name:")
new_phone = st.text_input("Phone:")
new_email = st.text_input("Email:")
new_image = st.file_uploader("Upload Image:", type=["jpg", "jpeg", "png"])

# Button to trigger the upload
if st.button("Upload"):
    if not all([new_name, new_phone, new_email, new_image]):
        st.warning("Please fill in all fields and upload an image.")
    else:
        uploaded_data = upload_patient(new_name, new_phone, new_email, new_image)

        if 'id' in uploaded_data:
            st.success("Upload successful!")
            st.write("Uploaded Patient Data:")
            st.write(f"ID: {uploaded_data['id']}")
            st.write(f"Name: {uploaded_data['name']}")
            st.write(f"Phone: {uploaded_data['phone']}")
            st.write(f"Email: {uploaded_data['email']}")
            st.write("Uploaded Image:")
            st.image(uploaded_data['report']['src'], caption="Source Image", use_column_width=True)
        else:
            st.error("Upload failed.")
