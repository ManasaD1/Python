def bank_withdrawal():
    account_balance = 500.0
    print(f"=== Welcome to the Bank ATM (Current Balance: ${account_balance}) ===")

    try:
        user_input = input("Enter the amount you wish to withdraw: ")
        amount = float(user_input)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        
        if amount > account_balance:
            raise RuntimeError("Insufficient funds in your account.")

    except ValueError as val_err:
        print(f"\n[ERROR] Invalid Input: {val_err}")
        print("-> Please enter a valid positive number next time.")

    except RuntimeError as run_err:
        print(f"\n[ERROR] Transaction Denied: {run_err}")
        print("-> Consider checking your balance or requesting a smaller amount.")

    except Exception as general_err:
        print(f"\n[ERROR] An unexpected system error occurred: {general_err}")

    else:
        account_balance -= amount
        print("\n[SUCCESS] Transaction approved!")
        print(f"-> Dispensing ${amount:.2f}...")
        print(f"-> Your new balance is: ${account_balance:.2f}")

    finally:
        print("\n[SYSTEM] Safely terminating your session...")
        print("[SYSTEM] Connection closed. Thank you for banking with us!\n")
bank_withdrawal()
