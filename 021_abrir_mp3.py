import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader

class music(App):
    sound=SoundLoader.load("ichika_nito_e_manuel_gardner_fernandes.mp3")
    def build(self):
        return Label(text="{:^65}\n\n{:^70}\n\n{:^75}\n\n{:^48}".format("ESTA OUVINDO", "ICHIKA NITO", "AND", "MANUEL GARDNER FERNANDES"))
    if sound:
        sound.play()
music().run()


    
        