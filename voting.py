def check_voting_eligibility(age):
    if age < 18:
        raise ValueError("You are not eligible to vote")
    else:
        return "You are eligible to vote"
    

age = int(input())
print(check_voting_eligibility(age))