import random

def generate_random_integer(min_value, max_value):
    """
    This function will return a random integer within the range of min_value and max_value (inclusive)The min_value and max_value must be of type int.
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
        operation (str): The operator ('+', '-', '*').
    
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
    This function will make sure to track their score throughout the entire game.
    """
    score = 0
    total_MathQuestions = 5  #needs to be an integer!

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_MathQuestions):
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5)  
        operation = random_arithmetic_operation()

        problem, correct_answer = arithmetic_operation(number1, number2, operation)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))  # Convert input to an integer and check
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue  # Skip to the next question if input is invalid

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_MathQuestions}")

if __name__ == "__main__":
    math_quiz()
