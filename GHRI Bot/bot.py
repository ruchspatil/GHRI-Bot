# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatbot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend 🤗",
])
trainer.train([
    "Are you there?",
    "Yes, I'm here! How can i help you?",
])
trainer.train([
    "How are you?",
    "I'm good! How can i help you?",
])
trainer.train([
    "Are you a there?",
    "Yes, I'm here! How can i help you?",
])
trainer.train([
    "What is the address of your college?",
    "Address: Khandesh Complex, 91,92, Mohadi Rd, Jalgaon, Maharashtra 425001",
])
trainer.train([
    "Which courses are you offering?",
    "Business Management, Engineering, Computer Application" "You can see more about it on our website:https://ghribmjal.raisoni.net/"
])


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")