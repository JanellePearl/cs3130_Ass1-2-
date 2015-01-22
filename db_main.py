#cs3130 Lab Assignment 2
#Janelle Montgomery
#Reading and writing from an employee database
#Main program

import db_interaction


def display_menu():
    print("--")
    print("Employee FMS\n")
    print("Select one of the following:\n")
    print("1) Add a new employee")
    print("2) Search for an employee")
    print("3) Remove an employee from FMS")
    print("4) Display entire employee FMS")
    print("5) Quit\n")
    print("Option?\n")
    print("--\n")

def get_option():
    try:
        selection = int(input())
        print("\n")
        
    except ValueError:
        print("You must input a number.")
        return -1
    
    except Exception:
        print("Please enter a valid number.")
        return -1

    if not selection in range(1,6):
        print("Your choice must be in the range of 1 to 6")

    return selection

def main():
    while True:
        display_menu()
        selection = -1
        while selection == -1:
            selection = get_option()
            if selection == 1:
                db_interaction.db_add()
            elif selection == 2:
                db_interaction.db_search()
            elif selection == 3:
                db_interaction.db_remove()
            elif selection == 4:
                db_interaction.db_display()
            elif selection == 5:
                db_interaction.db_quit()
            else:
                selection = -1

    
if __name__ == "__main__":
    main()
                

    
        
        


    




