# Simple Customer Feedback System

try:
    name = input("Enter your name: ").strip()
    feedback = input("Enter your feedback: ").strip()

    # Check if name or feedback is empty
    if not name or not feedback:
        raise ValueError("Name and feedback cannot be empty!")

except ValueError as e:
    print("Error:", e)

else:
    print("\nThank you for your feedback!")
    print(f"Name: {name}")
    print(f"Feedback: {feedback}")

finally:
    print("\n--- Feedback session ended ---")
