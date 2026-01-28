
import pandas as pd
import re

data = pd.read_csv("customer_support_conversations.csv")
data = data[data["inbound"] == True]
data = data[["text"]].dropna()

def assign_intent(text):
    text = text.lower()

    if any(word in text for word in ['refund', 'money back', 'return']):
        return 'refund'

    elif any(word in text for word in ['late', 'delay', 'not delivered']):
        return 'delivery_issue'

    elif any(word in text for word in ['cancel', 'stop order']):
        return 'cancellation'

    elif any(word in text for word in ['payment', 'charged', 'card']):
        return 'payment_issue'

    elif any(word in text for word in ['track', 'tracking', 'where is']):
        return 'tracking'

    else:
        return 'support'

data["intent"] = data["text"].apply(assign_intent)
print("Labeled Dataset:")
print(data)

def chatbot(user_input):
    return assign_intent(user_input)

print("\n--- Customer Support Chatbot ---")
print("Type 'exit' to stop\n")

while True:
    user = input("User: ")
    if user.lower() == "exit":
        print("Chat ended.")
        break
    print("Bot Intent:", chatbot(user))
