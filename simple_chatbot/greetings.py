import random


def welcomeText(userName):
    welcome = [f"Hey {userName}, What would you like to chat about?",
           f"Hello {userName}. Ask me a question.",
           f"How can I help you,{userName}?",
           f"Ask away,{userName}"]
    print('Gita:' + random.choice(welcome))

def farewellText():
    farewell =  ["Goodbye.", 
             "See you again.", 
             "Bye Bye Miss American Pie.", 
             "I don't know why you say goodbye I say hello."]
    print(random.choice(farewell))

    
    
    

    

    