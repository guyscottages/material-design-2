from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    my_message = 'You just clicked the button!'
    alert(my_message) 
  # b 3

 
