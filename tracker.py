import sys

def main():
    # welcome message
    print("Welcome to LeetTrack!")

    # command error checking
    if len(sys.argv) < 2:
        print("Please Provide a Command!")
        sys.exit(1)
    
    # common commands
    command = sys.argv[1]

    if command == "add":
        print("Add Problem!")
    elif command == "update":
        print("Update Problem!")
    elif command == "show":
        print("Show Problem Statistics!")
    else:
        print("Please Enter a Valid Command!")

if __name__ == "__main__":
    main()