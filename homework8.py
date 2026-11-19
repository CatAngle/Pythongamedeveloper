import random
import time

def math_speed_quiz():
    print("Welcome to the Python Math Speed Quiz (Quiz Master)!")
    print("Rules: The system will generate random questions, and you need to input the correct answer as quickly as possible.")
    print("(Enter 'q' to quit the game at any time)\n")

    score = 0
    total_questions = 5  # Set the number of questions
    start_time = time.time()

    for i in range(total_questions):
        # Randomly generate two numbers between 1-10 and an operator
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        
        # Calculate the correct answer (avoid negative numbers by subtracting the smaller from the larger)
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            if num1 < num2:
                num1, num2 = num2, num1
            answer = num1 - num2
        else:
            answer = num1 * num2

        # Ask the question
        try:
            user_input = input(f"Question {i + 1}: {num1} {operator} {num2} = ? ")
            
            if user_input.lower() == 'q':
                print("Game exited.")
                break
                
            user_answer = int(user_input)
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        # Check the answer
        if user_answer == answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {answer}.\n")

    # Calculate total time and final score
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
    print("=" * 30)
    print(f"Quiz finished! You got {score} / {total_questions} correct")
    print(f"Total time: {total_time} seconds")
    
    if score == total_questions:
        print("🏆 Awesome, you are a true Quiz Master!")
    elif score >= total_questions // 2:
        print("👍 Good job, keep it up!")
    else:
        print("💪 Practice your math skills a bit more!")

if __name__ == "__main__":
    math_speed_quiz()