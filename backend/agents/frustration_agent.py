def detect_frustration(message):
    """
    Detect the frustration level of a customer message.
    """

    message = message.lower()

    # Strong emotional words
    strong_words = [
        "ridiculous",
        "terrible",
        "worst",
        "useless",
        "angry",
        "furious",
        "unacceptable",
        "hate"
    ]

    # Medium emotional words
    medium_words = [
        "frustrated",
        "annoyed",
        "disappointed",
        "upset"
    ]

    # Problem-related words
    problem_words = [
        "problem",
        "issue",
        "not working",
        "failed",
        "failure"
    ]

    # Words related to delays and waiting
    delay_words = [
        "late",
        "delay",
        "delayed",
        "waiting",
        "still waiting",
        "hasn't arrived",
        "haven't received",
        "not arrived"
    ]

    # Repeated support problems
    repeated_words = [
        "again",
        "already contacted",
        "already told",
        "three times",
        "four times",
        "five times",
        "nobody is helping",
        "no one is helping"
    ]

    score = 0
    reasons = []

    # Strong emotional words
    for word in strong_words:
        if word in message:
            score += 25
            reasons.append(
                f"Strong frustration detected: {word}"
            )

    # Medium emotional words
    for word in medium_words:
        if word in message:
            score += 15
            reasons.append(
                f"Frustration detected: {word}"
            )

    # Problem words
    for word in problem_words:
        if word in message:
            score += 10
            reasons.append(
                f"Customer problem detected: {word}"
            )

    # Delay / waiting words
    for word in delay_words:
        if word in message:
            score += 15
            reasons.append(
                f"Delay or waiting detected: {word}"
            )

    # Repeated support problems
    for phrase in repeated_words:
        if phrase in message:
            score += 20
            reasons.append(
                f"Repeated support problem: {phrase}"
            )

    # Exclamation marks
    if "!" in message:
        score += 5
        reasons.append(
            "Strong punctuation detected"
        )

    # Don't allow score above 100
    score = min(score, 100)

    # Determine level
    if score <= 25:
        level = "LOW"

    elif score <= 50:
        level = "MEDIUM"

    elif score <= 75:
        level = "HIGH"

    else:
        level = "CRITICAL"

    # No frustration indicators
    if not reasons:
        reasons.append(
            "No strong frustration indicators detected"
        )

    return {
        "frustration_score": score,
        "level": level,
        "reasons": reasons
    }