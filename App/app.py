import streamlit as st
import pandas as pd
import joblib

# ---------------------------
# Load Model
# ---------------------------
try:
    model = joblib.load("purchase_prediction_model.pkl")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.set_page_config(
    page_title="Online Shopper Purchase Prediction",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Online Shopper Purchase Prediction")
st.markdown("""
Predict whether an online visitor is likely to complete a purchase based on browsing behavior using a trained Random Forest model.

**Model:** Random Forest Classifier  
**Dataset:** Online Shoppers Purchasing Intention Dataset
""")
st.write("Predict whether a website visitor is likely to make a purchase.")

st.sidebar.subheader("📄 Page Activity")
# Administrative
# Informational
# Product Related

st.sidebar.subheader("📈 Engagement")
# Bounce Rate
# Exit Rate
# Page Value

st.sidebar.subheader("🌍 Visitor Information")
# Browser
# Region
# Month
# Visitor Type
# Numerical Inputs


Administrative = st.sidebar.number_input("Administrative Pages", min_value=0)
Administrative_Duration = st.sidebar.number_input("Administrative Duration", min_value=0.0)

Informational = st.sidebar.number_input("Informational Pages", min_value=0)
Informational_Duration = st.sidebar.number_input("Informational Duration", min_value=0.0)

ProductRelated = st.sidebar.number_input("Product Related Pages", min_value=0)
ProductRelated_Duration = st.sidebar.number_input("Product Related Duration", min_value=0.0)

BounceRates = st.sidebar.number_input("Bounce Rate", min_value=0.0, format="%.4f")
ExitRates = st.sidebar.number_input("Exit Rate", min_value=0.0, format="%.4f")

PageValues = st.sidebar.number_input("Page Value", min_value=0.0)
SpecialDay = st.sidebar.slider("Special Day", 0.0, 1.0)

OperatingSystems = st.sidebar.number_input("Operating System", min_value=1)
Browser = st.sidebar.number_input("Browser", min_value=1)
Region = st.sidebar.number_input("Region", min_value=1)
TrafficType = st.sidebar.number_input("Traffic Type", min_value=1)

Weekend = st.sidebar.selectbox(
    "Weekend",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

Month = st.sidebar.selectbox(
    "Month",
    ["Dec","Feb","Jul","June","Mar","May","Nov","Oct","Sep"]
)

VisitorType = st.sidebar.selectbox(
    "Visitor Type",
    ["Returning_Visitor","Other"]
)

# ---------------------------
# Create Input DataFrame
# ---------------------------

data = {
    'Administrative':[Administrative],
    'Administrative_Duration':[Administrative_Duration],
    'Informational':[Informational],
    'Informational_Duration':[Informational_Duration],
    'ProductRelated':[ProductRelated],
    'ProductRelated_Duration':[ProductRelated_Duration],
    'BounceRates':[BounceRates],
    'ExitRates':[ExitRates],
    'PageValues':[PageValues],
    'SpecialDay':[SpecialDay],
    'OperatingSystems':[OperatingSystems],
    'Browser':[Browser],
    'Region':[Region],
    'TrafficType':[TrafficType],
    'Weekend':[Weekend],

    'Month_Dec':[0],
    'Month_Feb':[0],
    'Month_Jul':[0],
    'Month_June':[0],
    'Month_Mar':[0],
    'Month_May':[0],
    'Month_Nov':[0],
    'Month_Oct':[0],
    'Month_Sep':[0],

    'VisitorType_Other':[0],
    'VisitorType_Returning_Visitor':[0]
}

if Month == "Dec":
    data["Month_Dec"]=[1]
elif Month=="Feb":
    data["Month_Feb"]=[1]
elif Month=="Jul":
    data["Month_Jul"]=[1]
elif Month=="June":
    data["Month_June"]=[1]
elif Month=="Mar":
    data["Month_Mar"]=[1]
elif Month=="May":
    data["Month_May"]=[1]
elif Month=="Nov":
    data["Month_Nov"]=[1]
elif Month=="Oct":
    data["Month_Oct"]=[1]
elif Month=="Sep":
    data["Month_Sep"]=[1]

if VisitorType=="Other":
    data["VisitorType_Other"]=[1]
else:
    data["VisitorType_Returning_Visitor"]=[1]

input_df = pd.DataFrame(data)

        # ---------------------------
# Match Feature Order
# ---------------------------

feature_order = [
    'Administrative',
    'Administrative_Duration',
    'Informational',
    'Informational_Duration',
    'ProductRelated',
    'ProductRelated_Duration',
    'BounceRates',
    'ExitRates',
    'PageValues',
    'SpecialDay',
    'OperatingSystems',
    'Browser',
    'Region',
    'TrafficType',
    'Weekend',
    'Month_Dec',
    'Month_Feb',
    'Month_Jul',
    'Month_June',
    'Month_Mar',
    'Month_May',
    'Month_Nov',
    'Month_Oct',
    'Month_Sep',
    'VisitorType_Other',
    'VisitorType_Returning_Visitor'
]

input_df = input_df[feature_order]
   with st.expander("📋 View Processed Input"):

        st.dataframe(
            input_df,
            use_container_width=True
        )


# ---------------------------
# Prediction
# ---------------------------

if st.button("🔮 Predict Purchase"):

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Prediction")

        if prediction == 1:
            st.success("✅ Customer is likely to make a purchase.")
        else:
            st.error("❌ Customer is unlikely to make a purchase.")

    with col2:

        st.subheader("Purchase Probability")

        st.metric(
    "Purchase Probability",
    f"{probability:.1%}"
)

    st.progress(float(probability))

    if probability >= 0.80:
        st.success("🟢 High Purchase Intent")
    elif probability >= 0.50:
        st.warning("🟡 Moderate Purchase Intent")
    else:
        st.error("🔴 Low Purchase Intent")

    st.markdown("---")

    st.subheader("Input Summary")

 
