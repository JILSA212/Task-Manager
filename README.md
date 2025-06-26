=======================================
✅ Task Manager (CLI) - Beginner Python Project
=======================================

A clean and user-friendly command-line Task Manager built with Python. It allows users to manage tasks by adding categories, setting priorities, assigning due dates, and marking them as complete. All data is saved in a JSON file, and the interface uses colorama for better visual organization in the terminal.

-------------------
🔧 Features
-------------------
- Add new tasks with name, category, priority (1–5), due date, and description
- Mark tasks as complete or incomplete
- Delete tasks by name
- View all saved tasks in a colorful, readable format
- Tasks are stored persistently in a JSON file
- Built using Object-Oriented Programming (OOP) principles
- Terminal styling with the colorama library

-------------------
🧠 What I Learned
-------------------
- How to use classes and organize code using OOP
- How to read from and write to JSON files for persistent storage
- How to work with dates using the datetime module
- Using colorama to improve terminal output and user experience
- Managing a virtual environment for project dependencies

-------------------
🚀 How to Run
-------------------
1. Clone the repository:
   git clone https://github.com/Iceycoast/task-manager.git

2. Navigate into the project folder:
   cd task-manager

3. Set up a virtual environment:
   python -m venv venv

4. Activate the environment:
   - On Windows: venv\Scripts\activate
   - On Mac/Linux: source venv/bin/activate

5. Install dependencies:
   pip install colorama

6. Run the script:
   python task_manager.py

-------------------
📁 File Structure
-------------------
- task_manager.py        # Main Python script
- tasks.json             # File where all task data is saved (auto-created if not present)
- venv/                  # Virtual environment folder (optional, not included in version control)

-------------------
✅ Example Use
-------------------
1. Add a task:
   Name: Submit assignment  
   Category: College  
   Priority: 2  
   Due Date: 2025-07-01  
   Description: Final project submission  

2. View tasks:
   => Lists all saved tasks with color-coded priority levels

3. Complete a task:
   => Marks the selected task as completed and updates it in the JSON file

-------------------
🙌 Beginner Friendly
-------------------
This project is perfect for beginners who want to practice Python with real-world logic using classes, file handling, terminal inputs, and virtual environments.

-------------------
👤 Author
-------------------
GitHub: https://github.com/Iceycoast
