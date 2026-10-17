import random
import re
from datetime import datetime


class Chatbot:
    """A lightweight rule-based chatbot for simple conversations."""

    def __init__(self, name: str = "KhibraBot"):
        self.name = name

    def respond(self, message: str) -> str:
        text = (message or "").strip()
        if not text:
            return "I didn't catch that. Please ask me something else."

        normalized = text.lower()

        if any(word in normalized for word in ["hello", "hi", "hey", "bonjour"]):
            return f"Hello! I'm {self.name}. How can I help you today?"

        if any(word in normalized for word in ["your name", "who are you", "what is your name"]):
            return f"My name is {self.name}. I am a simple AI assistant."

        if any(word in normalized for word in ["how are you", "how are u"]):
            return "I'm doing well, thank you. I'm here to help you."

        if any(word in normalized for word in ["time", "date", "today"]):
            now = datetime.now()
            return f"The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}."

        if any(word in normalized for word in ["help", "commands", "what can you do"]):
            return (
                "I can greet you, tell you the time, do simple math, "
                "tell jokes, and answer basic questions."
            )

        if any(word in normalized for word in ["bye", "goodbye", "see you", "exit", "quit"]):
            return "Goodbye! It was nice chatting with you."

        if any(word in normalized for word in ["joke", "funny"]):
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs.",
                "I told my computer I needed a break, and now it sends me to sleep mode.",
                "Why was the JavaScript developer sad? Because they didn't know how to 'null' their feelings.",
            ]
            return random.choice(jokes)

        math_match = re.search(r"(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)", normalized)
        if math_match:
            left = float(math_match.group(1))
            operator = math_match.group(2)
            right = float(math_match.group(3))
            if operator == "+":
                result = left + right
            elif operator == "-":
                result = left - right
            elif operator == "*":
                result = right * left
            elif operator == "/":
                if right == 0:
                    return "I can't divide by zero."
                result = left / right
            else:
                result = None

            if result is not None:
                if result.is_integer():
                    result = int(result)
                return f"The result is {result}."

        if any(word in normalized for word in ["thanks", "thank you"]):
            return "You are welcome! How can I help you further?"

        if any(word in normalized for word in ["who", "what", "when", "where", "why", "how"]):
            return "I can answer basic questions, help with simple tasks, and have a short conversation."

        return (
            "I'm still learning, but I can help with greetings, time, simple math, "
            "and general conversation. Ask me something else."
        )


def main() -> None:
    chatbot = Chatbot()
    print(f"Welcome! I'm {chatbot.name}. Type 'exit' or 'quit' to leave.")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"exit", "quit", "bye", "goodbye"}:
            print(chatbot.respond(user_input))
            break

        print(f"{chatbot.name}: {chatbot.respond(user_input)}")


if __name__ == "__main__":
    main()
