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

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"

<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True
    text_align: "left"  # Set the text alignment to left
    
<ClickableTextFieldRound>:
    size_hint_y: None
    height: text_field.height

    MDTextField:
        id: text_field
        hint_text: root.hint_text
        text: root.text
        password: True
        icon_left: "key-variant"

    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field.password = False if text_field.password is True else True
            
<RightContentCls>
    disabled: True
    adaptive_size: True
    pos_hint: {"center_y": .5}

    MDIconButton:
        icon: root.icon
        user_font_size: "16sp"
        md_bg_color_disabled: 0, 0, 0, 0

    MDLabel:
        text: root.text
        font_style: "Caption"
        adaptive_size: True
        pos_hint: {"center_y": .5}


<Item>
    IconLeftWidget:
        icon: root.left_icon

    RightContentCls:
        id: container
        icon: root.right_icon
        text: root.right_text

ScreenManager:
    MainMenu:
    GasMenu:
    GasMenuH2Gas:
    
    
<GasMenu>:
    name: 'gas'
    BoxLayout:
        orientation: 'vertical'

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: "GAS"
                        elevation: 4
                        pos_hint: {"top": 1}
                        md_bg_color: "#e7e4c0"
                        specific_text_color: "#4a4939"
                        left_action_items: [['arrow-left', lambda x: root.change_screen('menu')]]
                        right_action_items: [["dots-vertical", lambda x: app.callback(x)]]
                           
                       

                    MDBottomNavigation:
                        selected_color_background: "orange"
                        text_color_active: "lightgrey"

                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'Mail'
                            icon: 'gmail'
                            badge_icon: "numeric-10"
                            
                            GridLayout:
                                cols: 2
                                padding: dp(16)
                                spacing: dp(10)

                                MDTextField:
                                    hint_text: "Date"
                                    id: date
                                    mode: "rectangle"

                                MDTextField:
                                    hint_text: "Shift"
                                    id: shift
                                    mode: "rectangle"

                                MDTextField:
                                    hint_text: "Temperature"
                                    id: temp
                                    mode: "rectangle"

                                MDTextField:
                                    hint_text: "Nitrogen"
                                    id: n_pressure
                                    mode: "rectangle"

                                MDTextField:
                                    hint_text: "Pressure"
                                    id: p_pressure
                                    mode: "rectangle"

                                MDTextField:
                                    hint_text: "Nitrogen cylinder pressure reading"
                                    id: n_cylinder_pressure
                                    mode: "rectangle"

                                MDTextField:
                                    hint_text: "Primary Pressure gauge BH2"
                                    id: p_pressure_gauge_bhs2
                                    mode: "rectangle"

                                MDTextField:
                                    hint_text: "Time"
                                    id: time
                                    mode: "rectangle"

                                    
                                MDTextField:
                                    hint_text: "Primary Pressure gauge Pallet"
                                    id: p_pressure_gauge_pallet
                                    mode: "rectangle"

                                MDTextField:
                                    hint_text: "Remarks"
                                    id: remarks
                                    mode: "rectangle"
                                    
                                MDTextField:
                                    hint_text: "Secondary Pressure gauge BH2"
                                    id: s_pressure_gauge
                                    mode: "rectangle"
                                    
                            BoxLayout:
                                orientation: 'horizontal'
                                size_hint_y: None
                                height: self.minimum_height
                                spacing: dp(10)
                                padding: dp(16)  # Add padding here

                                Widget:  # Spacer to push the button to the right
                                
                                MDRaisedButton:
                                    text: "Save"
                                    size_hint: None, None
                                    size: "340dp", "90dp"
                                    on_press: app.button_press()  # Replace with your button press function          

                        MDBottomNavigationItem:
                            name: 'screen 3'
                            text: 'LinkedIN'
                            icon: 'linkedin'

                            MDLabel:
                                text: 'LinkedIN'
                                halign: 'center'

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Header title"
                    title_color: "#4a4939"
                    text: "Header text"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Mail"

                DrawerClickableItem:
                    icon: "gmail"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Inbox"
                    on_press: root.manager.current = 'gas'
                    

                DrawerClickableItem:
                    icon: "send"
                    text: "Outbox"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Labels"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"
                   
                   
                   
               
                   

                ContentNavigationDrawer:
            
<GasMenuH2Gas>:
    name: 'h2gas'
    BoxLayout:
        orientation: 'vertical'

        MDNavigationLayout:

            MDScreenManager:

                MDScreen:

                    BoxLayout:
                        orientation: 'vertical'

                        MDTopAppBar:
                            title: "H2 GASS"
                            elevation: 4
                            pos_hint: {"top": 1}
                            md_bg_color: "#e7e4c0"
                            specific_text_color: "#4a4939"
                            left_action_items: [['arrow-left', lambda x: root.change_screen('gas')]]
                            right_action_items: [["dots-vertical", lambda x: app.callback(x)]]

<MainMenu>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: "Navigation Drawer"
                        elevation: 4
                        pos_hint: {"top": 1}
                        md_bg_color: "#e7e4c0"
                        specific_text_color: "#4a4939"
                        left_action_items:
                            [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items:
                            [['theme-light-dark', lambda x: app.switch_theme_style()],["clock", lambda x: app.callback_2()]]
                           
                       

                    MDBottomNavigation:
                        selected_color_background: "orange"
                        text_color_active: "lightgrey"

                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'Mail'
                            icon: 'gmail'
                            badge_icon: "numeric-10"
                            
                            MDLabel:
                                text: 'TEST'
                                halign: 'center'

                        MDBottomNavigationItem:
                            name: 'screen 3'
                            text: 'LinkedIN'
                            icon: 'linkedin'

                            MDLabel:
                                text: 'LinkedIN'
                                halign: 'center'

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Header title"
                    title_color: "#4a4939"
                    text: "Header text"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Mail"

                DrawerClickableItem:
                    icon: "gmail"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Inbox"
                    on_press: root.manager.current = 'gas'
                    

                DrawerClickableItem:
                    icon: "send"
                    text: "Outbox"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Labels"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"
                ContentNavigationDrawer:

'''


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
        self.screen = Builder.load_string(KV)

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
