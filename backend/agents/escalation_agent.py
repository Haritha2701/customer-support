def decide_escalation(trust_score, frustration_level, priority):

    if frustration_level == "HIGH":
        escalation = True
        reason = "Customer frustration is high"

    elif trust_score < 40:
        escalation = True
        reason = "Customer trust score is low"

    elif priority == "HIGH":
        escalation = True
        reason = "Case has high priority"

    else:
        escalation = False
        reason = "Customer can continue with automated support"

    return escalation, reason


if __name__ == "__main__":

    escalation, reason = decide_escalation(
        45,
        "LOW",
        "MEDIUM"
    )

    print("Escalation:", escalation)
    print("Reason:", reason)