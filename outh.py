
from pickle import TRUE
import sqlite3
from traceback import print_tb
import utility

 
conn = sqlite3.connect('test.db')
# conn.execute("drop table USER")
conn.execute('''CREATE TABLE IF NOT EXISTS USER
         (ID INTEGER PRIMARY KEY,
         F_NAME           TEXT    NOT NULL,
         L_NAME           TEXT    NOT NULL,
         EMAIL            TEXT    UNIQUE NOT NULL,
         PASSWORD        CHAR(50),
         PHONE          REAL);''')

conn.close()

CurentUserID="-1"

def login():
    
    print("Login ----------")
    conn = sqlite3.connect('test.db')
    EMAIL=utility.inputString("E-mail : ")
    PASSWORD=utility.inputString("Password : ")
    # TODO - encrypt the password or hashing it to compare with the stored (encrypted password)
     
    cursor = conn.execute("SELECT PASSWORD , ID from USER WHERE EMAIL='"+EMAIL+"'")
    

    for row in cursor:
        if row[0] == PASSWORD:
            conn.close()
            CurentUserID=row[1]
            return CurentUserID
    
    return "-1"

def signUp():
    print("Signup ----------")
    conn = sqlite3.connect('test.db')
    query = """
     INSERT INTO USER (F_NAME,L_NAME,EMAIL,PASSWORD,PHONE) 
     VALUES
          (?,?,?,?,?)
        """
    
    F_NAME=utility.inputString("First Name: ")
    L_NAME=utility.inputString("Last Name : ")
    EMAIL=utility.inputEmail("E-mail : ")
    PASSWORD=utility.inputString("Password : ")
    ## TODO -- Encrypt the password before storing it
    PHONE=utility.inputString("Phone : ")

    data =  [F_NAME, L_NAME, EMAIL,PASSWORD, PHONE]
    try:
        conn.execute(query,data)
        conn.commit()    
        conn.close()
        return True
    except sqlite3.IntegrityError as e:
        print('\033[91m' + str(e) + '\033[0m')
        return signUp()
    