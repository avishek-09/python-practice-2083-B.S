# A simple quiz game using python

questions = ("In which country is the Mt.Everest ?",
             "What is the capital city of Nepal ?",
             "Which is the largest desert of the world ?",
             "Cristiano Ronaldo is form which country ?")
options = (("A. Nepal","B. India","C. China","D. Bhutan"),
           ("A. Pokhara","B. Baglung","C. Kathmandu","D. Texas"),
           ("A. Sahara","B. Egypt","C. Antartica","D. Artic"),
           ("A. Spain","B. Argentina","C. England","D. Portugal"))

answers = ("A","C","C","D")
guesses = []
q_no = 0
score = 0
print("--------")
for question in questions:
    print(question)
    for option in options[q_no]:
        print(option)
    guess= input("Enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[q_no]:
        score += 1 
        print("Correct!!")
    else:
        print("Incorrect!!")
        print(f"{answers[q_no]} is the correct answer.")
    q_no += 1
    print("---------")
s = int((score/len(questions)) * 100)
print(f"---Congrts you scored {s}%---")