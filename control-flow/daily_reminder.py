while True:
    task = input("Enter your task: ")
    Priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    # Match priority to set PriorityMsg
    match Priority:
        case "low":
            PriorityMsg = f"{task} is a low priority task. Consider completing it when you have free time."
        case "high":
            reminder = f"{task} is a high priority task that requires immediate attention today!"
            PriorityMsg = reminder
        case "medium":
            PriorityMsg = f"{task} is a medium priority task."

    # Check conditions and print reminder/note accordingly
    if time_bound == "yes" and Priority == "high":
        print("Reminder: ", reminder)
    elif time_bound == "no" and Priority == "low":
        print(f"Note: {PriorityMsg}")
    # Ask user if they want to continue
    choice = input("Do you want to enter another task? (yes/no): ")
    if choice.lower() != "yes":
        break  # Exit loop if user does not want to continue