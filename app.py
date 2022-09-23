 
from pprint import pprint
from tkinter import E
from tracemalloc import start
import inquirer
import outh
import dashboard
 
def Start():
    
        
    questions = [
        inquirer.List(
            "action",
            message="Welcom to the Crowd fund dashboard!",
            choices=["Login", "Sign up", "Exit"],
        ),
    ]

    answers = inquirer.prompt(questions)
    if answers['action'] == "Login":
        CurentUserID = outh.login()
        if CurentUserID != "-1":
            dashboard.Start(CurentUserID)
            Start()
        else:
            print("Wrong User name or password!")
            Start() 
    elif answers['action'] == "Sign up":
        outh.signUp()
        Start()
    else:
        return 0
 

Start()