def calculate_trust_score(customer_message):
    message = customer_message.lower()

    score = 50

    # Positive signals
    if "thank" in message or "thanks" in message:
        score += 10

    if "please" in message:
        score += 5

    # Negative signals
    if "fraud" in message or "scam" in message:
        score -= 20

    if "angry" in message or "terrible" in message:
        score -= 10

    if "failed" in message or "problem" in message:
        score -= 5

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    return score


if __name__ == "__main__":
    message = "My payment failed and I am having a problem."

    score = calculate_trust_score(message)

    print("Trust Score:", score)