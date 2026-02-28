from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

OLLAMA_URL = "http://localhost:11434/api/generate"

# Core CSE Subject Prompts
SUBJECT_PROMPTS = {
    "OS": """
    You are an Operating Systems professor.
    Explain concepts clearly with:
    - Definitions
    - Diagrams explanation (if needed)
    - Examples
    - Important interview points
    """,

    "CN": """
    You are a Computer Networks expert.
    Explain in structured format with:
    - Layer-wise explanation (if applicable)
    - Real-world examples
    - Protocol details
    - Interview-focused explanation
    """,

    "DBMS": """
    You are a Database Management Systems professor.
    Explain with:
    - Definitions
    - SQL examples (if required)
    - Normalization explanation
    - ACID properties if relevant
    - Interview important points
    """,

    "General": "You are a helpful AI assistant."
}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    subject = data.get("subject", "General")

    system_prompt = SUBJECT_PROMPTS.get(subject, SUBJECT_PROMPTS["General"])

    final_prompt = f"""
    {system_prompt}

    Student Question: {user_message}
    """

    payload = {
        "model": "phi3:mini",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return jsonify({"response": response.json()["response"]})
    else:
        return jsonify({"error": "Model failed"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)