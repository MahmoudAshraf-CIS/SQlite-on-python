import datetime
import re

def inputEmail(msg):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email=""
    while not re.fullmatch(regex, email):
        email=input(msg)
    return email

def inputString(msg):
    
    s=""
    while not s.strip():
        s=input(msg)
    return s
def inputDate(msg):
    print("\tEnter Date in DD-MM-YYY format")
    date_string = input(msg)
    format = '%d-%m-%Y'
    try:
        datetime.datetime.strptime(date_string, format)
        return date_string
    except ValueError:
        print("\tThis is the incorrect date string format. It should be DD-MM-YYY")
        return inputDate(msg)


def inputInteger(msg):
    integer = input(msg)
    try:
        integer = int(integer)
        return integer
    except ValueError:
        print('The provided value is not an integer')
        return inputInteger(msg)