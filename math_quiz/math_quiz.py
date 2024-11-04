import random

def generate_random_integer(min_value, max_value):
    """
    This function will return a random integer within the range of min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)


def random_arithmetic_operation():
    """
    This function will return a randomly chosen arithmetic operation from the options ['+', '-', '*'].
    """
    return random.choice(['+', '-', '*'])


def arithmetic_operation(number1, number2, operation):
    """
    This function creates a math problem string and calculates the answer based on the given operator.
    
    Args:
        number1 (int): The first number.
        number2 (int): The second number.
        operator (str): The operator ('+', '-', '*').
    
    Returns:
        tuple: A tuple containing the problem as a string and the correct answer as an integer.
    """
    
    problem = f"{number1} {operation} {number2}"
    
    if operation == '+':
        answer = number1 + number2
    elif operation == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return problem, answer

def math_quiz():

    """
    This is the main function for the Math Quiz Game. The user will be asked to solve a series of math problems.
    This function will make sure to track their score thoughout the entire game.
    """
    score = 0
    total_MathQuestions = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_MathQuestions):
        
        number1 = generate_random_integer(1, 10);
        number2 = generate_random_integer(1, 5.5);
        operation = random_arithmetic_operation()

        problem, correct_answer = arithmetic_operation(number1, number2, operation)
        print(f"\nQuestion: {PROBLEM}")

        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer) # the input is converted into an integer and checked
        except ValueError:
            print("This input is invalid. Please enter a value that is numeric")
            continue # Jumps to the next question if the input is invalid

        if useranswer == correct_answer:
            print("Correct! You earned one point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
