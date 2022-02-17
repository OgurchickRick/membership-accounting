from kivy.uix.screenmanager import Screen, SlideTransition
from kivyauth.utils import auto_login, login_providers
from kivyauth.google_auth import initialize_google, login_google


GOOGLE_CLIENT_ID = "1039821075002-km4ku6n5t3kk1h5aq33hi4rs7a1b33l0.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"


class Welcome(Screen):
    current_provider = ""

    def on_start(self):
        if auto_login(login_providers.google):
            self.current_provider = login_providers.google

    def login(self):
        initialize_google(self.after_login, self.error_listener, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET)

    def gl_login(self, *args):
        login_google()
        self.current_provider = login_providers.google

        self.show_login_progress()

    def after_login(self, **qwargs):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'clients'
        self.hide_login_progress()


    def error_listener(self, **qwargs):
        pass
