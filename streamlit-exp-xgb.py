# Importing required libraries
import streamlit as st
import pandas as pd
import xgboost as xgb
import requests
import pickle
from io import BytesIO

# Loading the model from GitHub
@st.cache_data
def load_model_from_github():
    url = "https://github.com/lordchan/Network-Anomaly-Detection/blob/main/xgboost_model.pkl?raw=true"  # Replace with your model's GitHub URL
    response = requests.get(url)
    response.raise_for_status()  # This will raise an error if the file is not accessible
    model = pickle.loads(response.content)
    return model

# Load the model
model = load_model_from_github()

# Streamlit UI
st.title("🤖 Network Anomaly Detection using XGBoost")
st.write("Enter the details of your network and predict the chances of getting attacked with 99% accuracy!")
# Define the input fields
# Adjust these according to the model's features

col1, col2 = st.columns(2)
with col1:
    protocoltype = st.selectbox("Protocol used in the connection", ["tcp", "udp", "icmp"])

with col2:
    service = st.selectbox("Destination network service used.", ['http', 'private', 'domain_u', 'smtp', 'ftp_data', 'eco_i', 'other',
       'ecr_i', 'telnet', 'finger'])
    
protocoltype = st.selectbox("Protocol used in the connection", ["tcp", "udp", "icmp"])
service = st.selectbox("Destination network service used.", ['http', 'private', 'domain_u', 'smtp', 'ftp_data', 'eco_i', 'other',
       'ecr_i', 'telnet', 'finger'])

srcbytes = st.number_input("Number of data bytes transferred from source to destination", min_value = 0)
dstbytes = st.number_input("Number of data bytes transferred from destination to source", min_value = 0)
numcompromised = st.slider(" Number of 'compromised' conditions", min_value = 0, max_value = 7479)
count = st.slider("Number of connections to the same destination host as the current connection in the past 2 seconds.", min_value = 0, max_value = 511)
srvcount = st.slider("Number of connections to the same service as the current connection in the past two seconds.", min_value = 0, max_value = 511)
lastflag = st.slider("How many times has the connection been flagged", min_value = 0, max_value = 21)
dsthostserrorrate = st.slider("Destination host server error rate:", min_value = 0.0, max_value = 1.0, step = 0.01)
loggedin = st.radio("Login Status:", options=["Logged out", "Logged in"], index="Logged out")
diffsrvrate = st.slider("Percentage of connections that were to different services, among the connections aggregated in count:", min_value = 0.0, max_value = 1.0, step = 0.01)

# Convert user input into a DataFrame for the model
user_input = pd.DataFrame({
    "protocoltype": [protocoltype],
    "service": [service],
    "srcbytes": [srcbytes],
    "dstbytes": [dstbytes],
    "numcompromised": [numcompromised],
    "count": [count],
    "srvcount": [srvcount],
    "lastflag": [lastflag],
    "dsthostserrorrate": [dsthostserrorrate],
    "loggedin": [loggedin],
    "diffsrvrate": [diffsrvrate]
})

