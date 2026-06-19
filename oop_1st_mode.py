class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.wallet = 0
        self.orders = []

    def charge_wallet(self, amount):
        self.wallet += amount

    def buy_food(self, restaurant, food_name):
        for food in restaurant.menu:
            if food.name == food_name:
                if self.wallet >= food.price:
                    self.wallet -= food.price
                    self.orders.append(food)
                    print(f"Bought {food_name}")
                    return
                else:
                    print("Charge your wallet first")
                    return
        print(f"{food_name} is not available in the menu")

    def show_wallet(self):
        print(f"Wallet balance: {self.wallet}")

    def show_orders(self):
        if self.orders:
            print("My orders:")
            for order in self.orders:
                print(order.name)
        else:
            print("No orders yet")


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def add_restaurant(self, system, name, address, level):
        system.restaurants[name] = Restaurant(name, address, level)

    def add_food(self, restaurant_name, food_name, price):
        if restaurant_name in system.restaurants:
            system.restaurants[restaurant_name].add_food(food_name, price)
        else:
            print("The restaurant is not in the system")


class Restaurant:
    def __init__(self, name, address, level):
        self.name = name
        self.address = address
        self.level = level
        self.menu = []

    def add_food(self, name, price):
        self.menu.append(Food(name, price))

    def show_menu(self):
        if self.menu:
            print(f"Menu for {self.name}:")
            for food in self.menu:
                print(f"{food.name} - {food.price}$")
        else:
            print("Menu is empty")


class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class System:
    def __init__(self):
        self.users = {}
        self.restaurants = {}
        self.admin = Admin("Jack", "83672")
        self.current_user = None

    def sign_up(self, username, password):
        if username in self.users:
            print("User already exists")
        else:
            self.users[username] = User(username, password)
            print("Sign up successful")

    def login(self, user_type, username, password):
        if user_type == "admin":
            if username == self.admin.username and password == self.admin.password:
                self.current_user = self.admin
                print("Admin logged in")
            else:
                print("The password is wrong")
        elif user_type == "user":
            if username in self.users and self.users[username].password == password:
                self.current_user = self.users[username]
                print("User logged in")
            else:
                print("The password is wrong or user is not available")

    def logout(self):
        self.current_user = None
        print("Logged out")


system = System()

system.admin.add_restaurant(system, "Luxurious", "123 Main St", "luxury")
system.admin.add_food("Luxurious", "Steak", 50)
system.admin.add_food("Luxurious", "Salad", 20)
system.sign_up("john", "12345")
system.login("user", "john", "12345")
system.current_user.charge_wallet(100)
system.current_user.buy_food(system.restaurants["Luxurious"], "Steak")
system.current_user.show_wallet()
system.current_user.show_orders()
