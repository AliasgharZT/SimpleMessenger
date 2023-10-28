from kivymd.app import MDApp
from kivy .lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.dialog import MDDialog
from AZ_MDBoxLayout import AZMDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.properties import ObjectProperty
from AZ_FileManager import MDFileManager

Builder.load_file('style.kv')

class Style(MDAnchorLayout):

    user_info={'name':None,'family':None,'number':None}
    # name_user=ObjectProperty()
    # family_user=ObjectProperty()
    # number_user=ObjectProperty()
    user_photo=ObjectProperty()
    address_photo=None 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f=MDFileManager(
            exit_manager=self.close_add_user_photo,
            icon_selection_button='content-save-check-outline',
            select_path=self.get_user_photo,
            size_hint=(0.6,0.7),
            preview=True,
        )

    get_user_info='''
AZMDBoxLayout:
    orientation:'vertical'
    spacing:7

    name:name
    family:family
    number:number

    MDTextField:
        id:name
        helper_text:'Enter Name'
    MDTextField:
        id:family
        helper_text:'Enter Family'
    MDTextField:
        id:number
        helper_text:'Enter Number'
        input_filter:'int'
    MDAnchorLayout:
        anchor_x:'center'
        anchor_y:'center'
        MDFillRoundFlatButton:
            text:'Rejister'
            on_press:
                root.get_user_info()
'''

    def about(self): 
        self.about_d=MDDialog(title='About :\n',
                              text='This program was created by Ali Asghar Zahdyan\n'+
                              '                                            < < < A . Z > > >')
        self.about_d.open()

    def add_user(self):
        self.add_user_d=MDDialog(title='Information :\n\n\n\n\n\n\n\n\n\n\n\n',type='custom',
                                 content_cls=Builder.load_string(self.get_user_info),
                                 buttons=[MDFlatButton(text='Back',on_press=self.close_add_user)  ] )
        self.add_user_d.size_hint=0.4,0.63
        self.add_user_d.open()
    
    def close_add_user(self,obj):
        self.add_user_d.dismiss()

    def add_user_photo(self):
        self.f.selection_button.on_press=self.set_user_photo
        self.f.show_disks()

    def close_add_user_photo(self,*args):
        self.f.close() 

    def get_user_photo(self,path):
        self.address_photo=path
        # self.user_photo.source=path

    def set_user_photo(self,*args):
        if self.address_photo==None:
            pass
        else:
            self.user_photo.source=self.address_photo
            self.address_photo=None 
            self.close_add_user_photo()

class MainApp(MDApp):
    
    def build(self):
        self.title='MESSENGER'
        self.icon='icon-app.jpg'
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette='BlueGray'
        self.theme_cls.primary_hue='900'
        return Style()


MainApp().run()