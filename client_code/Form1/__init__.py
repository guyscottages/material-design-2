from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  '''
  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
  '''

  '''
  def text_box_1_pressed_enter(self, **event_args):
    my_message = self.text_box_1.text
    alert('You typed: ' + my_message)
  '''

  def button_1_click(self, **event_args):
    name = self.text_box_1.text
    alert('Hi ' + name + '!')
    self.text_box_1.text = ''
    self.text_box_1.focus()





  # master

 
