from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
# from views import mobile_view, tablet_view, desktop_view
from kivymd.uix.dialog import MDDialog
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.toolbar import MDTopAppBar
from kivy.properties import ObjectProperty
import requests
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu


class GasMenu(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class GasMenuH2Gas(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class MainMenu(Screen):
    pass


sm = ScreenManager()
sm.add_widget(GasMenu(name="gas"))
sm.add_widget(MainMenu(name="menu"))
sm.add_widget(GasMenuH2Gas(name="h2gas"))


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]


class ContentNavigationDrawer(MDBoxLayout):
    pass


class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file("main.kv")

    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "H2 GAS",
                "height": dp(56),
                "on_release": lambda x="H2 GAS", screen_name='h2gas': self.change_screen_h2_gas(screen_name),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Item 2",
                "height": dp(56),
                "on_release": lambda x="Item 2": self.menu_callback(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Item 3",
                "height": dp(56),
                "on_release": lambda x="Item 3": self.menu_callback(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Item 4",
                "height": dp(56),
                "on_release": lambda x="Item 4": self.menu_callback(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Item 5",
                "height": dp(56),
                "on_release": lambda x="Item 5": self.menu_callback(x),
            }
        ]
        self.menu = MDDropdownMenu(
            items=self.menu_items,
            width_mult=4,
        )
        return self.screen

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Amber" else "Amber"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def change_screen(self, screen_name):
        self.root.current = screen_name

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        print('test')

    def change_screen_h2_gas(self, screen_name):
        self.menu.dismiss()
        self.root.current = screen_name


Example().run()
