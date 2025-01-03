from flask import Flask, request, jsonify
import os
import requests
import logging
import markdown2

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

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
                            "text": (f"Based on the following data: Total Emissions: {total_emissions} tons CO2, "
                                     f"Per Capita Emissions: {per_capita_emissions} tons CO2 per person, and "
                                     f"Emission Reduction of {emission_reduction} tons co2, provide suggestions and pathways "
                                     "for achieving carbon neutrality in a structured format. Please provide each "
                                     "suggestion as a separate object with the following properties: id, title, "
                                     "description, category, numeric cost analysis and recommendations, Policies introduced my indian government. every property should have bullet point and every property should start from new line  Each recommendation should be a "
                                     "bullet point with a brief description, and should include a unique id and a brief description.")
                        }
                    ]
                }
            ]
        }

        logging.info(f"Request body for Gemini API: {request_body}")

        response = requests.post(
            f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GOOGLE_API_KEY}',
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

if __name__ == '__main__':
    app.run(port=5000)
