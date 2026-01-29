members = [
    {"name": "Alice", "days_left": 5},
    {"name": "maryann", "days left": 0},
    {"name": "Austin", "days_left": 15},
]
def renew_membership(name):
    for m in members:
        if m["name"].lower() == name.lower():
           m["days_left"] += 30
           print(f"{m['name']} renewed. Days left {m['days_left']}")
           return
        print("member not found!")
member_name = input("Enter the name of the member to be renew:")
renew_membership(member_name)