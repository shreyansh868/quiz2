import os

# Function to load quiz data from a file
def load_quiz_data(file_name="quiz_data.txt"):
    """
    Reads the quiz data from a text file.
    Returns a list of dictionaries containing questions, options, and answers.
    """
    questions = []
    if not os.path.exists(file_name):
        print(f"Error: {file_name} not found in {os.getcwd()}")
        return questions

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 4):  # Each question block is 4 lines (3 lines + 1 blank line)
                question = lines[i].strip()
                options = lines[i + 1].strip().split(",")
                answer = lines[i + 2].strip()
                questions.append({"question": question, "options": options, "answer": answer})
    except Exception as e:
        print(f"Error reading quiz data: {e}")
    return questions


# Function to administer the quiz
def take_quiz(questions):
    """
    Administers the quiz to the user and calculates their score.
    """
    score = 0
    for idx, question in enumerate(questions, start=1):
        print(f"\nQuestion {idx}: {question['question']}")
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        # Get user's answer
        try:
            user_answer = int(input("Enter your choice (1-4): "))
            if question["options"][user_answer - 1] == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer was: {question['answer']}")
        except (ValueError, IndexError):
            print("Invalid choice! Please enter a number between 1 and 4.")

    print(f"\nQuiz completed! Your final score is: {score}/{len(questions)}")
    return score


# Function to save the user's score
def save_score(user_name, score, file_name="scores.txt"):
    """
    Saves the user's score to a file.
    """
    try:
        with open(file_name, "a") as file:
            file.write(f"{user_name}: {score}\n")
        print(f"Score for {user_name} saved successfully in {file_name}.")
    except Exception as e:
        print(f"Error saving score: {e}")


# Main function
def main():
    """
    Main function to run the quiz application.
    """
    print("Welcome to the Quiz Application!")

    # Load quiz data
    questions = load_quiz_data()

    if not questions:
        print("No quiz data available. Please check the file and try again.")
        return

    # Get the user's name
    user_name = input("Enter your name: ")

    # Administer the quiz
    score = take_quiz(questions)

    # Save the user's score
    save_score(user_name, score)


if __name__ == "__main__":
    main()
