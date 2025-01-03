# import streamlit as st
# import requests
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px
# import io

# # Constants
# MARKET_RATE_PER_TON = 10  # Example market rate for carbon credits in USD per ton
# SERVER_URL = 'http://localhost:5000'  # URL of your backend server





# # Calculation functions
# def calculate_total_emissions(excavation, equipment_utilization, transportation, diesel_consumption, 
#                                methane_content, coal_washing, electricity_consumption, ventilation_airflow, dust_emissions):
#     return (excavation + transportation + diesel_consumption + methane_content + coal_washing + 
#             electricity_consumption + ventilation_airflow + dust_emissions) * (1 - equipment_utilization / 100)

# def calculate_reduction_impact(clean_tech, renewable_energy, methane_capture, diesel_consumption, 
#                                methane_content, coal_washing):
#     return (clean_tech + renewable_energy + methane_capture) * (diesel_consumption + methane_content + coal_washing) * 0.01

# def calculate_carbon_sink(plantation_sink):
#     return plantation_sink * 1.2

# def calculate_emission_gap(total_emissions, carbon_sink):
#     return total_emissions - carbon_sink

# def calculate_carbon_credits_value(emission_gap):
#     return emission_gap * 0.5  # Example calculation

# def calculate_land_required_for_afforestation(carbon_sink):
#     return carbon_sink / 7  # Example conversion factor

# # Function to fetch reduction pathways from server API
# def fetch_reduction_pathways(total_emissions, per_capita_emissions, reduction_impact):
#     try:
#         response = requests.post(
#             f'{SERVER_URL}/get-ai-suggestions',
#             json={
#                 'totalEmissions': total_emissions,
#                 'perCapitaEmissions': per_capita_emissions,
#                 'emissionReduction': reduction_impact
#             },
#             headers={'Content-Type': 'application/json'}
#         )
#         response.raise_for_status()
#         data = response.json()
#         html_content = data.get('html', '')

#         if not html_content:
#             return "<p>No suggestions available</p>"

#         return html_content
#     except requests.RequestException as e:
#         st.error(f"Error fetching reduction pathways: {e}")
#         return "<p>Error fetching reduction pathways. Please check the console for details.</p>"
#     except Exception as e:
#         st.error(f"An unexpected error occurred: {e}")
#         return "<p>An unexpected error occurred. Please check the console for details.</p>"

# # Function to load historical data
# def load_historical_data():
#     try:
#         historical_data = pd.read_csv('historical_data.csv')
#         return historical_data
#     except Exception as e:
#         st.error(f"Error loading historical data: {e}")
#         return pd.DataFrame()

# # Streamlit UI
# st.title("CarbonSense AI")

# # User Inputs
# with st.form("emissionsForm"):
#     excavation = st.number_input('Excavation (tons)', min_value=0.0, value=0.0, step=1.0)
#     equipment_utilization = st.number_input('Equipment Utilization (%)', min_value=0.0, max_value=100.0, value=0.0, step=1.0)
#     transportation = st.number_input('Transportation (tons)', min_value=0.0, value=0.0, step=1.0)
#     population = st.number_input('Population', min_value=1, value=1, step=1)
#     plantation_sink = st.number_input('Plantation Sink (hectares)', min_value=0.0, value=0.0, step=1.0)
#     clean_tech = st.number_input('Clean Tech (%)', min_value=0.0, max_value=100.0, value=0.0, step=1.0)
#     renewable_energy = st.number_input('Renewable Energy (%)', min_value=0.0, max_value=100.0, value=0.0, step=1.0)
#     methane_capture = st.number_input('Methane Capture (%)', min_value=0.0, max_value=100.0, value=0.0, step=1.0)
#     diesel_consumption = st.number_input('Diesel Consumption (liters)', min_value=0.0, value=0.0, step=1.0)
#     methane_content = st.number_input('Methane Content (m³)', min_value=0.0, value=0.0, step=1.0)
#     coal_washing = st.number_input('Coal Washing (tons)', min_value=0.0, value=0.0, step=1.0)
#     electricity_consumption = st.number_input('Electricity Consumption (kWh)', min_value=0.0, value=0.0, step=1.0)
#     ventilation_airflow = st.number_input('Ventilation Airflow (m³/s)', min_value=0.0, value=0.0, step=1.0)
#     dust_emissions = st.number_input('Dust Emissions (tons)', min_value=0.0, value=0.0, step=1.0)
#     # Submit Button
#     submitted = st.form_submit_button("Calculate")

