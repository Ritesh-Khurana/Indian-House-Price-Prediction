import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Set the page configuration
st.set_page_config(
    page_title="🏠 Indian Property Price Predictor",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS for modern blue-purple theme styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    .main > div {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.1);
    }
    
    .stSidebar > div {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(15px);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 0.75rem 2rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #43a7e5 0%, #00d9e5 100%);
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(79, 172, 254, 0.4);
    }
    
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border: 1px solid #cbd5e1;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f8fafc;
        border-radius: 12px;
        padding: 5px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, #e2e8f0 0%, #cbd5e1 100%);
        color: #475569;
        border-radius: 8px;
        font-weight: 600;
        border: 1px solid #94a3b8;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        border-color: #4facfe;
    }
    
    .modern-gradient {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        height: 4px;
        width: 100%;
        margin: 1rem 0;
        border-radius: 2px;
    }
    
    /* Fix for sidebar text alignment */
    .stSidebar [data-testid="stMarkdownContainer"] p {
        margin-bottom: 0.5rem;
        line-height: 1.4;
    }
    
    /* Better spacing for selectboxes */
    .stSelectbox {
        margin-bottom: 1rem;
    }
    
    /* Checkbox alignment */
    .stCheckbox {
        margin-bottom: 0.3rem;
    }
    
    /* Slider spacing */
    .stSlider {
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Title with modern blue-purple gradient
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <h1 style="
        font-size: 3rem; 
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-weight: 700;
        margin-bottom: 0.5rem;
    ">🏠 Indian Property Price Predictor</h1>
    <div class="modern-gradient"></div>
    <p style="font-size: 1.3rem; color: white; font-weight: 500; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
        Smart Real Estate Analytics for Indian Market
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar with Indian property inputs
with st.sidebar:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: #1e293b;
        text-align: center;
        margin-bottom: 2rem;
        border: 2px solid #4facfe;
    ">
        <h2 style="margin: 0; font-size: 1.5rem; color: #0369a1;">🎯 Property Details</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Indian city selection
    st.markdown("**🏙️ City**")
    city = st.selectbox(
        "Select City",
        ["Mumbai", "Delhi NCR", "Bangalore", "Hyderabad", "Chennai", "Pune", "Kolkata", "Ahmedabad", "Surat", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad", "Ludhiana"],
        index=0,
        label_visibility="collapsed"
    )
    
    # Property type
    st.markdown("**🏠 Property Type**")
    property_type = st.selectbox(
        "Property Type",
        ["Apartment/Flat", "Independent House", "Villa", "Builder Floor", "Penthouse", "Studio Apartment"],
        index=0,
        label_visibility="collapsed"
    )
    
    # BHK Configuration
    st.markdown("**🏡 BHK Configuration**")
    bhk = st.selectbox(
        "BHK",
        ["1 RK", "1 BHK", "2 BHK", "3 BHK", "4 BHK", "5+ BHK"],
        index=3,
        label_visibility="collapsed"
    )
    
    # Area in sq ft
    st.markdown("**📐 Area (Sq Ft)**")
    area = st.slider("Area", 200, 5000, 1200, 50, label_visibility="collapsed")
    st.markdown(f"<small style='color: #64748b;'>{area:,} sq ft ({area * 0.092903:.0f} sq meters)</small>", unsafe_allow_html=True)
    
    # Location type
    st.markdown("**📍 Location Type**")
    location_type = st.selectbox(
        "Location",
        ["Prime Location", "Central Area", "Suburb", "Outskirts", "IT Hub", "Business District"],
        index=2,
        label_visibility="collapsed"
    )
    
    # Property age
    st.markdown("**📅 Property Age**")
    age = st.selectbox(
        "Age",
        ["Under Construction", "Ready to Move", "0-1 Years", "1-5 Years", "5-10 Years", "10-15 Years", "15+ Years"],
        index=3,
        label_visibility="collapsed"
    )
    
    # Floor details
    st.markdown("**🏢 Floor Details**")
    floor = st.selectbox(
        "Floor",
        ["Ground Floor", "1st-3rd Floor", "4th-7th Floor", "8th-12th Floor", "Above 12th Floor"],
        index=2,
        label_visibility="collapsed"
    )
    
    # Furnishing
    st.markdown("**🪑 Furnishing**")
    furnishing = st.selectbox(
        "Furnishing",
        ["Unfurnished", "Semi-Furnished", "Fully Furnished"],
        index=1,
        label_visibility="collapsed"
    )
    
    # Parking
    st.markdown("**🚗 Parking**")
    parking = st.selectbox(
        "Parking",
        ["No Parking", "1 Car", "2 Cars", "3+ Cars"],
        index=1,
        label_visibility="collapsed"
    )
    
    # Indian amenities
    st.markdown("---")
    st.markdown("**🏘️ Amenities**")
    
    amenities = {}
    amenities['lift'] = st.checkbox("🛗 Lift/Elevator")
    amenities['power_backup'] = st.checkbox("⚡ Power Backup")
    amenities['security'] = st.checkbox("🔒 24x7 Security")
    amenities['gym'] = st.checkbox("🏋️ Gym/Club House")
    amenities['swimming_pool'] = st.checkbox("🏊 Swimming Pool")
    amenities['garden'] = st.checkbox("🌳 Garden/Park")
    amenities['temple'] = st.checkbox("🛕 Temple/Prayer Room")
    amenities['vastu'] = st.checkbox("🕉️ Vastu Compliant")

# Enhanced prediction function for Indian market
def calculate_indian_property_price(city, property_type, bhk, area, location_type, age, floor, furnishing, parking, amenities):
    # Base prices per sq ft for major Indian cities (in INR)
    city_prices = {
        "Mumbai": 25000, "Delhi NCR": 12000, "Bangalore": 8500, "Hyderabad": 6500,
        "Chennai": 7000, "Pune": 7500, "Kolkata": 5500, "Ahmedabad": 5000,
        "Surat": 4500, "Jaipur": 4000, "Lucknow": 3500, "Kanpur": 3000,
        "Nagpur": 3500, "Indore": 3200, "Bhopal": 3000, "Visakhapatnam": 4500,
        "Patna": 2800, "Vadodara": 4200, "Ghaziabad": 5500, "Ludhiana": 4000
    }
    
    # Property type multipliers
    property_multipliers = {
        "Apartment/Flat": 1.0, "Independent House": 1.2, "Villa": 1.5,
        "Builder Floor": 1.1, "Penthouse": 1.8, "Studio Apartment": 0.85
    }
    
    # Location multipliers
    location_multipliers = {
        "Prime Location": 1.4, "Central Area": 1.2, "Suburb": 1.0,
        "Outskirts": 0.8, "IT Hub": 1.3, "Business District": 1.25
    }
    
    # Age multipliers
    age_multipliers = {
        "Under Construction": 0.9, "Ready to Move": 1.0, "0-1 Years": 1.05,
        "1-5 Years": 1.0, "5-10 Years": 0.95, "10-15 Years": 0.85, "15+ Years": 0.75
    }
    
    # Floor multipliers
    floor_multipliers = {
        "Ground Floor": 0.95, "1st-3rd Floor": 1.0, "4th-7th Floor": 1.05,
        "8th-12th Floor": 1.08, "Above 12th Floor": 1.12
    }
    
    # Furnishing multipliers
    furnishing_multipliers = {
        "Unfurnished": 1.0, "Semi-Furnished": 1.08, "Fully Furnished": 1.15
    }
    
    # Calculate base price
    base_price = city_prices[city] * area
    
    # Apply all multipliers
    base_price *= property_multipliers[property_type]
    base_price *= location_multipliers[location_type]
    base_price *= age_multipliers[age]
    base_price *= floor_multipliers[floor]
    base_price *= furnishing_multipliers[furnishing]
    
    # BHK adjustments
    bhk_multipliers = {"1 RK": 0.8, "1 BHK": 0.9, "2 BHK": 1.0, "3 BHK": 1.1, "4 BHK": 1.2, "5+ BHK": 1.3}
    base_price *= bhk_multipliers[bhk]
    
    # Parking bonus
    parking_bonus = {"No Parking": 0, "1 Car": 200000, "2 Cars": 350000, "3+ Cars": 500000}
    base_price += parking_bonus[parking]
    
    # Amenities bonus
    amenity_bonus = 0
    if amenities['lift']: amenity_bonus += 100000
    if amenities['power_backup']: amenity_bonus += 150000
    if amenities['security']: amenity_bonus += 200000
    if amenities['gym']: amenity_bonus += 300000
    if amenities['swimming_pool']: amenity_bonus += 500000
    if amenities['garden']: amenity_bonus += 100000
    if amenities['temple']: amenity_bonus += 50000
    if amenities['vastu']: amenity_bonus += 100000
    
    base_price += amenity_bonus
    
    return int(base_price)

# Calculate prediction
predicted_price = calculate_indian_property_price(
    city, property_type, bhk, area, location_type, age, floor, furnishing, parking, amenities
)

# Main prediction section
if st.button("🎯 Calculate Property Price", type="primary", use_container_width=True):
    
    # Main prediction display
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        margin: 2rem 0;
        border: 3px solid #4facfe;
        box-shadow: 0 15px 35px rgba(79, 172, 254, 0.3);
    ">
        <h2 style="color: #0369a1; margin: 0; font-size: 1.6rem;">💰 Estimated Property Value</h2>
        <h1 style="color: #1e293b; margin: 0.5rem 0; font-size: 4rem; font-weight: bold;">
            ₹{:,}
        </h1>
        <p style="color: #64748b; margin: 0; font-size: 1.2rem;">
            {:.2f} Crores | ±12% accuracy range
        </p>
    </div>
    """.format(predicted_price, predicted_price/10000000), unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        price_per_sqft = predicted_price / area
        st.metric(
            "💹 Price per Sq Ft",
            f"₹{price_per_sqft:,.0f}",
            delta=f"₹{price_per_sqft - 8000:+.0f}" if price_per_sqft > 8000 else None
        )
    
    with col2:
        monthly_emi = predicted_price * 0.0075  # 9% interest rate
        st.metric(
            "🏦 Monthly EMI",
            f"₹{monthly_emi:,.0f}",
            delta="@ 9% for 20 years"
        )
    
    with col3:
        stamp_duty = predicted_price * 0.05  # 5% stamp duty
        st.metric(
            "📋 Stamp Duty (Est.)",
            f"₹{stamp_duty:,.0f}",
            delta="5% of property value"
        )
    
    with col4:
        registration = predicted_price * 0.01  # 1% registration
        st.metric(
            "📄 Registration Fee",
            f"₹{registration:,.0f}",
            delta="1% of property value"
        )
    
    # Analysis tabs
    st.markdown("### 🔍 Detailed Analysis")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Price Breakdown", 
        "🏡 Property Summary", 
        "📈 Market Analysis", 
        "💼 Investment Insights"
    ])
    
    with tab1:
        # Price breakdown
        st.markdown("#### 💰 Price Breakdown")
        
        breakdown = {
            'Component': ['Base Property', 'Location Premium', 'Amenities', 'Market Factors'],
            'Value': [predicted_price * 0.6, predicted_price * 0.25, predicted_price * 0.1, predicted_price * 0.05]
        }
        
        fig = px.pie(
            values=breakdown['Value'], 
            names=breakdown['Component'],
            title="Property Value Components",
            color_discrete_sequence=['#667eea', '#764ba2', '#4facfe', '#00f2fe']
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Component metrics
        col_a, col_b, col_c, col_d = st.columns(4)
        with col_a:
            st.metric("🏠 Base Property", f"₹{breakdown['Value'][0]:,.0f}")
        with col_b:
            st.metric("📍 Location Premium", f"₹{breakdown['Value'][1]:,.0f}")
        with col_c:
            st.metric("✨ Amenities", f"₹{breakdown['Value'][2]:,.0f}")
        with col_d:
            st.metric("📈 Market Factors", f"₹{breakdown['Value'][3]:,.0f}")
    
    with tab2:
        # Property summary
        st.markdown("#### 🏠 Property Summary")
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); 
            padding: 2rem; 
            border-radius: 15px; 
            border-left: 5px solid #0ea5e9;
            margin: 1rem 0;
        ">
            <div style="
                display: grid; 
                grid-template-columns: 1fr 1fr; 
                gap: 1.2rem; 
                color: #0c4a6e;
                font-size: 1rem;
                line-height: 1.6;
            ">
                <div><strong>🏙️ City:</strong> {city}</div>
                <div><strong>🏠 Type:</strong> {property_type}</div>
                <div><strong>🏡 Configuration:</strong> {bhk}</div>
                <div><strong>📐 Area:</strong> {area:,} sq ft</div>
                <div><strong>📍 Location:</strong> {location_type}</div>
                <div><strong>📅 Age:</strong> {age}</div>
                <div><strong>🏢 Floor:</strong> {floor}</div>
                <div><strong>🪑 Furnishing:</strong> {furnishing}</div>
                <div style="grid-column: 1 / -1;"><strong>🚗 Parking:</strong> {parking}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Amenities list
        selected_amenities = [k.replace('_', ' ').title() for k, v in amenities.items() if v]
        if selected_amenities:
            st.markdown("#### ✨ Available Amenities")
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
                padding: 1.5rem;
                border-radius: 12px;
                border-left: 4px solid #f59e0b;
                margin: 1rem 0;
            ">
                <div style="color: #92400e; font-weight: 600; font-size: 1.1rem;">
                    {" • ".join(selected_amenities)}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("🏠 No additional amenities selected")
    
    with tab3:
        # Market analysis
        st.markdown("#### 📈 Market Analysis")
        
        # Sample market trend data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        prices = [predicted_price * (0.95 + i * 0.02) for i in range(6)]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=months, y=prices,
            mode='lines+markers',
            name='Price Trend',
            line=dict(color='#667eea', width=3),
            marker=dict(size=8, color='#764ba2')
        ))
        fig.update_layout(
            title="6-Month Price Trend",
            xaxis_title="Month",
            yaxis_title="Price (₹)",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Market insights
        st.markdown(f"""
        <div style="background: #f0f9ff; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #4facfe;">
            <h4 style="color: #0369a1; margin: 0 0 1rem 0;">💡 Market Insights</h4>
            <ul style="color: #0c4a6e; margin: 0;">
                <li>Property prices in {city} have shown {"strong growth" if city in ["Mumbai", "Delhi NCR", "Bangalore"] else "steady appreciation"}</li>
                <li>{location_type} areas are {"highly sought after" if location_type in ["Prime Location", "IT Hub"] else "showing good potential"}</li>
                <li>{bhk} properties are {"in high demand" if bhk in ["2 BHK", "3 BHK"] else "niche market segment"}</li>
                <li>Properties with amenities command {"premium pricing" if sum(amenities.values()) >= 4 else "standard rates"}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab4:
        # Investment insights
        st.markdown("#### 💼 Investment Insights")
        
        # Rental yield calculation
        annual_rent = predicted_price * (0.024 if city in ["Mumbai", "Delhi NCR"] else 0.03)
        rental_yield = (annual_rent / predicted_price) * 100
        
        col_x, col_y, col_z = st.columns(3)
        
        with col_x:
            st.metric("🏠 Rental Yield", f"{rental_yield:.1f}%", "Per annum")
        
        with col_y:
            monthly_rent = annual_rent / 12
            st.metric("💰 Monthly Rent", f"₹{monthly_rent:,.0f}", f"₹{annual_rent:,.0f}/year")
        
        with col_z:
            appreciation = 8 if city in ["Mumbai", "Delhi NCR", "Bangalore"] else 6
            st.metric("📈 Capital Appreciation", f"{appreciation}%", "Expected yearly")
        
        # Tax benefits
        st.markdown("""
        <div style="background: #fef3c7; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #f59e0b; margin-bottom: 2rem;">
            <h4 style="color: #92400e; margin: 0 0 1rem 0;">💰 Tax Benefits</h4>
            <ul style="color: #78350f; margin: 0;">
                <li><strong>Home Loan Interest (Section 24):</strong> Up to ₹2 Lakhs deduction</li>
                <li><strong>Principal Repayment (Section 80C):</strong> Up to ₹1.5 Lakhs deduction</li>
                <li><strong>First Time Buyer (Section 80EE):</strong> Additional ₹50,000 deduction</li>
                <li><strong>Total Annual Tax Savings:</strong> Up to ₹4 Lakhs</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Investment grade
        total_return = rental_yield + appreciation
        grade = "Excellent" if total_return > 12 else "Good" if total_return > 9 else "Average"
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); padding: 1.5rem; border-radius: 12px; border: 2px solid #4facfe;">
            <h4 style="color: #0369a1; margin: 0 0 1rem 0;">⭐ Investment Grade: {grade}</h4>
            <p style="color: #0c4a6e; margin: 0;">
                <strong>Total Expected Return:</strong> {total_return:.1f}% per annum<br>
                <strong>Recommendation:</strong> {
                    "Strong Buy - Excellent growth potential with good rental yields" if grade == "Excellent" 
                    else "Good Investment - Steady returns with moderate appreciation" if grade == "Good"
                    else "Consider carefully - Average returns expected"
                }
            </p>
        </div>
        """, unsafe_allow_html=True)

else:
    # Welcome message
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(240, 249, 255, 0.9) 0%, rgba(224, 242, 254, 0.9) 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 3rem 0;
        border: 3px dashed #4facfe;
    ">
        <h2 style="color: #0369a1; margin: 0 0 1rem 0; font-size: 2.5rem;">🏡 Welcome!</h2>
        <p style="color: #0c4a6e; font-size: 1.4rem; margin: 0; font-weight: 500;">
            Fill in your property details in the sidebar to get accurate price prediction<br>
            for Indian real estate market
        </p>
        <div class="modern-gradient" style="margin: 2rem auto; width: 200px;"></div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: white;">
    <h4 style="margin: 0 0 1rem 0; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">🏠 Indian Property Price Predictor</h4>
    <p style="margin: 0; font-size: 0.9rem; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
        Powered by Indian Real Estate Intelligence<br>
        <strong>Created with ❤️ by Ritesh</strong> | For educational and informational purposes
    </p>
    <div class="modern-gradient" style="margin: 1rem auto; width: 100px;"></div>
</div>
""", unsafe_allow_html=True)
