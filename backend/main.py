from fastapi import FastAPI
from backend.agents.intent_agent import detect_intent
from backend.agents.trust_agent import calculate_trust_score
from backend.agents.frustration_agent import detect_frustration
from backend.agents.response_agent import generate_response
from backend.agents.escalation_agent import decide_escalation


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "TrustCare AI is running!"
    }


@app.post("/analyze")
def analyze_customer_message(message: str):

    intent = detect_intent(message)

    trust_score = calculate_trust_score(message)

    frustration_score, frustration_level = detect_frustration(message)
    action, priority = generate_response(
    intent,
    trust_score,
    frustration_level
    )
    escalation, escalation_reason = decide_escalation(
    trust_score,
    frustration_level,
    priority
    )



    return {
    "customer_message": message,
    "intent": intent,
    "trust_score": trust_score,
    "frustration_score": frustration_score,
    "frustration_level": frustration_level,
    "action": action,
    "priority": priority,
    "escalation": escalation,
    "escalation_reason": escalation_reason
}