import streamlit as st
from azure.storage.blob import BlobServiceClient
from io import BytesIO

# Azure Storage Account details
azure_storage_account_name = "mitrejson"
azure_storage_account_key = "Gc8RX3y8gdKZNFxMTlG3ZhOwYXahPzZ9SYJZ95m13Q9LQWrTrp2b4klI1cuxIupuMNVa91Rv85px+AStzyNUdg=="
container_name = "layers"

# Function to upload file to Azure Storage
def upload_to_azure_storage(file):
    blob_service_client = BlobServiceClient.from_connection_string(f"DefaultEndpointsProtocol=https;AccountName={azure_storage_account_name};AccountKey={azure_storage_account_key}")
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.name)
    blob_client.upload_blob(file)

# Streamlit App
st.title("Azure Storage Uploader")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.image(uploaded_file)

    # Upload the file to Azure Storage on button click
    if st.button("Upload to Azure Storage"):
        upload_to_azure_storage(uploaded_file)
        st.success("File uploaded to Azure Storage!")
