def calculate_due_amount(total_bill, amount_paid):
    """
    Calculates the customer's due amount or change after a bill payment.

    Args:
        total_bill (float): The total bill amount.
        amount_paid (float): The amount paid by the customer.

    Returns:
        float: Positive if more is owed, negative if change is due, zero if fully paid.
    """
    return total_bill - amount_paid


if __name__ == "__main__":
    try:
        # Get input from the user
        bill_amount = float(input("Enter the total bill amount: "))
        paid_amount = float(input("Enter the amount paid by the customer: "))

        if bill_amount < 0 or paid_amount < 0:
            print("Amounts cannot be negative. Please enter valid values.")
        else:
            # Calculate due amount
            result = calculate_due_amount(bill_amount, paid_amount)

            # Display result
            if result > 0:
                print(f"Customer still owes: ₹{result:.2f}")
            elif result < 0:
                print(f"Change to be returned: ₹{abs(result):.2f}")
            else:
                print("Bill fully paid. No due amount or change.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
