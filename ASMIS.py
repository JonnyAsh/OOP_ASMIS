# Dependencies
import hashlib
import time




# This function allows for conditions to be set to validate password
def password_check(Password):
      
# Passwprd must be five or more characters
    if len(Password) < 5:
        print('length should be at least 5')
        val = False
# Password must have at least one numeral
    if not any(char.isdigit() for char in Password):
        print('Password should have at least one numeral')
        val = False
# Password must have one uppercase letter        
    if not any(char.isupper() for char in Password):
        print('Password should have at least one uppercase letter')
        val = False
# Password must have one lowercase letter       
    if not any(char.islower() for char in Password):
        print('Password should have at least one lowercase letter')
        val = False        
    if val:
        return val



# start of authentication process
# This function displays a landing page welcoming users to Queens Medical Centre, and gives guidance on next steps to be taken
def Welcome():
    print("Welcome to Queens Medical Centre")
    print("Please choose one of the following to access the appointment and scheduling system")
    # User selects which option they prefer
    print("Select 1 to Register")
    print("Select 2 to Login")
    print()
    # As this is a simple 1/0 logic operator, the boolean returns the value True
    while True:
        print()
        user = input("Input your selection here: ")
        if user in ['1', '2']:
            break
    if user == '1':
        Register()
    else:
        Login()


def Register():
    print("Welcome to Queens Medical centre registration portal")
  
    # User inputs name and password if first time using system
    Username = input("Please input your name: ")
    Password = input("Please input your password:")
    # hashlib constructs password hashing
    hashedpassword = hashlib.sha256(Password.encode()).hexdigest()
    

    # Sets conditons for password validation. If condtion are not met, then user is routed back to landinf page
    if len(Password) < 5:
        print('length should be at least 5')
        val = False   
    if not any(char.isdigit() for char in Password):
        print('Password should have at least one numeral')
        val = False
    if not any(char.isupper() for char in Password):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in Password):
        print('Password should have at least one lowercase letter')
        val = False
# This function opens the text file to add new users' username and hashed password   
    file = open("Patient_database.txt", "r")
# This function compares users' username and password against the registered users'credentials, If already regsitered, output will state ' You are already registered'
    for f in file:
        if Username in f:
            print("You are already registered")
            Welcome()
            return
        
    file.close()
    file = open("Patient_database.txt", "a")
    file.write(Username + "," + hashedpassword)
    file.write(",")
    file.write(hashedpassword)
    file.write("\n")
    file.close()
# if newly registered and no exceptions raised, then output will state 'Your details have been entered'
    print("Your details have been entered")
    Welcome()       
            
    
def Login():
# Welcome message asking for users’ name and password
    print("Welcome to Queens Medical centre login portal")
    Username = input("Please input your name: ")
    Password = input("Please input your password:")
    
    # Starts the hash dependency for password decrypting
    hashedpassword = hashlib.sha256(Password.encode()).hexdigest()
    
# This function opens the text file and compares against the registered users’ credentials.   
    with open ("Patient_database.txt", "r") as file:
        for line in file:
            line = line.strip().split(",")
    if line[0] == Username and line[1] == hashedpassword:
# If the users’ username and password are already registered, then output will state ‘You are now logged in’.                
        print("You are now logged in")
        return True
    print("Sorry, your credentials are incorrect")
# This time dependency has a three second duration before user can take the next step
    time.sleep(3)
# This returns the user to the landing page to restart the process.
    return False
    


Welcome()
Register()
Login()