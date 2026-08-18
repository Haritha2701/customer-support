from agents.trust_agent import calculate_trust_score


# TEST 1
frustration = {
    "frustration_score": 10
}

knowledge = {
    "confidence": 90
}

result = calculate_trust_score(
    frustration,
    knowledge
)

print("TEST 1")
print(result)


# TEST 2
frustration = {
    "frustration_score": 75
}

knowledge = {
    "confidence": 30
}

result = calculate_trust_score(
    frustration,
    knowledge
)

print("\nTEST 2")
print(result)
