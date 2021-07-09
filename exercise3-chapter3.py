score = input('Enter the score between 0.0 and 1.0: ')
try:
    score  = float(score)
    if (score <= 1.0 and score >=0):
        if score >=0.9:
            print("\nGrade A")
        elif score >=0.8:
            print("\nGrade B")
        elif score >=0.7:
            print("\nGrade C")
        elif score >=0.6:
            print("\nGrade D")
        else:
            print("\nGrade F")
    else:
        print("\nBad score")
except:
    print("\nBad score")