# if submitted:
#     total_emissions = calculate_total_emissions(excavation, equipment_utilization, transportation, diesel_consumption, 
#                                                 methane_content, coal_washing, electricity_consumption, ventilation_airflow, dust_emissions)
#     per_capita_emissions = total_emissions / population if population > 0 else 0
#     reduction_impact = calculate_reduction_impact(clean_tech, renewable_energy, methane_capture, diesel_consumption, 
#                                                  methane_content, coal_washing)
#     carbon_sink = calculate_carbon_sink(plantation_sink)
#     emission_gap = calculate_emission_gap(total_emissions, carbon_sink)
#     carbon_credits_value = calculate_carbon_credits_value(emission_gap)
#     land_required_for_afforestation = calculate_land_required_for_afforestation(carbon_sink)
#     potential_revenue = carbon_credits_value * MARKET_RATE_PER_TON

#     st.subheader("Current Data")
#     st.write(f"Total Emissions: {total_emissions:.2f} tons CO₂")
#     st.write(f"Per Capita Emissions: {per_capita_emissions:.2f} tons CO₂")
#     st.write(f"Reduction Impact: {reduction_impact:.2f} tons CO₂")
#     st.write(f"Carbon Sink: {carbon_sink:.2f} tons CO₂")
#     st.write(f"Emission Gap: {emission_gap:.2f} tons CO₂")
#     st.write(f"Estimated Carbon Credits: {carbon_credits_value:.2f} tons CO₂")
#     st.write(f"Potential Revenue from Carbon Credits: ${potential_revenue:.2f}")
#     st.write(f"Land Required for Afforestation: {land_required_for_afforestation:.2f} hectares")

#     pathways_html = fetch_reduction_pathways(total_emissions, per_capita_emissions, reduction_impact)
#     st.markdown(pathways_html, unsafe_allow_html=True)

#     # Load historical data
#     historical_data = load_historical_data()

#     if not historical_data.empty:
#         # Display columns in historical data for debugging
#         st.subheader("Historical Data Columns")
#         st.write(historical_data.columns)

#         # Comparison Table
#         st.subheader("Historical Data Comparison")
#         st.write(historical_data)

#         # Plotting with Matplotlib
#         st.subheader("Charts")
        
#         # Ensure the necessary columns exist in the historical data
#         if 'year' in historical_data.columns and 'totalEmissions' in historical_data.columns:
#             fig, ax = plt.subplots(figsize=(10, 6))
#             ax.plot(historical_data['year'], historical_data['totalEmissions'], label='Historical Emissions', marker='o', color='royalblue', linestyle='-')
#             ax.axhline(y=total_emissions, color='red', linestyle='--', label='Current Emissions')
#             ax.set_xlabel('Year', fontsize=12)
#             ax.set_ylabel('Total Emissions (tons CO₂)', fontsize=12)
#             ax.set_title('Historical vs Current Emissions', fontsize=14)
#             ax.legend()
#             ax.grid(True, linestyle='--', alpha=0.7)
#             st.pyplot(fig)
#         else:
#             st.error("The historical data CSV must contain 'year' and 'totalEmissions' columns.")
        
#         # Emission Reduction Impact
#         reduction_impact_data = {
#             'Category': ['Clean Tech', 'Renewable Energy', 'Methane Capture'],
#             'Impact': [clean_tech, renewable_energy, methane_capture]
#         }
#         reduction_df = pd.DataFrame(reduction_impact_data)
#         fig = px.bar(reduction_df, x='Category', y='Impact', title='Emission Reduction Impact by Category',
#                      color='Category', color_discrete_map={'Clean Tech': 'teal', 'Renewable Energy': 'orange', 'Methane Capture': 'green'})
#         fig.update_layout(xaxis_title='Category', yaxis_title='Impact (%)', title_x=0.5, title_font_size=14)
#         st.plotly_chart(fig)
        
