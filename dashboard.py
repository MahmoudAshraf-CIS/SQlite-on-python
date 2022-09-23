from pprint import pprint
import inquirer
import projects
import utility

def Start(userID):
    # print("Hi "+ str(userID))
    choices2=[]
    choices2.append("New Project")
    for p in projects.GetProjects(userID):
        choices2.append(p)
    choices2.append("Back")
    
    questions = [
    inquirer.List(
        "action",
        message="Select or create a project !",
        choices=choices2,
    ),
    ]

    answers = inquirer.prompt(questions)
     
    if answers['action'] == "New Project":
        projects.AddNewProject(userID)
        return Start(userID)
    elif answers['action'] == "Back":
        return 0
    else:
        projects.SelectProject(userID,answers['action'])
        return Start(userID)