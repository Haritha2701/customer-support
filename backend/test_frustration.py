from agents.frustration_agent import detect_frustration


# -------------------------------
# TEST 1: Calm customer
# -------------------------------

message1 = "Can you tell me your return policy?"

result1 = detect_frustration(message1)

print("\n==============================")
print("TEST 1")
print("==============================")
print("Customer:", message1)
print("Result:", result1)


# -------------------------------
# TEST 2: Slightly frustrated
# -------------------------------

message2 = "My order is late and I am disappointed."

result2 = detect_frustration(message2)

print("\n==============================")
print("TEST 2")
print("==============================")
print("Customer:", message2)
print("Result:", result2)


# -------------------------------
# TEST 3: Very frustrated
# -------------------------------

message3 = "This is ridiculous! I've contacted you three times!"

result3 = detect_frustration(message3)

print("\n==============================")
print("TEST 3")
print("==============================")
print("Customer:", message3)
print("Result:", result3)


# -------------------------------
# TEST 4: Extremely frustrated
# -------------------------------

message4 = "I am furious! This is unacceptable! Nobody is helping me!"

result4 = detect_frustration(message4)

print("\n==============================")
print("TEST 4")
print("==============================")
print("Customer:", message4)
print("Result:", result4)