#         # Carbon Sink and Emission Gap
#         sink_gap_data = {
#             'Category': ['Carbon Sink', 'Emission Gap'],
#             'Amount': [carbon_sink, emission_gap]
#         }
#         sink_gap_df = pd.DataFrame(sink_gap_data)
#         fig = px.pie(sink_gap_df, names='Category', values='Amount', title='Carbon Sink vs Emission Gap',
#                      color='Category', color_discrete_map={'Carbon Sink': 'blue', 'Emission Gap': 'red'})
#         fig.update_traces(textinfo='percent+label', hole=0.4)
#         fig.update_layout(title_x=0.5, title_font_size=14)
#         st.plotly_chart(fig)









import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import folium
import io
from streamlit_folium import folium_static


# Constants
MARKET_RATE_PER_TON = 10  # Example market rate for carbon credits in USD per ton
SERVER_URL = 'http://localhost:5000'  # URL of your backend server

total_emissions = 0.0
per_capita_emissions = 0.0
reduction_impact = 0.0
carbon_sink = 0.0
emission_gap = 0.0
carbon_credits_value = 0.0
land_required_for_afforestation = 0.0

# Calculation functions
def calculate_total_emissions(excavation, equipment_utilization, transportation, diesel_consumption, 
                               methane_content, coal_washing, electricity_consumption, ventilation_airflow, dust_emissions):
    return (excavation + transportation + diesel_consumption + methane_content + coal_washing + 
            electricity_consumption + ventilation_airflow + dust_emissions) * (1 - equipment_utilization / 100)

def calculate_reduction_impact(clean_tech, renewable_energy, methane_capture, diesel_consumption, 
                               methane_content, coal_washing):
    return (clean_tech + renewable_energy + methane_capture) * (diesel_consumption + methane_content + coal_washing) * 0.01

def calculate_carbon_sink(plantation_sink):
    return plantation_sink * 1.2

def calculate_emission_gap(total_emissions, carbon_sink):
    return total_emissions - carbon_sink

def calculate_carbon_credits_value(emission_gap):
    return emission_gap * 0.5  # Example calculation

def calculate_land_required_for_afforestation(carbon_sink):
    return carbon_sink / 7  # Example conversion factor

