from ._anvil_designer import Form1_copyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1_copy(Form1_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  # LoginForm code


    def login_button_click(self, **event_args):
        email = self.email_textbox.text
        password = self.password_textbox.text

        # Validate user credentials
        if anvil.server.call('validate_user_credentials', email, password):
            open_form('QuestionPage', question_number=1, user_email=email)
        else:
            self.error_label.text = 'Invalid email or password. Please try again.'

