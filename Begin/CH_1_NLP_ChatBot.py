from textblob import TextBlob

class ChatBot:
    def __init__(self):
        self.sentiment_analyzer = TextBlob("")
        self.negative_keywords = {
            "hurt", "pain", "sad", "angry", "depressed", "anxious",
            "frustrated", "crying", "suffering", "terrible"
        }
        self.positive_keywords = {
            "happy", "joy", "excited", "love", "grateful", "amazing",
            "fantastic", "awesome", "great", "wonderful"
        }

    def start_chat(self):
        print("ChatBot: Hi, how can I help you?")
        while True:
            user_message = input("You: ").strip()
            if not user_message:
                print("ChatBot: Please say something.")
                continue
            if user_message.lower() in {"bye", "exit", "quit"}:
                print("ChatBot: Goodbye! Take care!")
                break

            self.sentiment_analyzer = TextBlob(user_message)
            sentiment_score = self.sentiment_analyzer.sentiment.polarity

            lower_message = user_message.lower()
            if any(w in lower_message for w in self.negative_keywords):
                sentiment_score = -1.0
            elif any(w in lower_message for w in self.positive_keywords):
                sentiment_score = 1.0

            if sentiment_score > 0.10:
                chatbot_message = f"ChatBot: That's great to hear! 😊\nSentiment score: {sentiment_score}\n"
            elif sentiment_score < -0.10:
                chatbot_message = f"ChatBot: I'm sorry to hear that. What can I do to help? 😔\nSentiment score: {sentiment_score}\n"
            else:
                chatbot_message = f"ChatBot: Hmm, I see. Tell me more. 😐\nSentiment score: {sentiment_score}\n"

            print(chatbot_message)

if __name__ == "__main__":
    ChatBot().start_chat()
