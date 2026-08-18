from agents.knowledge_agent import search_knowledge


# Test 1
message1 = "How long does delivery take?"

result1 = search_knowledge(message1)

print("\n==============================")
print("TEST 1")
print("==============================")
print("Customer:", message1)
print("Result:", result1)


# Test 2
message2 = "What is your return policy?"

result2 = search_knowledge(message2)

print("\n==============================")
print("TEST 2")
print("==============================")
print("Customer:", message2)
print("Result:", result2)


# Test 3
message3 = "Can I cancel my order?"

result3 = search_knowledge(message3)

print("\n==============================")
print("TEST 3")
print("==============================")
print("Customer:", message3)
print("Result:", result3)


# Test 4
message4 = "I forgot my password."

result4 = search_knowledge(message4)

print("\n==============================")
print("TEST 4")
print("==============================")
print("Customer:", message4)
print("Result:", result4)