from agents.frustration_agent import detect_frustration
from agents.knowledge_agent import search_knowledge
from agents.resolution_agent import generate_response


# Customer message
message = "My order is late and I am very disappointed!"


# Step 1: Detect frustration
frustration_result = detect_frustration(message)


# Step 2: Search knowledge base
knowledge_result = search_knowledge(message)


# Step 3: Generate final response
response = generate_response(
    message,
    frustration_result,
    knowledge_result
)


print("\n===================================")
print("CUSTOMER SUPPORT SYSTEM")
print("===================================")

print("\nCustomer Message:")
print(message)

print("\nFrustration Result:")
print(frustration_result)

print("\nKnowledge Result:")
print(knowledge_result)

print("\nAI RESPONSE:")
print(response)