#def get_positive_input(prompt, allow_zero=True):
    #"""Ask for integer and reject negative values. """

   # try:
        #value =int(input(prompt))
        #if  value <0:
       #     print(f"Error :{prompt.strip()} cannot be negative. Program stopped.")
      #      exit()
     #   return value
    #except ValueError:
      #  print("Error: Please enter a whole number .")
     #   exit()

    # 1. number of days
    #days = get_positive_int("Enter number of days in the week: ")

    # 2. Daily expenses
    #total_expenses = 0
   # for i in range(1, days + 1):
        #expense = get_positive_int(f"Enter expense for Day {i} (in Naira): ")
        # Reject negative expense values
#if expense <0:
         #   print("Error: Expense cannot be negative. ")
          #  exit()
#        total_expenses += expense

   # print(f"\nTotal weekly expenses: N{total_expenses}")

    # 3. Weekly budget
   # budget = get_positive_int("Enter your weekly budget(in Naira): ")

    
# Classify a valid score using a pass mark of 50.

score = float(input("Enter your score: "))

if score >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
