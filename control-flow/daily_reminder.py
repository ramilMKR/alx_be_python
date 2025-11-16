task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        msg = f"'{task}' is a high priority task"
    case "medium":
        msg = f"'{task}' is a medium priority task"
    case "low":
        msg = f"'{task}' is a low priority task"
    case _:
        msg = f"'{task}' has an undefined priority"

if time_bound == "yes":
    msg += " that requires immediate attention today!"
else:
    msg += ". Consider completing it when you have free time."

print("Reminder:", msg)