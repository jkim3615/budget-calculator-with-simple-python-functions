# Simple Budget Calculator in Python for Beginners
# By Jack Kim
# Budget Calculator that supposed to work even without WiFi or Network

# Calendar


# Monthly Budget

def total_budget():
    n=int(input("Enter your monthly budget:  "))
    if n>0:
        print("Your monthly budget is", n, "krw.")

    # Meal Budget

    x=int(input("Enter your meal budget:  "))
    if x>0 or x<n:
        print("Your meal budget is", x, "krw.")

    # Transportation Budget

    y=int(input("Enter your transportation budget:  "))
    if y>0 or y<n:
        print("Your transportation budget is", y, "krw.")

    # Social Budget

    h=int(input("Enter your social budget:  "))
    if h>0 or h<n:
        print("Your social budget is", h, "krw.")

    # Remaining Budget

    total_budget = n-x-y-h
    txt = "The total budget is {} krw."
    print(txt.format(total_budget))

total_budget()