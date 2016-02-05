from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from ResizeBehavior import *
from Terrain import *
from GamePiece import *



class StrategoWindow(FloatLayout):
    def change_gamestate(self):
        #0 is game setup
        if self.gamestate == 0:
            pass






class StrategoBoard(GridLayout):
    def __init__(self, **kwargs):
        self.grid = []
        super(StrategoBoard, self).__init__()
        self.create_background()

    def create_background(self):
        for i in range(10):
            self.grid.append([])
            for j in range(10):
                self.grid[i].append(j)
                if i in (4,5) and j in (2,3,6,7):
                    self.add_widget(Terrain(i,j, land=False))
                else:
                    self.add_widget(Terrain(i,j))


class Sidebar(GridLayout):
    def __init__(self, **kwargs):
        super(Sidebar, self).__init__()
        for piecenumber in pieceamounts:
            for i in range(pieceamounts[piecenumber]):
                self.add_widget(GamePiece(piecenumber, "Red"))