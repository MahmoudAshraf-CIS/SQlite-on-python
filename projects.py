 
from logging import exception
from pickle import TRUE
import sqlite3
import utility
import inquirer

conn = sqlite3.connect('test.db')
# conn.execute('drop table PROJECT')
conn.execute('''CREATE TABLE IF NOT EXISTS PROJECT
         (ID INTEGER PRIMARY KEY,
         TITLE           TEXT    NOT NULL,
         DETAILS          TEXT    NOT NULL,
         TOTAL_TARGET     TEXT    NOT NULL,
         START_DATE        DATE,
         END_DATE          DATE,
         USER_ID    INTEGER NOT NULL,
         FOREIGN KEY (USER_ID)
            REFERENCES USER (ID) 
         );''')

conn.close()

def GetProjects(userID):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute("SELECT TITLE FROM PROJECT WHERE USER_ID='"+ str(userID) +"'")

    rows = cur.fetchall()
    projects=[]
    for row in rows:
        projects.append(row[0])

    return projects

def AddNewProject(userID):
    print("AddNewProject ----------")
    conn = sqlite3.connect('test.db')
    query = """
     INSERT INTO PROJECT (TITLE,DETAILS,TOTAL_TARGET,START_DATE,END_DATE,USER_ID) 
     VALUES
          (?,?,?,?,?,?)
        """
    
    TITLE=utility.inputString("Title : ")
    DETAILS=utility.inputString("Details : ")
    TOTAL_TARGET=utility.inputInteger("Target : ")
    START_DATE=utility.inputDate("Start Date : ")
    
    END_DATE=utility.inputDate("End Date : ")

    data =  [TITLE,DETAILS,TOTAL_TARGET,START_DATE,END_DATE,userID]
    try:
        conn.execute(query,data);
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError as e:
        print('\033[91m' + str(e) + '\033[0m')
        return AddNewProject()

def PrintProject(userID,projectTitle):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute("SELECT TITLE,DETAILS,TOTAL_TARGET,START_DATE,END_DATE FROM PROJECT WHERE USER_ID='"+ str(userID) +"' AND TITLE='" + str(projectTitle) + "'")

    rows = cur.fetchall()
    projects=[]
    for row in rows:
        print("Title : "+ row[0])
        print("Details : "+ row[1])
        print("Target : "+ row[2])
        print("Start : "+ row[3])
        print("End : "+ row[4])
        
def DeleteProject(userID,projectTitle):
    questions = [
    inquirer.List(
        "action",
        message="Confirm Deleting "+str(projectTitle) + " project ? ",
        choices=["Yes","No"],
    ),
    ]

    answers = inquirer.prompt(questions)
     
    if answers['action'] == "Yes":
        
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM PROJECT WHERE USER_ID='"+ str(userID) +"' AND TITLE='" + str(projectTitle) + "'")
        conn.commit()
        conn.close()
        return 1
    else:
        return 0

def UpdateProject(userID,projectTitle):
    print("update project " + str(projectTitle) + "userid = "+ str(userID) )
     
    conn = sqlite3.connect('test.db')
    query = """
     UPDATE PROJECT 
     SET TITLE = ?,
        DETAILS = ?,
        TOTAL_TARGET = ?,
        START_DATE = ?,
        END_DATE = ?
          
    WHERE USER_ID = ? AND
    TITLE = ?
        """
    
    TITLE=utility.inputString("Title : ")
    DETAILS=utility.inputString("Details : ")
    TOTAL_TARGET=utility.inputInteger("Target : ")
    START_DATE=utility.inputDate("Start Date : ")
    
    END_DATE=utility.inputDate("End Date : ")

    data =  [TITLE,DETAILS,TOTAL_TARGET,START_DATE,END_DATE,userID,projectTitle]
    try:
        conn.execute(query,data)
        conn.commit()
        conn.close()
        return 0
    except exception as e:
        print('\033[91m' + str(e) + '\033[0m')
        return UpdateProject(userID,projectTitle)

 
    



def SelectProject(userID,projectTitle):
    print("project "+ str(projectTitle) + " of user " + str(userID)+ " is selcted")
    
    PrintProject(userID, projectTitle)
    
    
    questions = [
    inquirer.List(
        "action",
        message="Select or create a project !",
        choices=["Delete","Edit","Back"],
    ),
    ]

    answers = inquirer.prompt(questions)
     
    if answers['action'] == "Delete":
        return DeleteProject(userID,projectTitle)
    elif answers['action'] == "Back":
        return 0
    else:
        return UpdateProject(userID,projectTitle)
    
 