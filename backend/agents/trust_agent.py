def calculate_trust_score(frustration_result, knowledge_result):
    """
    Calculate the trust score and decide
    whether human support is required.
    """

    # Get knowledge confidence
    knowledge_confidence = knowledge_result.get(
        "confidence",
        0
    )

    # Get frustration score
    frustration_score = frustration_result.get(
        "frustration_score",
        0
    )

    # Start with knowledge confidence
    trust_score = knowledge_confidence

    # Reduce trust when frustration is high
    if frustration_score >= 70:

        trust_score -= 20

    elif frustration_score >= 40:

        trust_score -= 10

    # Keep score between 0 and 100
    trust_score = max(
        0,
        min(trust_score, 100)
    )

    # Decide trust level
    if trust_score >= 70:

        trust_level = "HIGH"

    elif trust_score >= 40:

        trust_level = "MEDIUM"

    else:

        trust_level = "LOW"


    # -----------------------------------
    # HUMAN ESCALATION
    # -----------------------------------

    if (
        frustration_score >= 70
        and trust_score < 40
    ):

        escalation_required = True

        escalation_reason = (
            "Customer frustration is high "
            "and AI confidence is low."
        )

    elif frustration_score >= 70:

        escalation_required = True

        escalation_reason = (
            "Customer frustration is very high."
        )

    elif trust_score < 20:

        escalation_required = True

        escalation_reason = (
            "AI confidence is very low."
        )

    else:

        escalation_required = False

        escalation_reason = (
            "AI can continue handling the request."
        )


    return {
        "trust_score": trust_score,
        "trust_level": trust_level,
        "escalation_required": escalation_required,
        "escalation_reason": escalation_reason
    }

