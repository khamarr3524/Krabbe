# Testing wrapper for the Krabbe engine

import Krabbe

krabbe = Krabbe.Krabbe()

# Test the get_input method
print("Testing get_input method")
print(krabbe.get_input("Enter something: "))
print()

# Test the get_input_int method
print("Testing get_input_int method")
print(krabbe.get_input_int("Enter an integer: "))
print()

# Test the get_input_float method
print("Testing get_input_float method")
print(krabbe.get_input_float("Enter a float: "))
print()

# Test the get_input_bool method
print("Testing get_input_bool method")
print(krabbe.get_input_bool("Enter a boolean: "))
print()

# Test the get_input_list method
print("Testing get_input_list method")
print(krabbe.get_input_list("Enter a list item: ", ["yes", "no", "maybe"]))
print()

# Test the print_text method
print("Testing print_text method")
krabbe.print_text("This is a test of the print_text method.")
print()

# Test the print_text_centered method
print("Testing print_text_centered method")
krabbe.print_text_centered("This is a test of the print_text_centered method.")
print()

# Test the print_text_wrapped method
print("Testing print_text_wrapped method")
krabbe.print_text_wrapped("This is a test of the print_text_wrapped method.")
print()

# Test the print_text_wrapped_centered method
print("Testing print_text_wrapped_centered method")
krabbe.print_text_wrapped_centered("This is a test of the print_text_wrapped_centered method.")
print()

# Test the print_text_wrapped_centered_with_border method
print("Testing print_text_wrapped_centered_with_border method")
krabbe.print_text_wrapped_centered_with_border("This is a test of the print_text_wrapped_centered_with_border method.")
print()

# Test the print_text_wrapped_with_border method
print("Testing print_text_wrapped_with_border method")
krabbe.print_text_wrapped_with_border("This is a test of the print_text_wrapped_with_border method.")
print()