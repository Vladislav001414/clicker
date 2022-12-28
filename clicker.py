from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.label import Label
from kivymd.uix.floatlayout import FloatLayout
import json
class app(MDApp):
    def build(self):
        ###Данные###
        self.score = 0
        default = {"score":0}
        try:
            with open("data.txt") as data:
                l = json.load(data)
                self.score = l["score"]
        except:
            with open("data.txt", "w") as data:
                json.dump(default, data)
                
            with open("data.txt") as data:
                l = json.load(data)
                self.score = l["score"]
            
        
        
        fl = FloatLayout()
        but = MDFillRoundFlatButton(text = "Кликни сюда", pos_hint = {"center_x":.5, "center_y":.4}, size_hint = (.5,.3))
        self.lb = Label(text = str(self.score), pos_hint = {"center_x":.5, "center_y":.6}, font_size = "30sp", color = (0,0,0,1))
        fl.add_widget(but)
        fl.add_widget(self.lb)
        but.bind(on_press = self.add)
        return fl
    def add(self, instance):
        self.score += 1
        self.lb.text = str(self.score)
        db = {"score":self.score}
        with open("data.txt", "w") as data:
            json.dump(db, data)
        
        
app().run()