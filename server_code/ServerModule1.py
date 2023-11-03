import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class QuizAppServerModule:

    # Sample quiz questions
    questions = [
        {
            'question_text': 'What is the capital of France?',
            'options': ['London', 'Paris', 'Berlin', 'Madrid'],
            'correct_answer': 'Paris'
        },
        {
            'question_text': 'Which planet is known as the Red Planet?',
            'options': ['Earth', 'Mars', 'Venus', 'Jupiter'],
            'correct_answer': 'Mars'
        },
        {
            'question_text': 'What is the symbol for water on the periodic table?',
            'options': ['H', 'O', 'W', 'A'],
            'correct_answer': 'H'
        },
        {
            'question_text': 'Who painted the Mona Lisa?',
            'options': ['Vincent van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 'Claude Monet'],
            'correct_answer': 'Leonardo da Vinci'
        },
        {
        'question_text': 'What is the largest mammal in the world?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'correct_answer': 'Blue Whale'
        }
    ]

    def __init__(self):
        self.user_responses = []
    @anvil.server.callable
    def get_quiz_question(self, question_number):
        # Get the quiz question based on the question number
        if 1 <= question_number <= len(self.questions):
            return self.questions[question_number - 1]
        else:
            return None

    @anvil.server.callable
    def save_user_response(self, question_number, selected_option):
        # Save the user's response
        if 1 <= question_number <= len(self.questions):
            question = self.questions[question_number - 1]
            self.user_responses.append({'question_text': question['question_text'],
                                        'selected_option': selected_option,
                                        'correct_answer': question['correct_answer']})

    @anvil.server.callable
    def get_user_responses(self):
        # Get user responses for admin
        return self.user_responses

    @anvil.server.callable
    def clear_user_responses(self):
        # Clear user responses for the next quiz attempt
        self.user_responses = []
    @anvil.server.callable
    def send_completion_email(self, user_email):
        # Send completion email to the user
        anvil.email.send(
            to=user_email,
            subject='Quiz Completed',
            text='Congratulations! You have completed the quiz.'
        )

    



# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

