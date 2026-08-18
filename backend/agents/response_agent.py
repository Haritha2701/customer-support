def generate_response(intent, trust_score, frustration_level):

    if frustration_level == "HIGH":
        action = "HUMAN_ESCALATION"
        priority = "HIGH"

    elif trust_score < 40:
        action = "HUMAN_ESCALATION"
        priority = "HIGH"

    elif intent == "PAYMENT_PROBLEM":
        action = "PAYMENT_SUPPORT"
        priority = "MEDIUM"

    else:
        action = "NORMAL_SUPPORT"
        priority = "LOW"

    return action, priority

if __name__ == "__main__":
    action, priority = generate_response(
        "PAYMENT_PROBLEM",
        45,
        "LOW"
    )

    print("Action:", action)
    print("Priority:", priority)