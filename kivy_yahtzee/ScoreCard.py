#import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty, DictProperty, \
                            StringProperty, ObjectProperty
from kivy.uix.widget import Widget
from ValueChecking import score_types





    
class ScoreOption(BoxLayout):
    text = StringProperty("default")
    value = NumericProperty(0)

    def italicize_text(self):
        for widget in self.children:
            widget.markup = True
            widget.text = "[i]" + widget.text + "[/i]"


class BonusScoreOption(ScoreOption):
    pass



class ScoreCard(BoxLayout):
    def __init__(self, **kwargs):
        super(ScoreCard,self).__init__()
        for entry in score_types:
            self.add_widget(ScoreOption(id = entry))


    def select_score(self):
        for option in self.children:
            if option.ids["button"].state == "down":
                option.used = True
            elif option.used == False:
                option.value = 0
    

    def show_score_options(self, choice_of_scores):
        for option in self.children:

            if option.id == "Yahtzee Bonus":
                #I thought I could use self.ids["Yahtzee Bonus"] instead of self.children[1] but it won't work
                if self.children[1].used == True:
                    if choice_of_scores["Yahtzee Bonus"] != 0:
                        option.disabled = False
                else:
                    option.disabled = True

            if option.id in choice_of_scores.keys() and option.disabled == False:
                option.value += choice_of_scores[option.id]





    def disable_score_options(self):
        for option in self.children:
            option.disabled = True

    def enable_score_options(self):
        for option in self.children:
            if option.used == False:
                option.disabled = False



    





 
