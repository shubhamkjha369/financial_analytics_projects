import streamlit as st
import textwrap
from prediction_helper import predict, calculate_normalized_risk

# Set the page configuration and title
st.set_page_config(
    page_title="XYZ Finance: Premium Cost Estimator",
    page_icon="🏥",
    layout="wide"
)

# Custom Styling for modern premium light-theme visual identity
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Inter:wght@300;400;600;700&display=swap');

/* Global Font Override */
html, body, [class*="css"], .stMarkdown {
    font-family: 'Inter', sans-serif !important;
}

h1, h2, h3, h4, h5, h6, .metric-value {
    font-family: 'Outfit', sans-serif !important;
}

/* Light background gradient for main content */
.stApp {
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%) !important;
    color: #0f172a !important;
}

/* Container styling for cards */
div[data-testid="stContainer"] {
    background-color: #ffffff !important;
    border: 1px solid rgba(148, 163, 184, 0.15) !important;
    border-radius: 16px !important;
    padding: 24px !important;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05) !important;
    margin-bottom: 24px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

div[data-testid="stContainer"]:hover {
    border-color: rgba(99, 102, 241, 0.3) !important;
    box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.05), 0 4px 6px -4px rgba(99, 102, 241, 0.05) !important;
}

.main-header {
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.05) 0%, rgba(124, 58, 237, 0.02) 100%);
    border: 1px solid rgba(79, 70, 229, 0.15);
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 32px;
}

/* Card styling for results */
.result-container {
    background: rgba(255, 255, 255, 0.95) !important;
    border: 1.5px solid rgba(79, 70, 229, 0.2) !important;
    border-radius: 24px;
    padding: 32px;
    margin-top: 32px;
    box-shadow: 0 20px 25px -5px rgba(79, 70, 229, 0.05), 0 10px 10px -5px rgba(79, 70, 229, 0.05) !important;
    animation: fadeIn 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
}

.metrics-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-top: 24px;
}

@media (max-width: 768px) {
    .metrics-grid {
        grid-template-columns: 1fr;
    }
}

.metric-card {
    background: #ffffff !important;
    border: 1px solid rgba(226, 232, 240, 0.8) !important;
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.02) !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    text-align: center;
}

.metric-card:hover {
    transform: translateY(-4px);
    border-color: rgba(99, 102, 241, 0.2) !important;
    box-shadow: 0 8px 30px rgba(99, 102, 241, 0.06) !important;
}

.metric-title {
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #64748b !important;
    margin-bottom: 8px;
    font-weight: 600;
}

.metric-value {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 12px;
    line-height: 1.1;
    color: #4f46e5 !important;
    text-shadow: 0 0 25px rgba(79, 70, 229, 0.1);
}

.metric-badge {
    display: inline-block;
    padding: 6px 16px;
    font-size: 12px;
    font-weight: 700;
    border-radius: 50px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.profile-badge {
    background-color: rgba(99, 102, 241, 0.08);
    color: #4f46e5 !important;
    border: 1px solid rgba(99, 102, 241, 0.2);
}

.success-badge {
    background-color: rgba(16, 185, 129, 0.08);
    color: #059669 !important;
    border: 1px solid rgba(16, 185, 129, 0.2);
}

/* Premium Primary Button Styling */
div.stButton > button {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
    color: white !important;
    border: none !important;
    padding: 14px 28px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    border-radius: 12px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 14px rgba(79, 70, 229, 0.25) !important;
    width: 100% !important;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 12px;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%) !important;
    box-shadow: 0 8px 24px rgba(79, 70, 229, 0.35) !important;
    transform: translateY(-2px) !important;
}

div.stButton > button:active {
    transform: translateY(0px) !important;
}
</style>
""", unsafe_allow_html=True)

# Main Title and Header Section
st.markdown("""
<div class="main-header">
    <h1 style="margin: 0; color: #0f172a; font-size: 32px; font-weight: 700; display: flex; align-items: center; gap: 12px;">
        🏥 XYZ Finance: Premium Cost Estimator
    </h1>
    <p style="margin: 8px 0 0 0; color: #475569; font-size: 15px; line-height: 1.5;">
        State-of-the-art predictive model engineered to dynamically calculate personalized annual health insurance costs. Utilizes custom segment-based analytics to identify lifestyle and health risk premiums with explainable attribution.
    </p>
