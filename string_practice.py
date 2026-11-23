severity = input("Severity: ").strip().lower()

bug_title = "loginn button not working"
fixed_title = bug_title.replace("loginn", "login")

is_login_bug = "login" in fixed_title

print("Cleaned severity:", severity)
print("Fixed title:", fixed_title)
print("Is login bug:", is_login_bug)
print("Title length:", len(fixed_title))