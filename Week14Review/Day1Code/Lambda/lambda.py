def send_some_data(data, response_callback):
    # fancy code to send data here
    response_callback(f"{data} sent successfully")


print("\n---------Lambda Function---------")
# This is what a lambda function looks like
lambda x: x * 2

# assign a lambda expression to a variable, for later use
square_root = lambda x: x ** 0.5
numbers = [square_root(i) for i in [1,2,3,4,5,6]]
print(f"Result (lambda expressions in comprehensions): {numbers}")

# Passing lambda functions as callbacks
address_data = {
    "name": "Meghan",
    "adddress": ("123 street name", "City", "Zipcode", "Province"),
    "phone": "+1-888-777-6666"
}

#send_some_data function behaves differently depending on lambda function passed in
send_some_data(address_data, lambda x: print(x.upper()))
send_some_data(address_data, lambda x: print(x.lower()))