import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle,Ellipse,Line,Color

class Mypaint(Widget):
    def on_touch_down(self,touch):
        with self.canvas:
            Color(1,0,0)
            Rectangle(pos=(touch.x,touch.y),size=(50,50))
            touch.ud['line'] = Line(points=(touch.x,touch.y))

    def on_touch_move(self,touch):
        Color(1,1,0,1, mode="rgba")
        touch.ud['line'].points +=[touch.x,touch.y]



class PaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = Mypaint()
        clear = Button(text = 'clear')
        clear.bind(on_release = self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clear)
        return parent

    def clear_canvas(self,obj):
        self.painter.canvas.clear()

if __name__ == "__main__":
    PaintApp().run()