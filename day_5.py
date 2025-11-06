todo_list = ["Playing" , "Reading" , "Studing" , "Running"]
print(todo_list) # Printing the hole list 

print(todo_list[0]) # Prints the first task
print(todo_list[3]) # This prints "Running"

new_task = input("What new task you want to add ?")
todo_list.append(new_task)
print(todo_list)

number = len(todo_list)
print(f"You have now {number} tasks.")
