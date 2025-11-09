try:
  age = int(input("Enter your age "))
  print(f"Your age next year : {age + 1}")

except ValueError:
  print("Error: You Must Enter a Whole Number!")