# Human Resources Program - Sept 6, 2023

assessment_score = 85
location = "Canada"

if (location == "US" or location == "Canada") and assessment_score >= 75:
    print(f"Your assessment score is {assessment_score}/100! You're hired!")
elif location != "US" or location != "Canada" and assessment_score >= 75:
    print(
        f"Apologies, you are based in {location} but this role requires you to be based in the US/Canada. Would you "
        f"be interested in another role?")
else:
    print(
        f"Thank you for your interest, we regret to inform you that we will not be moving forward with your application.")