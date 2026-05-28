import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# Set the page configuration and title
st.set_page_config(
    page_title="XYZ Finance: Credit Risk Modelling",
    page_icon="📊",
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

/* Container styling for inputs and layout */
.main-header {
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.05) 0%, rgba(99, 102, 241, 0.02) 100%);
    border: 1px solid rgba(79, 70, 229, 0.12);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 28px;
}

/* Card styling for results */
.result-container {
    background: rgba(255, 255, 255, 0.85) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid rgba(15, 23, 42, 0.08) !important;
    border-radius: 24px;
    padding: 32px;
    margin-top: 32px;
    box-shadow: 0 15px 35px rgba(15, 23, 42, 0.05) !important;
    animation: fadeIn 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.metrics-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-top: 20px;
}

@media (max-width: 768px) {
    .metrics-grid {
        grid-template-columns: 1fr;
    }
}

.metric-card {
    background: rgba(255, 255, 255, 0.95) !important;
    border: 1px solid rgba(15, 23, 42, 0.05) !important;
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.01) !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    text-align: center;
}

.metric-card:hover {
    transform: translateY(-4px);
    border-color: rgba(79, 70, 229, 0.15) !important;
    box-shadow: 0 8px 25px rgba(79, 70, 229, 0.08) !important;
}

.metric-title {
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #475569 !important;
    margin-bottom: 12px;
    font-weight: 600;
}

.metric-value {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 16px;
    line-height: 1.1;
    letter-spacing: -0.5px;
    color: #0f172a !important;
}

.metric-badge {
    display: inline-block;
    padding: 8px 20px;
    font-size: 13px;
    font-weight: 700;
    border-radius: 50px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Progress bar container */
.progress-container {
    width: 80%;
    margin: 14px auto 0 auto;
    background-color: rgba(15, 23, 42, 0.06);
    border-radius: 12px;
    height: 12px;
    overflow: hidden;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
}

.progress-fill {
    height: 100%;
    border-radius: 12px;
    transition: width 1s ease-in-out;
}

/* Rating-specific color schemas - Optimized for Light Background Readability */
.excellent {
    color: #059669 !important;
}
.excellent-badge {
    background-color: rgba(16, 185, 129, 0.1);
    color: #059669 !important;
    border: 1px solid rgba(16, 185, 129, 0.25);
}
.excellent-bg {
    background: linear-gradient(90deg, #10b981 0%, #059669 100%);
    box-shadow: 0 0 10px rgba(16, 185, 129, 0.15);
}

.good {
    color: #1d4ed8 !important;
}
.good-badge {
    background-color: rgba(59, 130, 246, 0.1);
    color: #1d4ed8 !important;
    border: 1px solid rgba(59, 130, 246, 0.25);
}
.good-bg {
    background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
    box-shadow: 0 0 10px rgba(59, 130, 246, 0.15);
}

.average {
    color: #b45309 !important;
}
.average-badge {
    background-color: rgba(245, 158, 11, 0.1);
    color: #b45309 !important;
    border: 1px solid rgba(245, 158, 11, 0.25);
}
.average-bg {
    background: linear-gradient(90deg, #f59e0b 0%, #d97706 100%);
    box-shadow: 0 0 10px rgba(245, 158, 11, 0.15);
}

.poor {
    color: #b91c1c !important;
}
.poor-badge {
    background-color: rgba(239, 68, 68, 0.1);
    color: #b91c1c !important;
    border: 1px solid rgba(239, 68, 68, 0.25);
}
.poor-bg {
    background: linear-gradient(90deg, #ef4444 0%, #dc2626 100%);
    box-shadow: 0 0 10px rgba(239, 68, 68, 0.15);
}

/* Style streamlit input fields for pristine light theme aesthetic */
.stNumberInput input, .stSelectbox select {
    background-color: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    color: #0f172a !important;
    border-radius: 10px !important;
}

/* Make st.metric labels and values dark and highly readable on Light Background */
[data-testid="stMetricLabel"], [data-testid="stMetricLabel"] > div {
    color: #475569 !important; /* Slate-600 */
    font-size: 14px !important;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"], [data-testid="stMetricValue"] > div {
    color: #0f172a !important; /* Slate-900 */
    font-size: 32px !important;
    font-weight: 700 !important;
}

/* Ensure widget input labels are clean and highly visible */
[data-testid="stWidgetLabel"] p {
    color: #334155 !important; /* Slate-700 */
    font-weight: 600 !important;
}

/* Premium Calculate Risk Button Styling */
div.stButton > button {
    background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%) !important;
    color: white !important;
    border: none !important;
    padding: 14px 28px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    border-radius: 12px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 15px rgba(79, 70, 229, 0.2) !important;
    width: 100% !important;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 24px;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
    box-shadow: 0 8px 25px rgba(79, 70, 229, 0.3) !important;
    transform: translateY(-2px) !important;
}

div.stButton > button:active {
    transform: translateY(0px) !important;
}
</style>
""", unsafe_allow_html=True)

# Main Title and Header Section - Light theme optimized texts
st.markdown("""
<div class="main-header">
    <h1 style="margin: 0; color: #0F172A; font-size: 32px; font-weight: 700; display: flex; align-items: center; gap: 12px;">
        📊 XYZ Finance: Credit Risk Modelling
    </h1>
    <p style="margin: 8px 0 0 0; color: #475569; font-size: 16px;">
        State-of-the-art predictive analytics suite for real-time assessment of loan default probabilities and customer creditworthiness.
    </p>
</div>
""", unsafe_allow_html=True)

# Create rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the first row with default values
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    income = st.number_input('Income', min_value=0, value=1200000)
with row1[2]:
    loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000)

# Calculate Loan to Income Ratio and display it using a polished st.metric
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.metric(label="Loan to Income Ratio", value=f"{loan_to_income_ratio:.2f}")

# Assign inputs to the remaining controls
with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)

with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

# Button to calculate risk
if st.button('Calculate Risk'):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    # Determine CSS styling class matching the credit rating
    rating_classes = {
        'Excellent': 'excellent',
        'Good': 'good',
        'Average': 'average',
        'Poor': 'poor'
    }
    rating_class = rating_classes.get(rating, 'average')

    # Display results as gorgeous custom-styled metric cards optimized for high-readability
    st.markdown(f"""
        <div class="result-container">
            <h3 style="margin-top: 0; color: #0F172A; font-weight: 700; font-size: 20px; text-transform: uppercase; letter-spacing: 1px;">
                Risk Assessment Summary
            </h3>
            <div class="metrics-grid">
                <div class="metric-card">
                    <div class="metric-title">Credit Score & Rating</div>
                    <div class="metric-value {rating_class}">{credit_score}</div>
                    <span class="metric-badge {rating_class}-badge">{rating}</span>
                </div>
                <div class="metric-card">
                    <div class="metric-title">Default Probability</div>
                    <div class="metric-value {rating_class}">{probability:.2%}</div>
                    <div class="progress-container">
                        <div class="progress-fill {rating_class}-bg" style="width: {probability * 100:.1f}%;"></div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
