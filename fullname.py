def full_name(first_name, last_name):
    """Concatenates first and last names to create a full name,
       handling extra spaces.

    Args:
        first_name: The person's first name.
        last_name: The person's last name.

    Returns:
        The full name as a single string with one space between names.
    """
    first_name = first_name.strip()
    last_name = last_name.strip()
    full_name = f"{first_name} {last_name}"  # Add space between names
    return full_name

# Get user input
first_name = input("Enter your first name please: ")
last_name = input("Enter your last name please: ")

# Print the formatted full name, removing extra spaces in the output
formatted_full_name = full_name(first_name, last_name).replace("  ", " ") #To make sure there are only single spaces
print(f"Your full name is: {formatted_full_name}")