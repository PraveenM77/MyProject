import sys

class Order_Food:
    food = {"Pizza": 200, "Burger": 150, "Pasta": 300, "Cakes": 250}

    def __init__(self):
        print("Food available in PM Bhavan")
        for k, v in self.food.items():
            print(f"{k}   = Rs.{v}")

    def check(self):
        global total_amount
        ur_choice = int(input("""Enter Your Choice
                                1. Pizza
                                2. Burger
                                3. Pasta
                                4. Cakes
                                : """))
        if ur_choice in range(1, 5):
            ur_qty = int(input("Enter qty: "))
            if ur_choice == 1:
                total_amount += ur_qty * self.food["Pizza"]
                print("Order Placed successfully. Total Amount of Pizza is", ur_qty * self.food["Pizza"])
            elif ur_choice == 2:
                total_amount += ur_qty * self.food["Burger"]
                print("Order Placed successfully. Total Amount of Burger is", ur_qty * self.food["Burger"])
            elif ur_choice == 3:
                total_amount += ur_qty * self.food["Pasta"]
                print("Order Placed successfully. Total Amount of Pasta is", ur_qty * self.food["Pasta"])
            elif ur_choice == 4:
                total_amount += ur_qty * self.food["Cakes"]
                print("Order Placed successfully. Total Amount of Cakes is", ur_qty * self.food["Cakes"])

            wantToContinue = input("Do you want to continue? (Yes/No): ").strip().lower()
            if wantToContinue != "yes":
                print("Total amount:", total_amount)
                sys.exit(0)
        else:
            print("Invalid choice!")
            sys.exit(0)

total_amount = 0
o = Order_Food()
while True:
    o.check()
