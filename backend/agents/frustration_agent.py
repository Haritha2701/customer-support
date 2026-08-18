def detect_frustration(customer_message):
    message = customer_message.lower()

    frustration_score = 0

    # Strong frustration words
    strong_words = [
        "angry",
        "furious",
        "terrible",
        "worst",
        "scam",
        "useless"
    ]

    # Medium frustration words
    medium_words = [
        "bad",
        "problem",
        "failed",
        "disappointed",
        "annoyed"
    ]

    # Check strong words
    for word in strong_words:
        if word in message:
            frustration_score += 20

    # Check medium words
    for word in medium_words:
        if word in message:
            frustration_score += 10

    # Keep score between 0 and 100
    frustration_score = min(frustration_score, 100)

    # Decide frustration level
    if frustration_score >= 60:
        level = "HIGH"
    elif frustration_score >= 30:
        level = "MEDIUM"
    else:
        level = "LOW"

    return frustration_score, level


if __name__ == "__main__":
    message = "My payment failed and this is terrible."

    score, level = detect_frustration(message)

    print("Frustration Score:", score)
    print("Frustration Level:", level)