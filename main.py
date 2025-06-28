import json
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)

class Task:
    def __init__(self, name, category, priority, due_date, description, completed=False):
        self.name = name 
        self.category = category
        self.priority = priority
        self.due_date = due_date
        self.completed = completed
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "priority": self.priority,
            "due_date": self.due_date,
            "completed": self.completed,
            "description": self.description
        }

class Task_manager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def add_task(self, name, category, priority, due_date, description):
        task = Task(name, category, priority, due_date, description).to_dict()
        try:
            with open(self.filename, 'r') as f:
                tasks = json.load(f)
                tasks.append(task)
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = [task]
        with open(self.filename, 'w') as f:
            json.dump(tasks, f, indent=4)

    def view_all_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                tasks = []
                for item in data:
                    status = f"{Fore.GREEN}✅" if item["completed"] else f"{Fore.RED}❌"
                    task = (
                        f"\n{Fore.CYAN}Task: {item['name']}\n"
                        f"Category: {item['category']}\n"
                        f"Priority: {item['priority']}\n"
                        f"Due Date: {item['due_date']}\n"
                        f"Completed: {status}\n"
                        f"Description: {item['description']}\n"
                    )
                    tasks.append(task)
                return "\n".join(tasks) if tasks else f"{Fore.YELLOW}No Tasks Found"
        except (FileNotFoundError, json.JSONDecodeError):
            return f"{Fore.RED}No tasks found."

    def category_filter(self):
        user = input(f"{Fore.CYAN}Enter the Category of the Task You want to search: ")
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                filter_task = []
                for item in data:
                    if item['category'].lower() == user.lower():
                        task = (
                            f"\n{Fore.CYAN}Task: {item['name']}\n"
                            f"Category: {item['category']}\n"
                            f"Priority: {item['priority']}\n"
                            f"Due Date: {item['due_date']}\n"
                            f"Completed: {item['completed']}\n"
                            f"Description: {item['description']}\n"
                        )
                        filter_task.append(task)
                return "\n".join(filter_task) if filter_task else f"{Fore.YELLOW}No tasks found in this category."
        except (FileNotFoundError, json.JSONDecodeError):
            return f"{Fore.RED}Category Not Found"

    def mark_done(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for index, item in enumerate(data):
                    status = f"{Fore.GREEN}✅" if item["completed"] else f"{Fore.RED}❌"
                    print(f"{Fore.CYAN}{index + 1}. [{status}{Fore.CYAN}] {item['name']}")
                user = int(input(f"{Fore.CYAN}Enter the number of the task to mark as completed: "))
                selected_index = user - 1
                if 0 <= selected_index < len(data):
                    data[selected_index]['completed'] = True
                    print(f"{Fore.GREEN}Task '{data[selected_index]['name']}' marked as completed ✅")
                else:
                    print(f"{Fore.RED}Invalid task number selected.")
                    return
        except (FileNotFoundError, json.JSONDecodeError):
            return f"{Fore.RED}Task not Found"
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
        return f"{Fore.GREEN}The task has been updated successfully."

    def sort_tasks(self):
        user = int(input(f"{Fore.CYAN}Sort by:\n1. Priority\n2. Due Date\nYour choice: "))
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)

                if user == 1:
                    sorted_data = sorted(data, key=lambda x: x['priority'])
                else:
                    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['due_date'], "%Y-%m-%d"))

                sort = []
                for item in sorted_data:
                    status = f"{Fore.GREEN}✅" if item["completed"] else f"{Fore.RED}❌"
                    line = f"[{status}] {item['name']} | Priority: {item['priority']} | Due: {item['due_date']}"
                    sort.append(line)

                return "\n".join(sort) if sort else f"{Fore.YELLOW}No tasks to show"
        except (FileNotFoundError, json.JSONDecodeError):
            return f"{Fore.RED}Task not Found"

def get_required_value(prompt, error_message, validation_func=None):
    while True:
        value = input(prompt)
        if not value.strip():
            print(f"{Fore.RED}{error_message}")
            continue
        if validation_func and not validation_func(value):
            print(f"{Fore.RED}{error_message}")
            continue
        return value
    
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def main():
    manager = Task_manager()

    while True:
        print(f"\n{Fore.MAGENTA + Style.BRIGHT}📋 Task Manager Menu")
        print(f"{Fore.YELLOW}1.{Style.RESET_ALL} ➕ Add Task")
        print(f"{Fore.YELLOW}2.{Style.RESET_ALL} 📄 View All Tasks")
        print(f"{Fore.YELLOW}3.{Style.RESET_ALL} 🔍 Filter by Category")
        print(f"{Fore.YELLOW}4.{Style.RESET_ALL} ✅ Mark Task as Completed")
        print(f"{Fore.YELLOW}5.{Style.RESET_ALL} 📊 Sort Tasks")
        print(f"{Fore.YELLOW}6.{Style.RESET_ALL} ❌ Exit")

        choice = input(f"{Fore.CYAN}Enter your choice (1–6): ")

        if choice == "1":
            # name = input("Task Name: ")
            name = get_required_value(f"{Fore.CYAN}Task Name: ", "Task name is required.")
            # category = input("Category: ")
            category = get_required_value(f"{Fore.CYAN}Category: ", "Category is required.")
            try:
                # priority = int(input("Priority (1–5): "))
                priority = int(get_required_value(f"{Fore.CYAN}Priority (1–5): ", "Priority must be a number and between 1 to 5.", lambda x: x.isdigit() and 1 <= int(x) <= 5))
            except ValueError:
                print(f"{Fore.RED}❌ Priority must be a number.")
                continue
            # due_date = input("Due Date (YYYY-MM-DD): ")
            due_date = get_required_value(f"{Fore.CYAN}Due Date (YYYY-MM-DD): ", "Due date is required in valid format.", lambda x: x.strip() and len(x) == 10 and x[4] == '-' and x[7] == '-' and x[:4].isdigit() and x[5:7].isdigit() and  x[8:].isdigit() and is_valid_date(x))
            description = input("Description (optional): ")
            manager.add_task(name, category, priority, due_date, description)
            print(f"{Fore.GREEN}✅ Task added successfully.")

        elif choice == "2":
            print(manager.view_all_tasks())

        elif choice == "3":
            print(manager.category_filter())

        elif choice == "4":
            print(manager.mark_done())

        elif choice == "5":
            print(manager.sort_tasks())

        elif choice == "6":
            print(f"{Fore.BLUE}👋 Exiting Task Manager. Goodbye!")
            break

        else:
            print(f"{Fore.RED}❌ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
