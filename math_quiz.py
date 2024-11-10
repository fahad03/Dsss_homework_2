import random


def get_random_number(low, high):
    """
    Generates a random integer between low and high, inclusive.
    
    Args:
    low (int): The lowest integer value.
    high (int): The highest integer value.
    
    Returns:
    int: A random integer between low and high.
    """
    return random.randint(low, high)


def get_random_operator():
    """
    Randomly selects an operator for the math question.
    
    Returns:
    str: One of the operators: '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def generate_question_and_answer():
    """
    Creates a math question and calculates the answer based on random values and operator.
    
    Returns:
    tuple: The question as a string and the correct answer as an integer.
    """
    number1 = get_random_number(1, 10)
    number2 = get_random_number(1, 10)
    operator = get_random_operator()
    
    # Formulate question based on the operator
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:  # operator == '*'
        answer = number1 * number2
    
    question = f"{number1} {operator} {number2}"
    return question, answer


def math_quiz():
    """
    Starts a math quiz game with randomly generated questions.
    User scores points for correct answers and loses points for incorrect ones.
    """
    total_score = 0
    total_questions = 5  # Set the number of questions in the quiz

    print("Welcome to the Enhanced Math Quiz!")
    print("You will answer math questions. Correct answers earn you points; wrong answers deduct points.")

    for i in range(1, total_questions + 1):
        print(f"\nQuestion {i}:")
        
        # Generate a math question and its answer
        question, correct_answer = generate_question_and_answer()
        print("Solve:", question)
        
        try:
            # Get the user's answer
            user_answer = int(input("Your answer: "))

            # Check answer correctness and update score
            if user_answer == correct_answer:
                print("Correct! You earned 2 points.")
                total_score += 2  # Increase score for correct answer
            else:
                print(f"Incorrect. The correct answer was {correct_answer}. You lost 1 point.")
                total_score -= 1  # Decrease score for incorrect answer

        except ValueError:
            # Handle cases where user input is not an integer
            print("Invalid input! Please enter a numeric value. This question is skipped.")
        
    print(f"\nQuiz over! Your total score is: {total_score}/{total_questions * 2}")


# Execute the math quiz game
if __name__ == "__main__":
    math_quiz()
