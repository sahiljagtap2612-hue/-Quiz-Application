print("🎮 Welcome to Quiz Game")

score = 0

# Question 1
print("\n1. Capital of India?")
print("A. Mumbai")
print("B. Delhi")
print("C. Pune")

ans = input("Enter answer: ")

if ans == "B" or ans == "b":
    print("✅ Correct")
    score += 1
else:
    print("❌ Wrong")

# Question 2
print("\n2. Which language are you learning?")
print("A. Python")
print("B. HTML")
print("C. CSS")

ans = input("Enter answer: ")

if ans == "A" or ans == "a":
    print("✅ Correct")
    score += 1
else:
    print("❌ Wrong")

# Final Score
print("\n🎯 Final Score =", score)