# My first QAssist AI program - Bug Classifier
# Classifies a bug by severity

print("QAssist AI - Bug Classifier")
print("---------------------------")

severity = input("Enter bug severity (High/Medium/Low): ").lower()

if severity == "high":
    print("Bug severity:", severity)
    print("Priority: P1 - Fix immediately")
elif severity == "medium":
    print("Bug severity:", severity)
    print("Priority: P2 - Fix before release")
elif severity == "low":
    print("Bug severity:", severity)
    print("Priority: P3 - Schedule in sprint")
else:
    print("Invalid severity. Please enter High, Medium, or Low.")
