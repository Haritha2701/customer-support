from flask import Flask, request, jsonify
from flask_cors import CORS

from agents.frustration_agent import detect_frustration
from agents.knowledge_agent import search_knowledge
from agents.resolution_agent import generate_response
from agents.trust_agent import calculate_trust_score

import json
import os
from datetime import datetime


app = Flask(__name__)

CORS(app)


# ==========================================
# ESCALATION FILE
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

ESCALATION_FILE = os.path.join(
    BASE_DIR,
    "data",
    "escalations.json"
)


# ==========================================
# LOAD ESCALATIONS
# ==========================================

def load_escalations():

    try:

        with open(
            ESCALATION_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        return []


# ==========================================
# SAVE ESCALATIONS
# ==========================================

def write_escalations(escalations):

    with open(
        ESCALATION_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            escalations,
            file,
            indent=4
        )


# ==========================================
# SAVE ESCALATED CUSTOMER
# ==========================================

def save_escalation(
    message,
    frustration_result,
    knowledge_result,
    trust_result
):

    escalations = load_escalations()


    escalation = {

        "id": len(escalations) + 1,

        "time": datetime.now().isoformat(),

        "customer_message": message,

        "frustration_score":
            frustration_result.get(
                "frustration_score",
                0
            ),

        "frustration_level":
            frustration_result.get(
                "level",
                "UNKNOWN"
            ),

        "category":
            knowledge_result.get(
                "category",
                "Unknown"
            ),

        "knowledge_confidence":
            knowledge_result.get(
                "confidence",
                0
            ),

        "trust_score":
            trust_result.get(
                "trust_score",
                0
            ),

        "trust_level":
            trust_result.get(
                "trust_level",
                "UNKNOWN"
            ),

        "escalation_reason":
            trust_result.get(
                "escalation_reason",
                ""
            ),

        "status": "OPEN"

    }


    escalations.append(escalation)

    write_escalations(escalations)


    print("\n🚨 ESCALATION SAVED")
    print(escalation)


# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    return "TrustCare AI Backend is running!"


# ==========================================
# GET ESCALATIONS
# ==========================================

@app.route(
    "/escalations",
    methods=["GET"]
)
def get_escalations():

    escalations = load_escalations()

    return jsonify({
        "escalations": escalations
    })


# ==========================================
# RESOLVE ESCALATION
# ==========================================

@app.route(
    "/escalations/<int:escalation_id>/resolve",
    methods=["PUT"]
)
def resolve_escalation(escalation_id):

    escalations = load_escalations()


    for escalation in escalations:

        if escalation.get("id") == escalation_id:

            escalation["status"] = "RESOLVED"

            escalation["resolved_time"] = (
                datetime.now().isoformat()
            )

            write_escalations(escalations)


            return jsonify({

                "success": True,

                "message":
                    "Escalation resolved successfully.",

                "escalation":
                    escalation

            })


    return jsonify({

        "success": False,

        "error":
            "Escalation not found."

    }), 404


# ==========================================
# CHAT
# ==========================================

@app.route(
    "/chat",
    methods=["POST"]
)
def chat():

    data = request.get_json()


    if not data:

        return jsonify({
            "error": "No data received."
        }), 400


    message = data.get(
        "message",
        ""
    ).strip()


    if not message:

        return jsonify({
            "error": "Message is empty"
        }), 400


    print("\n==============================")
    print("CUSTOMER MESSAGE")
    print("==============================")

    print(message)


    # ======================================
    # 1. FRUSTRATION AGENT
    # ======================================

    frustration_result = detect_frustration(
        message
    )

    print("\nFRUSTRATION RESULT:")

    print(frustration_result)


    # ======================================
    # 2. KNOWLEDGE AGENT
    # ======================================

    knowledge_result = search_knowledge(
        message
    )

    print("\nKNOWLEDGE RESULT:")

    print(knowledge_result)


    # ======================================
    # 3. TRUST AGENT
    # ======================================

    trust_result = calculate_trust_score(
        frustration_result,
        knowledge_result
    )

    print("\nTRUST RESULT:")

    print(trust_result)


    # ======================================
    # 4. ESCALATION
    # ======================================

    if trust_result.get(
        "escalation_required",
        False
    ):

        save_escalation(

            message,

            frustration_result,

            knowledge_result,

            trust_result

        )


    # ======================================
    # 5. RESOLUTION AGENT
    # ======================================

    response = generate_response(

        message,

        frustration_result,

        knowledge_result

    )


    print("\nAI RESPONSE:")

    print(response)


    # ======================================
    # SEND RESPONSE
    # ======================================

    return jsonify({

        "response": response,

        "frustration":
            frustration_result,

        "knowledge":
            knowledge_result,

        "trust":
            trust_result

    })


# ==========================================
# START FLASK
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )

    