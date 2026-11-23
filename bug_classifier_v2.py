# Ask the user for the bug description and clean it
description = input("Enter bug description: ").strip().lower()

# --- 1. Detect the module ---
if "login" in description:
    module = "Login"
elif "payment" in description:
    module = "Payment"
elif "search" in description:
    module = "Search"
else:
    module = "General"

# --- 2. Detect the severity ---
if "crashed" in description:
    severity = "High"
    evidence = "'crashed'"
elif "slow" in description:
    severity = "Medium"
    evidence = "'slow'"
else:
    severity = "Low"
    evidence = "none"

# --- 3. Print the report ---
print("\n--- QAssist AI Bug Report ---")
print("Module:", module)
print("Severity:", severity, "(Evidence:", evidence + ")")