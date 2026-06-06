# Exception Handling in Python

# This code demonstrates how to handle exceptions in Python using try-except blocks.

try:
    # Code that might raise an exception
    x = 10 / 0

    if x < 0:
        raise ValueError("Negative value is not allowed.")

    else:
    # Execute if no exception occurred
        print("No exceptions occurred.")

except ZeroDivisionError as e:
    # Handle division by zero error
    print(f"Error: {e}")

finally:
    # Execute regardless of whether an exception occurred
    print("Execution completed.")