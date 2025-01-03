import streamlit as st

# Constants for industries and units
industry_options = [
    {"value": "agriculture", "label": "Agriculture"},
    {"value": "transportation", "label": "Transportation"},
    {"value": "manufacturing", "label": "Manufacturing"},
    {"value": "construction", "label": "Construction"},
    {"value": "energy", "label": "Energy"},
    {"value": "waste_management", "label": "Waste Management"},
    {"value": "mining", "label": "Mining"},
    {"value": "forestry", "label": "Forestry"},
    {"value": "fisheries", "label": "Fisheries"},
    {"value": "commercial", "label": "Commercial"},
    {"value": "residential", "label": "Residential"},
    {"value": "textiles", "label": "Textiles"},
    {"value": "food_processing", "label": "Food Processing"},
    {"value": "chemicals", "label": "Chemicals"},
    {"value": "pharmaceuticals", "label": "Pharmaceuticals"},
    {"value": "automotive", "label": "Automotive"},
    {"value": "aerospace", "label": "Aerospace"},
    {"value": "technology", "label": "Technology"},
    # Add more industries as needed
]

unit_options = [
    {"value": "liters", "label": "Liters (L)"},
    {"value": "kilometers", "label": "Kilometers (km)"},
    {"value": "meters", "label": "Meters (m)"},
    {"value": "grams", "label": "Grams (g)"},
    {"value": "kilograms", "label": "Kilograms (kg)"},
    {"value": "miles", "label": "Miles (mi)"},
    {"value": "feet", "label": "Feet (ft)"},
    {"value": "inches", "label": "Inches (in)"},
    {"value": "square_meters", "label": "Square Meters (m²)"},
    {"value": "cubic_meters", "label": "Cubic Meters (m³)"},
    {"value": "degrees_celsius", "label": "Degrees Celsius (°C)"},
    {"value": "degrees_fahrenheit", "label": "Degrees Fahrenheit (°F)"},
    {"value": "watts", "label": "Watts (W)"},
    {"value": "kilowatt_hours", "label": "Kilowatt Hours (kWh)"},
    {"value": "joules", "label": "Joules (J)"},
    {"value": "newtons", "label": "Newtons (N)"},
    {"value": "pascals", "label": "Pascals (Pa)"},
    {"value": "miles_per_hour", "label": "Miles per Hour (mph)"},
    {"value": "kilometers_per_hour", "label": "Kilometers per Hour (km/h)"},
    {"value": "liters_per_100km", "label": "Liters per 100 km (L/100 km)"},
    {"value": "parts_per_million", "label": "Parts Per Million (ppm)"},
    {"value": "Tons", "label": "Tons"},
    # Add more units as needed
]

# Initialize the session state for storing parameters if not already done
if "parameters" not in st.session_state:
    st.session_state.parameters = [{"name": "", "unit": ""}]
if "refresh" not in st.session_state:
    st.session_state.refresh = False

def main():
    # Title and introductory text
    st.title("Carbon Sense AI Customization")
    st.write("Customize your enterprise carbon calculator to meet your specific industry needs.")

    # Industry Selector
    selected_industry = st.selectbox(
        "Select Industry",
        [industry["label"] for industry in industry_options]
    )
    
    # Displaying Parameters
    st.subheader("Parameters")
    for i, parameter in enumerate(st.session_state.parameters):
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            parameter["name"] = st.text_input(f"Parameter {i+1} Name", parameter["name"], key=f"name_{i}")
        with col2:
            parameter["unit"] = st.selectbox(
                f"Unit {i+1}",
                [unit["label"] for unit in unit_options],
                key=f"unit_{i}"
            )
        with col3:
            if st.button("Remove", key=f"remove_{i}"):
                st.session_state.parameters.pop(i)
                st.session_state.refresh = not st.session_state.refresh  # Toggle refresh flag to update UI

    # Button to add a new parameter
    if st.button("Add Parameter"):
        st.session_state.parameters.append({"name": "", "unit": ""})
        st.session_state.refresh = not st.session_state.refresh  # Toggle refresh flag to update UI

    # Results Options for Customization
    st.subheader("Results Options")

    results_options = {
        "estimation": st.checkbox("Enable Estimation", value=True),
        "aiSuggestion": st.checkbox("Enable AI Suggestions", value=True),
        "historyComparison": st.checkbox("Enable History Comparison", value=False),
        "charts": st.checkbox("Enable Charts", value=False),
        "dataDownload": st.checkbox("Enable Data Download", value=False)
    }

    # Display example results for selected options
    if results_options["estimation"]:
        with st.expander("Estimation Example"):
            st.write("This is an example of how estimations would appear in your calculator.")
            st.write("Estimated Carbon Emission: 5.2 tons CO₂e")
            st.write("Expected reduction if green practices are implemented: 20%")

    if results_options["aiSuggestion"]:
        with st.expander("AI Suggestions Example"):
            st.write("Here is how AI suggestions would guide you to reduce emissions.")
            st.write("**Suggestion 1:** Shift to renewable energy sources to reduce carbon footprint.")
            st.write("**Suggestion 2:** Optimize supply chain for reduced emissions.")

    if results_options["historyComparison"]:
        with st.expander("History Comparison Example"):
            st.write("Visual comparison of past and current emission levels:")
            st.line_chart({"Month": ["Jan", "Feb", "Mar", "Apr"], "Emission Levels": [4.5, 4.2, 3.9, 3.7]})

    if results_options["charts"]:
        with st.expander("Charts Example"):
            st.write("Example charts to visualize emission data:")
            st.bar_chart({"Category": ["Energy", "Transportation", "Waste"], "Emissions": [2.5, 1.8, 0.9]})
            st.area_chart({"Time": ["Q1", "Q2", "Q3", "Q4"], "Total Emissions": [5, 4.7, 4.5, 4.2]})

    if results_options["dataDownload"]:
        with st.expander("Data Download Example"):
            st.write("You’ll have the option to download data in formats like CSV or Excel for further analysis.")
            st.download_button("Download Sample Data", data="Sample emission data...", file_name="sample_data.csv")

    # Submit Button with Modal Simulation
    if st.button("Submit Customizations"):
        # Modal dialog simulation using Streamlit's success/info message
        st.success("Thank you for your enterprise calculator customizations!")
        st.info(
            "We will make the calculator functional in 1-2 hours, and an email will be sent to you for usage. "
            "You’ll also have the option to further customize as needed. A consultant will be assigned to your "
            "enterprise to achieve net zero goals and potential revenue from carbon credits, with applicable consultation fees."
        )

# Run the main function to display the Streamlit app
if __name__ == "__main__":
    main()
