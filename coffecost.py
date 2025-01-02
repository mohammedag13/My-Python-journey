"""
This is a progam that calculates the cost of a coffee order
"""
def price():

    the_number_of_orders = int(input("Enter how many coffes you want to order: ")) #This line of code asks the user how many coffee he would like to order.

    cost_of_one_order = 10.80 + 0.86 + 1.50

    the_full_price = cost_of_one_order * the_number_of_orders

    print(f"The full price of the orders you made is: {the_full_price}")

price()