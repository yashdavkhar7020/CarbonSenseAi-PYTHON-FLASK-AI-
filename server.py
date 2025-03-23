from flask import Flask, request, jsonify
import os
import requests
import logging
import markdown2

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Cloud Run API URL
CLOUD_RUN_URL = *****************************************

@app.route('/get-ai-suggestions', methods=['POST'])
def get_ai_suggestions():
    data = request.json
    logging.info(f"Received request data: {data}")

    total_emissions = data.get('totalEmissions')
    per_capita_emissions = data.get('perCapitaEmissions')
    emission_reduction = data.get('emissionReduction')

    # Validate input data
    if (total_emissions is None or total_emissions <= 0 or
        per_capita_emissions is None or per_capita_emissions <= 0 or
        emission_reduction is None or emission_reduction < 0):
        logging.error("Invalid input data")
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        if not GOOGLE_API_KEY:
            logging.error("API key not found")
            return jsonify({'error': 'API key not found'}), 500

        request_body = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": (f"Based on the following data:\n\n"
                                     f"• **Total Emissions:** {total_emissions} tons CO2\n"
                                     f"• **Per Capita Emissions:** {per_capita_emissions} tons CO2 per person\n"
                                     f"• **Emission Reduction Target:** {emission_reduction} tons CO2\n\n"
                                     "Provide actionable pathways for achieving carbon neutrality in a structured format.\n\n"
                                     "Each suggestion should be an **object** with the following properties:\n\n"
                                     "• **ID**\n"
                                     "• **Title**\n"
                                     "• **Description**\n"
                                     "• **Category**\n"
                                     "• **Numeric cost analysis & recommendations**\n"
                                     "• **Policies introduced by the Indian government**\n\n"
                                     "Each property should be formatted as a bullet point, starting from a new line."
                            )
                        }
                    ]
                }
            ]
        }

        logging.info(f"Request body for Gemini API: {request_body}")

        response = requests.post(
            *****************************************************************
            json=request_body,
            headers={'Content-Type': 'application/json'}
        )

        logging.info(f"API response status code: {response.status_code}")
        response.raise_for_status()

        data = response.json()
        suggestions_content = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        logging.info(f"Suggestions from API: {suggestions_content}")

        if not suggestions_content:
            return jsonify({'html': "<p>No suggestions available based on the provided data.</p>"})

        # Convert Markdown to HTML
        html_content = markdown2.markdown(suggestions_content)

        return jsonify({'html': html_content})

    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        if e.response is not None:
            logging.error(f"Response content: {e.response.content}")
        return jsonify({'error': 'Failed to fetch data from API'}), 500

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Ensure the app listens on PORT for Google Cloud Run
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 for Cloud Run
    app.run(host="0.0.0.0", port=port)
