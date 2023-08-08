from manim import *

class Sum(Scene):
   def construct(self):
       text = Text("Summenzeichen", font_size=120)
       self.add(text)
       # sum_tex = Tex("$\sum$", font_size = 100)
       # sum_tex.next_to(text,DOWN)
       sum_tex = Tex("$\sum$", font_size = 300, fill_opacity = 0.5)
       
       self.play(FadeIn(text))
       self.add(sum_tex)
       self.play(FadeIn(sum_tex))
       