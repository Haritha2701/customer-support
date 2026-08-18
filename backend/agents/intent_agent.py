def detect_intent(customer_message):
    message = customer_message.lower()

    if "payment" in message or "paid" in message or "charge" in message:
        return "PAYMENT_PROBLEM"

    elif "refund" in message or "money back" in message:
        return "REFUND"

    elif "cancel" in message or "cancellation" in message:
        return "CANCELLATION"

    elif "order" in message or "delivery" in message or "where is" in message:
        return "ORDER_STATUS"

    elif "error" in message or "not working" in message or "problem" in message:
        return "TECHNICAL_PROBLEM"

    else:
        return "GENERAL_QUERY"


if __name__ == "__main__":
    result = detect_intent("My payment failed.")
    print("Customer Intent:", result)