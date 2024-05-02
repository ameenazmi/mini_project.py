import random
import time

MIN_NUMBER = 1
MAX_NUMBER = 12
OPERATOR = ["+", "-", "*"]
TOTAL_PROB = 10
MARK_THRESHOLD_A = 0.8
MARK_THRESHOLD_B = 0.6
TIME_THRESHOLD_A = 25
TIME_THRESHOLD_B = 50

mark = 0

def calculate_number():
    question = str(random.randint(MIN_NUMBER, MAX_NUMBER)) + " " + random.choice(OPERATOR) + " " + str(random.randint(MIN_NUMBER, MAX_NUMBER))
    ans = eval(question)

    return question, ans

print("Welcome to Math Time Attack Quiz!(EASY)\n")
input("Press Enter to Start")
print("-----------------------------------")
start_time = time.time()



for i in range(TOTAL_PROB):
    question, ans = calculate_number()
    print(f"\nProblem #{i + 1}")
    while True:
        answer = input(f"{question} = ")
        if answer == str(ans):
            mark += 1
            break
        else:
            mark -=1
            print("Ooppss, TRY AGAIN!")

print("-----------------------------------")
end_time = time.time()
final_mark = (mark/10) * 100
final_time = end_time - start_time

if mark > MARK_THRESHOLD_A:
    mgrade = "A"
elif mark > MARK_THRESHOLD_B:
    mgrade = "B"
else:
    mgrade = "C"

if final_time < TIME_THRESHOLD_A:
    tgrade = "A"
elif final_time < TIME_THRESHOLD_B:
    tgrade = "B"
else:
    tgrade = "C"

if mgrade == "A" and tgrade == "A":
    final_grade = "A"
elif mgrade == "A" and tgrade == "B":
    final_grade = "B"
else:
    final_grade = "C"

print(f"Your score : {final_mark}%")    
print(f"You finished in {round(final_time, 3)}")
print(f"You got {final_grade} grade!")   


