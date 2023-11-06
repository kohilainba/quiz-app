from ._anvil_designer import Form7Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form7(Form7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.question_inputs = [self.question1,self.question2, self.question3, self.question4, self.question5]
        self.answer_inputs = [
            [self.q1_ans1, self.q1_ans2, self.q1_ans3],
            [self.q2_ans1, self.q2_ans2, self.q2_ans3],
            [self.q3_ans1, self.q3_ans2, self.q3_ans3],
            [self.q4_ans1, self.q4_ans2, self.q4_ans3],
            [self.q5_ans1, self.q5_ans2, self.q5_ans3]
        ]
    # Any code you write here will run before the form opens.
  def button_2_click(self, **event_args):
      # Create a list to store question-answer pairs
      question_answers = []
   # Loop through the question and answer inputs
      for i in range(5):
           question = self.question_inputs[i].text
           answers = [ans.text for ans in self.answer_inputs[i]]
           question_answers.append((question, answers))
        

        # Store the data in the QuizData table
      for question, answers in question_answers:
            app_tables.quiz_data.add_row(Question=question, Answers=answers)

        # Clear the input fields
      for question_input in self.question_inputs:
            question_input.text = ""
      for answer_input_set in self.answer_inputs:
            for answer_input in answer_input_set:
                answer_input.text = ""

      alert("Quiz questions and answers have been saved to the database.", title="Success")
    
        
       
    
