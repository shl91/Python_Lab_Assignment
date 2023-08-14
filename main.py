from simple_chatbot import mapper
from simple_chatbot import greetings

if __name__ == "__main__":
    userName = input("Gita:What should I call you?\n")
    greetings.welcomeText(userName)
    print("(to leave,type thank you.)")

    while True:
        task = input (userName + ':')
        task = task.lower()
        mapper.mapper(task)
        


