# Network Anomaly Detection

## Problem Statement
In the field of cybersecurity, network anomaly detection is crucial for identifying unusual patterns or behaviors in network traffic that may indicate security threats, including compromised devices, malware infections, and large-scale cyber-attacks like DDoS (Distributed Denial of Service). Traditional rule-based detection methods often fall short, as they struggle to detect new or evolving threats and become increasingly complex to maintain as network environments grow. This project presents a dynamic approach to network anomaly detection through data analytics, machine learning, and visualization for real-time, accurate anomaly detection.

## Motivation
### Why Network Anomaly Detection Matters
1. **Evolving Security Threats**: Cyber threats are constantly evolving, requiring adaptive detection systems.
2. **Growing Network Complexity**: Modern networks consist of diverse devices and applications, challenging traditional anomaly detection methods.
3. **Operational Continuity**: Quick anomaly detection helps prevent disruptions in service.
4. **Regulatory Compliance**: Anomaly detection helps organizations meet stringent data security and privacy standards.

## Important Links
[Medium Blog](https://medium.com/@chinni030899/network-anomaly-detection-using-xgboost-an-end-to-end-project-836e87369833)
[Interact realtime with the model on Streamlit](https://app-xgb-prediction.streamlit.app/)
[Tableau Dashboard](https://public.tableau.com/app/profile/chanakya.g.r/viz/ProjectScaler/Dashboard1)

---

## Project Overview

### Block 1: Tableau Visualizations
This project features a Tableau dashboard to visualize network traffic and enable cybersecurity professionals to monitor, analyze, and detect anomalies.

#### Suggested Dashboard Components
- **Traffic Volume Over Time**: Line or area charts to detect unusual spikes or drops in traffic.
- **Anomaly Detection Metrics**: Visuals for metrics like `Wrong_fragment`, `Urgent`, and `Num_failed_logins` to highlight potential security issues.
- **Protocol and Service Analysis**: Pie/bar charts for `Protocol_type` and `Service` to detect frequently targeted protocols or services.
- **Connection Status Overview**: Heatmaps or bar charts of `Flag` status for a quick overview of connection health.
- **Geographical Insights**: Mapping IP geolocation data to identify anomaly sources by region.
- **Host-based Traffic Features**: Visualize features like `Dst_host_count` and `Dst_host_srv_count` to detect targeted hosts.
- **Interactive Filters**: Enable filtering by time, protocol, and service for focused analysis.
- **Correlation Analysis**: Scatter plots or matrices to explore relationships in features like `Src_bytes`, `Dst_bytes`, and `Duration`.
- **Alerts and Anomalies Log**: List recent anomalies for easy review.
- **Predictive Insights**: Forecast future anomalies based on historical and current trends.

---

### Block 2: EDA and Hypothesis Testing
Exploratory Data Analysis (EDA) and hypothesis testing reveal patterns in the data and validate assumptions, aiding in accurate anomaly detection.

#### Suggested EDA Steps
- **Feature Distribution Analysis**: Analyze the distribution of each feature.
- **Correlation Analysis**: Identify relationships among features.
- **Outlier Detection**: Flag unusual data points.
- **Time Series Analysis**: Detect time-dependent patterns in network traffic.
- **Feature Engineering**: Create features to improve prediction accuracy.
- **Missing Values Analysis**: Handle missing data.

#### Hypotheses for Testing
- **Network Traffic Volume and Anomalies**: Test if unusual traffic volumes are associated with anomalies.
- **Impact of Protocol Type**: Assess whether certain protocols are more prone to anomalies.
- **Service Targeting in Anomalies**: Identify if specific services are more frequently targeted.
- **Connection Status**: Analyze if error flags correlate with anomalies.
- **Urgent Packet Influence**: Determine if urgent packets signal anomalies.

---

### Block 3: ML Modeling
1. **Data Processing**
   - **Data Cleaning**: Handle missing values, duplicates, and errors.
   - **Feature Engineering**: Create new features to boost performance.
   - **Data Transformation**: Scale and normalize data where needed.
   - **Train-Test Split**: Split data to evaluate model on unseen samples.

2. **Model Selection**
   - **Supervised Learning Models**: Classification models such as logistic regression, decision trees, random forests, SVM, and neural networks.
   - **Ensemble Techniques**: Boosting, bagging, and stacking for improved accuracy and reduced overfitting.
   - **Unsupervised Learning Models**: Clustering models (K-means, DBSCAN) and dimensionality reduction (PCA, t-SNE) for anomaly detection without labels.

3. **Model Evaluation and Validation**
   - **Cross-Validation**: k-fold validation for robust performance assessment.
   - **Performance Metrics**: Accuracy, precision, recall, F1-score, and ROC-AUC for classification; silhouette score or reconstruction error for clustering.
   - **Confusion Matrix**: Understand true/false positives and negatives.
   - **Adjustment and Tuning**: Refine model through hyperparameter tuning and optimization.

**Model Performance**: The final model achieved accuracy, precision, recall, and F1-score greater than 99% on test data, effectively balancing predictive performance without overfitting.

---

### Block 4: Deployment
Deploying the model via a Flask API allows for real-time anomaly detection and accessibility across different applications.

#### Deployment Steps
1. **Flask API Setup**
   - Create a Python environment and install necessary libraries.
   - Set up Flask with routes for prediction.

2. **Model Integration**
   - Serialize and load the model for fast predictions.

3. **API Endpoints**
   - Define a POST route for users to submit network data in JSON format.
   - Preprocess incoming data for model compatibility.
   - Generate predictions and return results.

This setup enables seamless integration with network monitoring tools and other applications.

---

## Project Highlights
This project uses a data-centric approach, combining EDA, feature engineering, and machine learning to detect network anomalies. Through comprehensive visualization, we provide actionable insights into network traffic patterns. Model performance reached over 99% in accuracy, recall, precision, and F1-score on test data, with no signs of overfitting.
