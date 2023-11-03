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

