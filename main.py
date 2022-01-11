from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase

from screens.screens import *

class WindowManager(ScreenManager):
    pass

class Test(MDApp):
    CLASSES = {
        'Welcome':'screens.welcome',
        'Login':'screens.login',
        'Signup':'screens.signup'
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive': True})
    ]
    KV_FILES = [
        'kv/welcome.kv',
        'kv/login.kv',
        'kv/signup.kv'
    ]
    def build_app(self):
        self.wm = WindowManager()
        screens = [
            Welcome(name="welcome"),
            Login(name="login"),
            Signup(name="signup"),
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="assets/font/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="assets/font/Poppins-SemiBold.ttf")
    Test().run()
