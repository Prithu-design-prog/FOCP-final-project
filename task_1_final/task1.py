print("BPP Pizza Price Calculator\n==========================")


# Define a function to get valid integer input from the user
def get_input(prompt):
   """Repeatedly prompts the user for input until a valid integer is entered.

   Args:
       prompt (str): The message to display to the user.

   Returns:
       int: The integer value entered by the user.
   """

   while True:
       try:
           # Attempt to convert the input to an integer
           user_input = int(input(prompt))
           # Check for positive integers
           if user_input > 0:
               return user_input
           else:
               print("Please enter a positive integer!")
       except ValueError:
           print("Please enter a number!")

# Define a function to get a yes/no answer from the user, accepting "y" or "n"
def get_yes_no_input(prompt):
   """Repeatedly prompts the user for a yes/no answer until "y" or "n" is entered.

   Args:
       prompt (str): The message to display to the user.

   Returns:
       str: "y" if the user answered yes, "n" if the user answered no.
   """

   while True:
       user_input = input(prompt).lower()
       if user_input in ["y", "n"]:
           return user_input
       else:
           print('Please answer "y" or "n".')

# Set the base price of a pizza
pizza_price = 12

# Get the number of pizzas ordered
num_pizzas = get_input("How many pizzas would you like to order? ")

# Check for Tuesday discount
is_tuesday = get_yes_no_input("Is it Tuesday? (y or n): ")
if is_tuesday == "y":
   pizza_price *= 0.5  # Apply 50% discount on Tuesdays

# Determine delivery cost based on order size and delivery choice
delivery_required = get_yes_no_input("Is delivery required? (y or n): ")
delivery_cost = 0 if delivery_required == "n" else 2.5 if num_pizzas < 5 else 0

# Apply app discount if applicable
used_app = get_yes_no_input("Did the customer use the app? (y or n): ")
app_discount = 0.75 if used_app == "y" else 1.0

# Calculate the total cost
total_cost = num_pizzas * pizza_price * app_discount + delivery_cost

# Print the final cost
print("Total Price: £{:.2f}.".format(total_cost))
