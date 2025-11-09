while True:
  age_input = input("What is your age?")

  try:
    age = int(age_input)

    break

  except ValueError:
    print("Not a valid number! Please try again.")

print(f"Next Year age will be {age + 1}.")    
