#cs3130 Lab Assignment 2
#Janelle Montgomery
#Reading and writing from an employee database
#Database interaction 



def create_dictionary():
    d = {}
    f=open("database.txt","r")
    for rec in f:
        rec=rec.strip()
        ID,rest = rec.split(":",1)
        d[ID]=rest.split(":",2)
    return d

def db_add():
    d = create_dictionary()
    user = [];
    correct = False
    while not correct:
        print("Enter a 4 digit employee ID:")
        user_id = input()
        
        
        if user_id in d:
            print("This user already exists please try again.")
            print("\n")
            
            
        elif len(user_id) > 5:
            print("The length of this Employee ID is too long. Please retry.")
            print("\n")
        
        
        else:
            correct = True
            print("Enter employees first name:")
            user_first = input()
            user.append(user_first)

            print("Enter employees last name:")
            user_last = input()
            user.append(user_last)

            print("Enter the employees department:")
            user_dep = input()
            user.append(user_dep)

            d[user_id] = user

    with open("database.txt", "w+")as f:
        for k,v in d.items():
            f.write(k + ":" + ":".join(v) + "\n")
        #only saves one at a time

        #fixed with while not correct loop
        
    
def db_search():
    d = create_dictionary()
    print("Please enter an Employee ID:")
    user_id = input()
    if user_id in d.keys():
        print("\n")
        print("ID: " + user_id +"\n" + "Name: " + d[user_id][0] +" "+d[user_id][1] +"\n" + "Department: " + d[user_id][2] +"\n")
    else:
        print("Not a valid Employee ID.")

    print("Would you like to search for another employee? Y/N")
    choice = False
    while choice == False:
        answer = input()
        print("\n")
        if answer in['y','n','Y','N']:
            choice = True
        else:
            print("Invalid input.") 
            choice = False
            
           
    if answer in ['y','Y']:
        db_search()

    

    
def db_remove():
    d = create_dictionary()
    print("Enter Employee ID you would like to remove:")
    user_id = input()
    if not user_id in d.keys():
        print("Not a valid Employee ID.")
        print("\n")
        db_remove()
    else:
        print("Removed: ")
        print("ID: " + user_id +"\n" + "Name: " + d[user_id][0] +" "+d[user_id][1] +"\n" + "Department: " + d[user_id][2] +"\n")
        del d[user_id]
        with open("database.txt", "w+")as f:
            for k,v in d.items():
                f.write(k + ":" + ":".join(v) + "\n")
        f.close()
        
def db_display():
    d = create_dictionary()
    for k in d.keys():
        print("ID: " + k +"\n" + "Name: " + d[k][0] +" "+d[k][1] +"\n" + "Department: " + d[k][2] +"\n")
    
         
def db_quit():
    exit(0)