# Function to fetch reduction pathways from server API
def fetch_reduction_pathways(total_emissions, per_capita_emissions, reduction_impact):
    try:
        response = requests.post(
            f'{SERVER_URL}/get-ai-suggestions',
            json={
                'totalEmissions': total_emissions,
                'perCapitaEmissions': per_capita_emissions,
                'emissionReduction': reduction_impact
            },
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
        data = response.json()
        html_content = data.get('html', '')

        if not html_content:
            return "<p>No suggestions available</p>"

        return html_content
    except requests.RequestException as e:
        st.error(f"Error fetching reduction pathways: {e}")
        return "<p>Error fetching reduction pathways. Please check the console for details.</p>"
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return "<p>An unexpected error occurred. Please check the console for details.</p>"

# Function to load historical data
def load_historical_data():
    try:
        historical_data = pd.read_csv('historical_data.csv')
        return historical_data
    except Exception as e:
        st.error(f"Error loading historical data: {e}")
        return pd.DataFrame()

# Streamlit UI
st.title("CarbonSense AI")

# User Inputs
with st.form("emissionsForm"):
    excavation = st.number_input('Excavation (tons)', min_value=0.0, value=0.0, step=1.0)
    equipment_utilization = st.number_input('Equipment Utilization (%)', min_value=0.0, max_value=100.0, value=0.0, step=1.0)
    transportation = st.number_input('Transportation (tons)', min_value=0.0, value=0.0, step=1.0)
    population = st.number_input('Population', min_value=1, value=1, step=1)
    plantation_sink = st.number_input('Plantation Sink (hectares)', min_value=0.0, value=0.0, step=1.0)
    clean_tech = st.number_input('Clean Tech (%)', min_value=0.0, max_value=100.0, value=0.0, step=1.0)
    renewable_energy = st.number_input('Renewable Energy (%)', min_value=0.0, max_value=100.0, value=0.0, step=1.0)
    methane_capture = st.number_input('Methane Capture (%)', min_value=0.0, max_value=100.0, value=0.0, step=1.0)
    diesel_consumption = st.number_input('Diesel Consumption (liters)', min_value=0.0, value=0.0, step=1.0)
    methane_content = st.number_input('Methane Content (m³)', min_value=0.0, value=0.0, step=1.0)
    coal_washing = st.number_input('Coal Washing (tons)', min_value=0.0, value=0.0, step=1.0)
    electricity_consumption = st.number_input('Electricity Consumption (kWh)', min_value=0.0, value=0.0, step=1.0)
    ventilation_airflow = st.number_input('Ventilation Airflow (m³/s)', min_value=0.0, value=0.0, step=1.0)
    dust_emissions = st.number_input('Dust Emissions (tons)', min_value=0.0, value=0.0, step=1.0)

    # Market Rate per Ton of Carbon Credits
    carbon_price = st.slider('Market Rate per Ton of Carbon Credits (USD)', min_value=1, max_value=100, value=MARKET_RATE_PER_TON)

    # Select Reduction Pathways
    selected_pathways = st.multiselect('Select Reduction Pathways', ['Clean Tech', 'Renewable Energy', 'Methane Capture'])

    # Submit Button
    submitted = st.form_submit_button("Calculate")

if submitted:
    total_emissions = calculate_total_emissions(excavation, equipment_utilization, transportation, diesel_consumption, 
                                                methane_content, coal_washing, electricity_consumption, ventilation_airflow, dust_emissions)
    per_capita_emissions = total_emissions / population if population > 0 else 0
    reduction_impact = sum([clean_tech if 'Clean Tech' in selected_pathways else 0,
                            renewable_energy if 'Renewable Energy' in selected_pathways else 0,
                            methane_capture if 'Methane Capture' in selected_pathways else 0])
    carbon_sink = calculate_carbon_sink(plantation_sink)
    emission_gap = calculate_emission_gap(total_emissions, carbon_sink)
    carbon_credits_value = calculate_carbon_credits_value(emission_gap)
    land_required_for_afforestation = calculate_land_required_for_afforestation(carbon_sink)
    potential_revenue = carbon_credits_value * carbon_price

    st.subheader("Current Data")
    st.write(f"Total Emissions: {total_emissions:.2f} tons CO₂")
    st.write(f"Per Capita Emissions: {per_capita_emissions:.2f} tons CO₂")
    st.write(f"Reduction Impact: {reduction_impact:.2f} tons CO₂")
    st.write(f"Carbon Sink: {carbon_sink:.2f} tons CO₂")
    st.write(f"Emission Gap: {emission_gap:.2f} tons CO₂")
    st.write(f"Estimated Carbon Credits: {carbon_credits_value:.2f} tons CO₂")
    st.write(f"Potential Revenue from Carbon Credits at ${carbon_price} per ton: ${potential_revenue:.2f}")
    st.write(f"Land Required for Afforestation: {land_required_for_afforestation:.2f} hectares")

    pathways_html = fetch_reduction_pathways(total_emissions, per_capita_emissions, reduction_impact)
    st.markdown(pathways_html, unsafe_allow_html=True)

    # Load historical data
    historical_data = load_historical_data()

    if not historical_data.empty:
        st.subheader("Historical Data Comparison")
        st.write(historical_data)

        # Plotting with Matplotlib
        st.subheader("Charts")

        # Ensure the necessary columns exist in the historical data
        if 'year' in historical_data.columns and 'totalEmissions' in historical_data.columns:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(historical_data['year'], historical_data['totalEmissions'], label='Historical Emissions', marker='o', color='royalblue', linestyle='-')
            ax.axhline(y=total_emissions, color='red', linestyle='--', label='Current Emissions')
            ax.set_xlabel('Year', fontsize=12)
            ax.set_ylabel('Total Emissions (tons CO₂)', fontsize=12)
            ax.set_title('Historical vs Current Emissions', fontsize=14)
            ax.legend()
            ax.grid(True, linestyle='--', alpha=0.7)
            st.pyplot(fig)
        else:
            st.error("The historical data CSV must contain 'year' and 'totalEmissions' columns.")

        # Emission Reduction Impact
        reduction_impact_data = {
            'Category': ['Clean Tech', 'Renewable Energy', 'Methane Capture'],
            'Impact': [clean_tech, renewable_energy, methane_capture]
        }
        reduction_df = pd.DataFrame(reduction_impact_data)
        fig = px.bar(reduction_df, x='Category', y='Impact', title='Emission Reduction Impact by Category',
                     color='Category', color_discrete_map={'Clean Tech': 'teal', 'Renewable Energy': 'orange', 'Methane Capture': 'green'})
        fig.update_layout(xaxis_title='Category', yaxis_title='Impact (%)', bargap=0.4)
        st.plotly_chart(fig)

        # CO2 Emissions by Year - Seaborn Lineplot
        if 'totalEmissions' in historical_data.columns:
            plt.figure(figsize=(10, 6))
            sns.lineplot(x='year', y='totalEmissions', data=historical_data, marker='o', color='skyblue', label='Emissions Over Time')
            plt.axhline(y=total_emissions, color='coral', linestyle='--', label='Current Emissions')
            plt.xlabel('Year', fontsize=12)
            plt.ylabel('Emissions (tons CO₂)', fontsize=12)
            plt.title('CO₂ Emissions by Year', fontsize=14)
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)
            st.pyplot(plt.gcf())

        # Emissions Contribution per Category
        fig = plt.figure(figsize=(10, 6))
        labels = ['Excavation', 'Transportation', 'Diesel Consumption', 'Methane Content', 'Coal Washing', 'Electricity Consumption', 'Ventilation Airflow', 'Dust Emissions']
        sizes = [excavation, transportation, diesel_consumption, methane_content, coal_washing, electricity_consumption, ventilation_airflow, dust_emissions]
        colors = sns.color_palette('Set2', len(sizes))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
        plt.title('Emissions Contribution per Category')
        plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
        st.pyplot(fig)
        
    # Interactive Map for Afforestation
    st.subheader("Interactive Map for Afforestation")
    map_center = [20.5937, 78.9629]  # Center map on India
    afforestation_map = folium.Map(location=map_center, zoom_start=5)

    folium.Marker(
        location=map_center,
        popup=f"Land Required for Afforestation: {land_required_for_afforestation:.2f} hectares",
        icon=folium.Icon(icon="tree", color="green"),
    ).add_to(afforestation_map)

    folium_static(afforestation_map)

    # Additional Map: High Carbon Emission Areas
    st.subheader("High Carbon Emission Areas")
    emission_map_center = [23.2599, 77.4126]  # Center map on a specific region (e.g., Madhya Pradesh, India)
    emission_map = folium.Map(location=emission_map_center, zoom_start=6)

    # Example markers for high carbon emission areas (dummy coordinates)
    high_emission_areas = [
        {"location": [22.7196, 75.8577], "name": "Indore", "emissions": 200.5},
        {"location": [23.6102, 85.2799], "name": "Ranchi", "emissions": 180.3},
        {"location": [21.2514, 81.6296], "name": "Raipur", "emissions": 210.7},
    ]

    for area in high_emission_areas:
        folium.Marker(
            location=area["location"],
            popup=f"{area['name']}: {area['emissions']} tons CO₂",
            icon=folium.Icon(icon="cloud", color="red"),
        ).add_to(emission_map)

    folium_static(emission_map)

    # Data Download as Excel
   # Streamlit subheader
st.subheader("Download Calculated Data")

# Creating DataFrame
data = {
    'Category': ['Total Emissions', 'Per Capita Emissions', 'Reduction Impact', 'Carbon Sink', 'Emission Gap', 'Carbon Credits Value', 'Land Required for Afforestation'],
    'Value': [total_emissions, per_capita_emissions, reduction_impact, carbon_sink, emission_gap, carbon_credits_value, land_required_for_afforestation]
}
df = pd.DataFrame(data)

# Create a buffer to hold the Excel data
buffer = io.BytesIO()

# Write the DataFrame to the buffer
with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Carbon_Sense_AI')

# Reset the buffer's position to the beginning
buffer.seek(0)

# Streamlit download button
st.download_button(
    label="Download Data as Excel",
    data=buffer,
    file_name='carbon_sense_ai_data.xlsx',
    mime='application/vnd.ms-excel'
)

# Display the DataFrame in Streamlit
st.write(df)
