import time
import random

Responses = [
    "- Yes", 
    "- No", 
    "- Im not sure", 
    "- Maybe",
    "- Very likely",
    "- Thats unlikely",
    "- Totally!",
    "- Absolutely",
    "- Probably not",
    "- It could be",
    "- Thats a hard question to answer",
    "- I dont know",
    "- I dont have the time for me to answer in full detail",
    "- Who knows",
    "- Could be",
    "- Sounds unlikely",
    "- Hopefully yes",
    "- I cant tell",
    "- Im trying to figure it out",
    "- Definitely"
]

question = input("Hi, im a simpel Bot, enter your question: ")

print("- Thinking...")
time.sleep(1)

answer = random.randint(0, 19)
print(Responses[answer])

a = 2
b = 1

while a > b:

    secondQuestion = input("\nEnter another question or use 'quit' to return: ")

    if secondQuestion == "quit":
        a = 0
    else:
        print("- Thinking...")
        time.sleep(1)

        answer = random.randint(0, 19)
        print(Responses[answer])

