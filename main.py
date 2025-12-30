print("Welcome to expense tracker")

salary = float(input("enter your salary: "))
food_percent = float(input("enter the percentaage you would like to spend for your food: "))
shopping_percent = float(input("enter the percentaage you would like to spend for your shopping: "))
saving_percent = float(input("enter the percentaage you would like to spend for your saving: "))
transport_percent = float(input("enter the percentaage you would like to spend for your transport: "))
healthcare_percent = float(input("enter the percentaage you would like to spend for your healthcare: "))
housing_and_rent_percent = float(input("enter the percentaage you would like to spend for your housing_and_rent: "))
utilities_and_bills_percent = float(input("enter the percentaage you would like to spend for your utilities_and_bills: "))

print("salary: ",salary)
print("food_percent: ",food_percent)
print("shopping_percent: ",shopping_percent)
print("saving_percent: ",saving_percent)
print("transport_percent: ",transport_percent)
print("healthcare_percent: ",healthcare_percent)
print("housing_and_rent_percent: ",housing_and_rent_percent)
print("utilities_and_bills_percent: ",utilities_and_bills_percent)

categories = {
    "Food": food_percent,
    "Shopping": shopping_percent,
    "Savings": saving_percent,
    "Transport": transport_percent,
    "Healthcare": healthcare_percent,
    "Housing & Rent": housing_and_rent_percent,
    "Utilities & Bills": utilities_and_bills_percent
}

print("\nBudget Comparison Report")

for category, percent in categories.items():
    limit = salary * percent / 100
    spent = float(input(f"Enter amount spent on {category}: "))

    if limit > spent:
        print(f"{category}: Hurray!! you are spending in the budget!!")
    elif spent == limit:
        print(f"{category}: you are on a verge!!")
    else:
        print(f"{category}: Caution!! Over budget")
        print(f"Allowed: {limit}")
        print(f"Spent: {spent}")


