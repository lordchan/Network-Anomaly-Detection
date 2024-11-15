# Importing required libraries
import streamlit as st
import pandas as pd
from xgboost import XGBClassifier
import requests
import pickle
from io import BytesIO

st.title("My Project Dashboard")

# Sidebar Content
st.sidebar.title("Project Index")

# Project description
st.sidebar.subheader("About This Project")
st.sidebar.write("This project is designed to [briefly explain your project here].")

# Links
st.sidebar.subheader("Useful Links")
st.sidebar.markdown("[Complete GitHub code](https://github.com/lordchan/Network-Anomaly-Detection)", unsafe_allow_html=True)
st.sidebar.markdown("[Medium Blog](https://medium.com/@chinni030899/network-anomaly-detection-using-xgboost-an-end-to-end-project-836e87369833)", unsafe_allow_html=True)
st.sidebar.markdown("[Connect on LinkedIn](https://www.linkedin.com/in/chanakya-gadwal/)", unsafe_allow_html=True)


# Loading the model from GitHub
@st.cache_data
def load_model_from_github():
    url = "https://github.com/lordchan/Network-Anomaly-Detection/blob/main/xgboost_model.pkl?raw=true"  # Replace with your model's GitHub URL
    response = requests.get(url)
    response.raise_for_status()  # This will raise an error if the file is not accessible
    model = pickle.loads(response.content)
    return model

# Loading the categoric encoding table from GitHub
@st.cache_data
def load_encoder_from_github():
    url = "https://github.com/lordchan/Network-Anomaly-Detection/blob/main/target_enc.pkl?raw=true"  # Replace with your model's GitHub URL
    response = requests.get(url)
    response.raise_for_status()  # This will raise an error if the file is not accessible
    enc = pickle.loads(response.content)
    return enc

# Load the model and enc
model = load_model_from_github()
enc = load_encoder_from_github()

# Streamlit UI
st.title("🤖 Network Anomaly Detection using XGBoost")
st.write("Enter the details of your network and predict the chances of getting attacked with 99% accuracy!")
# Define the input fields
# Adjust these according to the model's features

protocoltype = st.radio("Protocol used in the connection:", options=["tcp", "udp", "icmp"], index=0)
service = st.selectbox("Destination network service used.", ['http', 'private', 'domain_u', 'smtp', 'ftp_data', 'eco_i', 'other',
       'ecr_i', 'telnet', 'finger'])
srcbytes = st.number_input("Number of data bytes transferred from source to destination", min_value = 0)
dstbytes = st.number_input("Number of data bytes transferred from destination to source", min_value = 0)

numcompromised = st.slider(" Number of 'compromised' conditions", min_value = 0, max_value = 7479)
count = st.slider("Number of connections to the same destination host as the current connection in the past 2 seconds.", min_value = 0, max_value = 511)
srvcount = st.slider("Number of connections to the same service as the current connection in the past two seconds.", min_value = 0, max_value = 511)
lastflag = st.slider("How many times has the connection been flagged", min_value = 0, max_value = 21)
dsthostserrorrate = st.slider("Destination host server error rate:", min_value = 0.0, max_value = 1.0, step = 0.01)
loggedin = st.radio("Login Status:", options=["Logged out", "Logged in"], index=0)
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
    "loggedin": [1 if loggedin=="Logged in" else 0],
    "diffsrvrate": [diffsrvrate]
})

def transform_(test):
    test['proto_service'] = test[['protocoltype', 'service']].apply(lambda x: x[0] + x[1], axis = 1)
    test['diffsrvcount_'] = test['diffsrvrate']*test['count']
    test = test.merge(enc, how = 'left', left_on = 'proto_service', right_on = 'proto_service').drop(columns = 'proto_service').rename(columns = {'attack?': 'proto_service'})
    test.drop(columns = ['protocoltype', 'service', 'diffsrvrate'], inplace = True)
    return test

if st.button("Predict"):
    # Perform prediction
    prediction = model.predict(transform_(user_input))[0] 
    
    if prediction == 1:
        st.error("😱 Network is under attack! Beware")
    else:
        st.success("No attack, you are safe 😌")
