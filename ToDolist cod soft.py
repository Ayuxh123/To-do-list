#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#program for codsoft, project : To-Do list
todo_list = []


def add_task():
    task = input("Enter a new task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"Added '{task}' to the to-do list.")

def complete_task():
    for i, item in enumerate(todo_list):
        if not item["completed"]:
            print(f"{i+1}. {item['task']}")
    index = int(input("Enter the number of the task you want to mark as complete: "))
    if 1 <= index <= len(todo_list):
        todo_list[index-1]["completed"] = True
        print(f"Marked '{todo_list[index-1]['task']}' as complete.")
    else:
        print("Invalid task number.")

def view_tasks():
    print("To-Do List:")
    for i, item in enumerate(todo_list):
        status = "✓" if item["completed"] else "✗"
        print(f"{i+1}. {status} {item['task']}")


while True:
    print("\nWhat would you like to do?")
    print("1. Add a new task")
    print("2. Mark a task as complete")
    print("3. View the to-do list")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        complete_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


# In[ ]:





# In[ ]:




