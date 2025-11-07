task = ["Running" , "Walking" , "Exercising" , "Yoga"]

while True : 
  print("1. Add New Task in the list : ")
  print("2. View all task : ")
  print("3. Exiting program :")

  choice = input("Enter a choice(1-3) : ")

  if choice == "1":
    add = input("What do you want to add ?")
    task.append(add)
    print("Task added.")

  elif choice == "2":
    print("Your Task :")
    for Vtask in task:
      print(f"Task : {Vtask}")

  elif choice == "3":
    print("Goodbye.")
    break

  else :
    print("Invalid choice please enter 1,2 or 3")

          
