class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.login_attempts = 0

    def describe_restaurant(self):
        return(f"Restaurant Name: {self.restaurant_name}")
        return(f"Restaurant Cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        return(f"{self.restaurant_name} is Open!")

    def customers_served(self):
        return(f"{restaurant.restaurant_name} has served {self.number_served} customers.")

    def increment_number_served(self, customers):
        self.number_served += customers
        return self.customers_served()

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attemps(self):
        self.login_attempts = 0

class User:
    def __init__(self, first_name, last_name ):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        


restaurant = Restaurant("Sabrina's Cafe", 'Italian')

print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
print(restaurant.customers_served())
restaurant.increment_number_served(5)
restaurant.increment_number_served(100)
print(restaurant.customers_served())
print(res)