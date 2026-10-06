import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Dubai Property Valuation",
    page_icon=None,
    layout="centered"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("models/dubai_property_model.joblib")


model = load_model()


# ============================================================
# DUBAI AREAS
# ============================================================

areas = [
    "Al Barshaa South Third",
    "Al Hebiah Second",
    "Al Hebiah Fourth",
    "Al Merkadh",
    "Al Safouh Second",
    "Al Wasl",
    "Bukadra",
    "Hadaeq Sheikh Mohammed Bin Rashid",
    "Marsa Dubai",
    "Palm Jumeirah",
    "Trade Center Second",
    "Wadi Al Safa 6",
    "Wadi Al Safa 7",
    "Zaabeel First",
    "Zaabeel Second"
]


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #f7f8fc;
}

.block-container {
    max-width: 900px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}


/* HEADER */

.hero {
    background: linear-gradient(
        120deg,
        #A00635 0%,
        #D01667 50%,
        #7619A6 100%
    );

    padding: 42px;
    border-radius: 20px;
    margin-bottom: 35px;

    box-shadow:
        0 15px 35px rgba(93, 16, 92, 0.15);
}

.hero-small {
    color: rgba(255,255,255,0.80);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.hero-title {
    color: #ffffff;
    font-size: 38px;
    line-height: 1.2;
    font-weight: 750;
    margin-bottom: 12px;
}

.hero-text {
    color: rgba(255,255,255,0.88);
    font-size: 15px;
    line-height: 1.6;
}


/* INPUT LABELS */

label {
    font-weight: 600 !important;
    color: #344054 !important;
}


/* BUTTON */

div.stButton > button {
    min-height: 52px;

    background: linear-gradient(
        90deg,
        #A00635,
        #D01667,
        #7619A6
    );

    color: white !important;

    border: none;
    border-radius: 10px;

    padding-left: 28px;
    padding-right: 28px;

    font-size: 16px;
    font-weight: 650;

    margin-top: 16px;

    box-shadow:
        0 7px 18px rgba(160, 6, 53, 0.18);

    transition: 0.2s;
}

div.stButton > button:hover {
    color: white !important;
    border: none !important;
    transform: translateY(-1px);
    box-shadow:
        0 9px 22px rgba(160, 6, 53, 0.25);
}

div.stButton > button:focus {
    color: white !important;
}


/* RESULT */

.result-card {
    background: linear-gradient(
        120deg,
        #A00635 0%,
        #D01667 50%,
        #7619A6 100%
    );

    padding: 38px;
    border-radius: 20px;
    margin-top: 30px;

    box-shadow:
        0 15px 35px rgba(93, 16, 92, 0.15);
}

.result-label {
    color: rgba(255,255,255,0.80);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

.result-price {
    color: white;
    font-size: 44px;
    line-height: 1.2;
    font-weight: 750;
    margin-top: 8px;
}

.year-badge {
    display: inline-block;

    background: rgba(255,255,255,0.17);
    border: 1px solid rgba(255,255,255,0.35);

    color: white;

    padding: 7px 13px;
    border-radius: 50px;

    font-size: 12px;
    font-weight: 650;

    margin-top: 14px;
}

.result-description {
    color: rgba(255,255,255,0.82);
    font-size: 13px;
    margin-top: 14px;
}


/* DETAIL CARDS */

.info-card {
    background: white;

    border: 1px solid #e5e7eb;

    padding: 20px;
    border-radius: 13px;

    margin-top: 12px;

    min-height: 95px;
}

.info-label {
    color: #667085;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.8px;
}

.info-value {
    color: #101828;
    font-size: 15px;
    font-weight: 650;
    margin-top: 7px;
}


/* DISCLAIMER */

.disclaimer {
    color: #667085;
    font-size: 12px;
    line-height: 1.6;
    margin-top: 5px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="hero">'
    '<div class="hero-small">UAE REAL ESTATE ANALYTICS</div>'
    '<div class="hero-title">Dubai Property Valuation</div>'
    '<div class="hero-text">'
    'Machine-learning valuation based on historical Dubai '
    'residential property transactions.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# INPUT FORM
# ============================================================

area = st.selectbox(
    "Location",
    areas,
    index=areas.index("Marsa Dubai")
)


col1, col2 = st.columns(2)


with col1:

    property_type = st.selectbox(
        "Property Type",
        ["Unit", "Villa"]
    )


with col2:

    bedroom_label = st.selectbox(
        "Bedrooms",
        [
            "Studio",
            "1 Bedroom",
            "2 Bedrooms",
            "3 Bedrooms",
            "4 Bedrooms",
            "5 Bedrooms",
            "6 Bedrooms",
            "7 Bedrooms"
        ],
        index=2
    )


bedroom_mapping = {
    "Studio": 0,
    "1 Bedroom": 1,
    "2 Bedrooms": 2,
    "3 Bedrooms": 3,
    "4 Bedrooms": 4,
    "5 Bedrooms": 5,
    "6 Bedrooms": 6,
    "7 Bedrooms": 7
}


bedrooms = bedroom_mapping[bedroom_label]


col3, col4 = st.columns(2)


with col3:

    size = st.number_input(
        "Property Size (sqm)",
        min_value=10.0,
        max_value=5000.0,
        value=120.0,
        step=5.0
    )


with col4:

    parking_label = st.selectbox(
        "Parking",
        ["Yes", "No"]
    )


parking = 1 if parking_label == "Yes" else 0


# ============================================================
# PREDICTION
# ============================================================

if st.button("Calculate Valuation"):

    property_input = pd.DataFrame({
        "area": [area],
        "property_type": [property_type],
        "bedrooms": [bedrooms],
        "area_sqm": [size],
        "has_parking": [parking],
        "year": [2026],
        "quarter": [4]
    })


    predicted_price = model.predict(property_input)[0]

    price_per_sqm = predicted_price / size


    # --------------------------------------------------------
    # RESULT CARD
    # --------------------------------------------------------

    result_html = (
        '<div class="result-card">'
        '<div class="result-label">'
        'ESTIMATED PROPERTY VALUE'
        '</div>'
        '<div class="result-price">'
        f'AED {predicted_price:,.0f}'
        '</div>'
        '<div class="year-badge">'
        '2026 Valuation'
        '</div>'
        '<div class="result-description">'
        'Model-based estimate using historical Dubai '
        'residential transactions'
        '</div>'
        '</div>'
    )

    st.markdown(
        result_html,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # PROPERTY DETAILS
    # --------------------------------------------------------

    c1, c2, c3 = st.columns(3)


    with c1:

        st.markdown(
            '<div class="info-card">'
            '<div class="info-label">LOCATION</div>'
            f'<div class="info-value">{area}</div>'
            '</div>',
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            '<div class="info-card">'
            '<div class="info-label">PROPERTY</div>'
            f'<div class="info-value">'
            f'{property_type} · {bedroom_label}'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    with c3:

        st.markdown(
            '<div class="info-card">'
            '<div class="info-label">'
            'ESTIMATED AED / SQM'
            '</div>'
            f'<div class="info-value">'
            f'AED {price_per_sqm:,.0f}'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    st.caption(
        f"Property Size: {size:,.0f} sqm   |   "
        f"Parking: {parking_label}"
    )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="disclaimer">'
    'Portfolio project. Estimates are generated by a '
    'machine-learning model trained on historical Dubai '
    'residential transaction data and should not be considered '
    'professional property valuations.'
    '</div>',
    unsafe_allow_html=True
)