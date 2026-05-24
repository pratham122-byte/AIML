def vacuum_cleaner():
    location = input("Enter the current location of the vacuum (A or B): ").upper()
    state_A = input("Enter the status of location A (Dirty/Clean): ").lower()
    state_B = input("Enter the status of location B (Dirty/Clean): ").lower()
    print("\n--- Vacuum Cleaner Simulation Start ---")
    if location == 'A':
        if state_A == 'dirty':
            print("Location A is dirty. Cleaning A...")
            state_A = 'clean'
        else:
            print("Location A is already clean.")
        print("Moving to location B...")
        if state_B == 'dirty':
            print("Location B is dirty. Cleaning B...")
            state_B = 'clean'
        else:
            print("Location B is already clean.")
    elif location == 'B':
        if state_B == 'dirty':
            print("Location B is dirty. Cleaning B...")
            state_B = 'clean'
        else:
            print("Location B is already clean.")
        print("Moving to location A...")
        if state_A == 'dirty':
            print("Location A is dirty. Cleaning A...")
            state_A = 'clean'
        else:
            print("Location A is already clean.")
    else:
        print("Invalid location! Please enter A or B.")
    print("\n--- Final Status ---")
    print(f"Location A: {state_A}")
    print(f"Location B: {state_B}")
    print("All locations are clean now!")
vacuum_cleaner()
