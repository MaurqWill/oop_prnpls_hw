class BudgetCategory:
    def __init__(self, category_name, budget):
        self.category_name = category_name
        self.budget = budget
        self.expenses = 0

    # Constructor and private attributes
    # ...

    # Getters and setters for category name and budget
    # ...
    def get_category_name(self):
        return self.category_name
    
    def get_budget(self):
        return self.budget
    
    def set_category_name(self, category_name):
        if type(category_name) == str:
            self.category_name = category_name
        else:
            print("Invalid input")

    def set_budget(self, budget):
        if budget > 0:
            self.budget = budget
        else:
            print("It should be a positive number.")

    def add_expense(self, amount):
        if amount < 0:
            print("Invalid expense amount. Please provide a positive number.")
            return
        
        if amount > self.budget:
            print("Expense amount exceeds the budget. Unable to add expense.")
            return

        self.expenses += amount
        self.budget -= amount
        print(f"Expense of ${amount} added to {self.category_name}. Remaining budget: ${self.budget}")

    def display_category_summary(self):
        print(f"Category: {self.category_name}")
        print(f"Budget: ${self.budget}")
        print(f"Expenses: ${self.expenses}")

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()

# deduct expenses from the budget
# do inside the add expense 
# check if the expense amount is lower than the budget to validAte
# if not raise error
# make a copy of the budget for the original and for after the expenses deductions
# print everything