</div>
""", unsafe_allow_html=True)

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# 3-Card layout to organize forms logically
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("<h3 style='margin-top:0; font-size:18px; color:#1e293b; font-weight:700; border-bottom: 2px solid #f1f5f9; padding-bottom: 8px; margin-bottom: 16px;'>👤 Demographics</h3>", unsafe_allow_html=True)
        age = st.number_input('Age', min_value=18, step=1, max_value=100, value=30)
        gender = st.selectbox('Gender', categorical_options['Gender'])
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
        region = st.selectbox('Region', categorical_options['Region'])

with col2:
    with st.container(border=True):
        st.markdown("<h3 style='margin-top:0; font-size:18px; color:#1e293b; font-weight:700; border-bottom: 2px solid #f1f5f9; padding-bottom: 8px; margin-bottom: 16px;'>🫁 Lifestyle & Health Risk</h3>", unsafe_allow_html=True)
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])
        genetical_risk = st.number_input('Genetical Risk Factor (0-5)', step=1, min_value=0, max_value=5, value=0)

with col3:
    with st.container(border=True):
        st.markdown("<h3 style='margin-top:0; font-size:18px; color:#1e293b; font-weight:700; border-bottom: 2px solid #f1f5f9; padding-bottom: 8px; margin-bottom: 16px;'>💼 Financials & Policy</h3>", unsafe_allow_html=True)
        income_lakhs = st.number_input('Income in Lakhs (Annual)', step=1, min_value=0, max_value=200, value=5)
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20, value=0)
        insurance_plan = st.selectbox('Insurance Plan Tier', categorical_options['Insurance Plan'])
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

# Create input dictionary
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Centered estimate button
st.markdown("<div style='margin-top: 10px; margin-bottom: 20px;'></div>", unsafe_allow_html=True)
if st.button('Estimate annual premium cost'):
    prediction = predict(input_dict)
    
    # Calculate exact medical risk factor for visualization
    normalized_risk = calculate_normalized_risk(medical_history)
    risk_percentage = int(normalized_risk * 100)
    
    # Model attribution description based on age
    if age <= 25:
        profile_tier = "Young Adult Policy"
        model_details = """<div style="background-color: rgba(79, 70, 229, 0.03); border: 1px solid rgba(79, 70, 229, 0.15); border-radius: 12px; padding: 16px; margin-top: 24px; font-size: 14px; color: #334155; line-height: 1.5;">
💡 <strong>Model Pipeline Attribution:</strong> This premium was evaluated under the <strong>Young Adult Cohort</strong> framework utilizing a regularized <strong>Linear Regression</strong> model (<code>model_young.joblib</code>). Linear equations prevent overfitting on the narrower young adult segment, ensuring stable, generalized, and highly transparent baseline calculations.
</div>"""
    else:
        profile_tier = "Standard Adult Policy"
        model_details = """<div style="background-color: rgba(124, 58, 237, 0.03); border: 1px solid rgba(124, 58, 237, 0.15); border-radius: 12px; padding: 16px; margin-top: 24px; font-size: 14px; color: #334155; line-height: 1.5;">
💡 <strong>Model Pipeline Attribution:</strong> This premium was evaluated under the <strong>Standard Adult Cohort</strong> framework utilizing an hyperparameter-tuned <strong>XGBoost Regressor</strong> (<code>model_rest.joblib</code>). Tree-boosting models are highly robust and capture the complex, non-linear risk boundaries, income interactions, and plan tier parameters present in this segment.
</div>"""
        
    # Render premium glassmorphic result container
    st.markdown(f"""<div class="result-container">
<h3 style="margin-top: 0; color: #0f172a; font-weight: 700; font-size: 20px; text-transform: uppercase; letter-spacing: 1.5px; border-bottom: 2px dashed rgba(79, 70, 229, 0.15); padding-bottom: 12px;">
    📊 Customized Premium Calculation Report
</h3>

<div class="metrics-grid">
    <div class="metric-card">
        <div class="metric-title">Estimated Annual Premium</div>
        <div class="metric-value">₹{prediction:,}</div>
        <span class="metric-badge success-badge">Pristine Calculation</span>
    </div>
    <div class="metric-card">
        <div class="metric-title">Risk Profile Policy Tier</div>
        <div style="font-size: 28px; font-weight: 700; color: #0f172a; margin: 12px 0 16px 0;">{profile_tier}</div>
        <span class="metric-badge profile-badge">Age Cohort: { "≤ 25" if age <= 25 else "> 25" }</span>
    </div>
</div>

<div style="margin-top: 28px; background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 20px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <span style="font-size: 14px; font-weight: 700; color: #334155;">🩺 Medical History Co-morbidity Index</span>
        <span style="font-size: 14px; font-weight: 700; color: { '#10b981' if risk_percentage < 30 else '#f59e0b' if risk_percentage < 60 else '#ef4444' };">{risk_percentage}% Risk</span>
    </div>
    <div style="background-color: #f1f5f9; border-radius: 9999px; height: 10px; width: 100%; overflow: hidden;">
        <div style="background: linear-gradient(90deg, #10b981 0%, { '#f59e0b' if risk_percentage >= 50 else '#10b981' } 50%, { '#ef4444' if risk_percentage >= 80 else '#f59e0b' } 100%); height: 100%; width: {max(risk_percentage, 4)}%; border-radius: 9999px; transition: width 0.8s ease-in-out;"></div>
    </div>
    <p style="margin: 8px 0 0 0; font-size: 12px; color: #64748b; line-height: 1.4;">
        *Comorbidity index is calculated based on cumulative severity weights assigned to chronic indicators in your Medical History. (Higher risk score scales insurance pricing symmetrically to cover tail exposure).
    </p>
</div>

{model_details}
</div>""", unsafe_allow_html=True)
