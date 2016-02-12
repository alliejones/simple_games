from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty
from ResizeBehavior import *





class GamePiece(ToggleButton):
    spot = ObjectProperty(None)

    def __init__(self, number, color, **kwargs):
        self.number = number
        self.player_color = color

        #scouts can move more than 1 space, flags/bombs can't move
        if self.number == 2:
            self.max_spaces = 9
        elif self.number in (0,11):
            self.max_spaces = 0
        else:
            self.max_spaces = 1
        super(GamePiece, self).__init__()

    def get_name(self):
        return names[self.number]


    def on_state(self, widget, value):
        print(str(self.number) + self.player_color + self.state)
        if value == 'down':
            if self.player_color == self.parent.activeplayer.color:
                self.parent.place_in_hand(self)
            else:
                self.spot.move_to_square()
                #self.state = "normal"
        else:
            self.parent.clear_hand()





names = {0: "Flag",
         1: "Spy",
         2: "Scout",
         3: "Miner",
         4: "Sergeant",
         5: "Lieutenant",
         6: "Captain",
         7: "Major",
         8: "Colonel",
         9: "General",
         10: "Marshal",
         11: "Bomb"}

pieceamounts = {0: 1,
           1: 1,
           2: 8,
           3: 5,
           4: 4,
           5: 4,
           6: 4,
           7: 3,
           8: 2,
           9: 1,
           10: 1,
           11: 6}

