def generate_response(customer_message, frustration_result, knowledge_result):
    """
    Generate a customer support response using:
    1. Customer message
    2. Frustration result
    3. Knowledge base result
    """

    frustration_level = frustration_result["level"]

    knowledge_found = knowledge_result["found"]

    # If we don't have an answer in the knowledge base
    if not knowledge_found:

        if frustration_level in ["HIGH", "CRITICAL"]:
            response = (
                "I'm really sorry that you're experiencing this issue. "
                "I understand how frustrating this can be. "
                "I don't currently have enough information to resolve "
                "this issue, so a support representative should assist you."
            )

        else:
            response = (
                "I'm sorry, but I couldn't find the information needed "
                "to answer your question. A support representative "
                "can help you with this."
            )

        return response

    # Get the answer from the knowledge base
    answer = knowledge_result["answer"]

    # Response for highly frustrated customers
    if frustration_level in ["HIGH", "CRITICAL"]:

        response = (
            "I'm really sorry about this situation. "
            "I understand how frustrating this must be. "
            f"{answer} "
            "If this doesn't resolve your issue, "
            "we can connect you with a support representative."
        )

    # Response for moderately frustrated customers
    elif frustration_level == "MEDIUM":

        response = (
            "I'm sorry you're experiencing this issue. "
            f"{answer} "
            "I hope this helps resolve the problem."
        )

    # Response for calm customers
    else:

        response = (
            f"{answer} "
            "Please let me know if you need any further assistance."
        )

    return response