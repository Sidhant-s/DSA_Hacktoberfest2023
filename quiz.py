class Quiz:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer == self.correct_option

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.score = 0

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

    def take_quiz(self):
        for quiz in self.quizzes:
            print(quiz.question)
            for i, option in enumerate(quiz.options, start=1):
                print(f"{i}. {option}")
            
            user_answer = int(input("Enter the number of your answer: "))
            if quiz.is_correct(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print("Incorrect. The correct answer is:", quiz.options[quiz.correct_option - 1], "\n")
        
        print("Quiz completed. Your score:", self.score, "out of", len(self.quizzes))

# Create a quiz game
quiz_game = QuizGame()

# Add quizzes to the game
quiz1 = Quiz("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3)
quiz2 = Quiz("Which planet is known as the Red Planet?", ["Earth", "Mars", "J
