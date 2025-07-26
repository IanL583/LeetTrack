import commands

def main():
    # welcome message with command help
    print("Welcome to LeetTrack!")
    print("Type 'help' to see available commands and type 'exit' to quit the program!\n")

    while True:
        command = input("What command would you like to use? ").strip().lower()

        if command == 'exit':
            print("Program Exited!")
            break
        elif command == 'help':
            print("""
Available Commands:
    add     : Add a new problem
    update  : Update an existing problem
    stats   : Show problem statistics
    show    : Show all problems 
    delete  : Delete a problem
    exit    : Quit the program
            """)

        elif command == 'add':
            title = input("Title: ")
            difficulty = input("Difficulty: ")
            topic = input("Topic: ")
            notes = input("Notes: ")
            commands.add.add_problem(title, difficulty, topic, notes)
        elif command == 'update':
            problem_id = input("Problem ID to update: ")
            status = input("New Status (solved/unsolved): ")
            notes = input("New Notes: ")
            commands.update.update_problem(problem_id, status, notes)
        elif command == 'stats':
            commands.stats.show_stats()
        elif command == 'show':
            topic_filter = input("Enter topic to filter (or press enter to show all): ")
            commands.show.show_problems(topic_filter if topic_filter else None)
        elif command == 'delete':
            problem_id = input("Problem ID to delete: ")
            confirm = input(f"Are you sure you want to delete this problem? (y/n): ")
            if confirm.lower() == 'y':
                commands.delete.delete_problem(problem_id)
            else:
                print("Delete cancelled.")
        else:
            print("Invalid Command. Type 'help' for the available options!\n")

if __name__ == "__main__":
    main()