# Python To-Do List CLI

## Overview

This is a beginner Python command-line to-do list application. The program allows users to add tasks, view tasks, mark tasks as complete, delete tasks, and exit the app through a simple menu system.

I built this project to practice Python fundamentals through a small interactive program.

## Features

- Add new tasks
- View all tasks
- Mark tasks as complete
- Delete tasks
- Use a command-line menu
- Handle invalid task numbers
- Store task status as complete or incomplete

## Python Concepts Used

- Functions
- Lists
- Dictionaries
- While loops
- If/elif/else conditionals
- User input
- Error handling with try/except
- Indexing
- Basic CRUD operations:
  - Create tasks
  - Read tasks
  - Update task status
  - Delete tasks

## How It Works

Each task is stored as a dictionary with two values:

```python
{
    "task": "Example task",
    "status": False
}
```
All tasks are stored inside a list called task_list.

The app repeatedly shows a menu until the user chooses to exit.

How to Run

Make sure Python is installed.

Then run:
```python
python todo_list.py
```
Example Usage
To-Do List App
1. Add Task
2. Show Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit

Enter your choice: 1
Enter a new task: Finish Python project
Task 'Finish Python project' is added to the list.

Enter your choice: 2

Your Tasks:
1. Finish Python project - Incomplete

Enter your choice: 3
Enter the task number to mark as complete: 1
Task 'Finish Python project' is marked as complete.

## What I Learned

This project helped me practice breaking a program into functions and managing data with lists and dictionaries. I also practiced using user input, validating task numbers, handling errors, and updating/deleting items from a list.

Future Improvements
- Save tasks to a CSV or text file
- Load saved tasks when the program starts
- Add due dates
- Add task categories
- Add priority levels
