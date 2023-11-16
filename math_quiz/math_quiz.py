import random


def generate_random_integer(minimum, maximum):
    """
    Generates a random integer between the specified minimum and maximum values.
    """
    return random.randint(minimum, maximum)


def generate_arithmetic_operator():
    """
    Generates a random arithmetic operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])


def calculate_arithmetic_result(number1, number2, operator):
    """
    Calculates the result of an arithmetic expression.
    """
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2

    expression = f"{number1} {operator} {number2}"
    return expression, result


def math_quiz():
    """
    Conducts a math quiz game, presenting questions and checking user answers.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz!")
    print("You will be presented with problems, and need to provide the correct answers")

    for _ in range(total_questions):
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5)
        operator = generate_arithmetic_operator()

        problem, answer = calculate_arithmetic_result(number1, number2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0  # Assign a default value to avoid crashing the program.

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
