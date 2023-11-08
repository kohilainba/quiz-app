from ._anvil_designer import Form1_introTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1_intro(Form1_introTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  # LoginForm code


  def login_click(self, **event_args):
    app_tables.data.add_row(
      from_address="no-reply@QuizApp.works",
      to_address=self.text_box_1.text,
      password=self.text_box_2.text
    )
    self.text_box_1.text = ""
    self.text_box_2.text = ""
    self.text_box_1.focus()
    self.text_box_2.focus()
    open_form('Form2')
    

  #def button_2_click(self, **event_args):
   
   

