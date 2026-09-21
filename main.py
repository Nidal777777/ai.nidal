from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex

class AISharedApp(App):
    def build(self):
        self.title = "منصة الذكاء الاصطناعي الشاملة"
        
        root_layout = BoxLayout(orientation='vertical', padding=15, spacing=12)
        
        title_label = Label(
            text='[b]AI Shared Hub[/b]',
            markup=True,
            size_hint=(1, 0.08),
            font_size='22sp',
            color=get_color_from_hex('#3498db')
        )
        root_layout.add_widget(title_label)
        
        self.output_label = Label(
            text='أهلاً بك يا سيد المعلمين! اكتب طلبك أو سؤالك أدناه للبدء...',
            size_hint_y=None,
            valign='top',
            halign='left',
            markup=True,
            color=get_color_from_hex('#ecf0f1')
        )
        self.output_label.bind(texture_size=self.output_label.setter('size'))
        self.output_label.bind(width=lambda *x: setattr(self.output_label, 'text_size', (self.output_label.width - 20, None)))
        
        scroll_view = ScrollView(size_hint=(1, 0.68), bar_width=10)
        scroll_view.add_widget(self.output_label)
        root_layout.add_widget(scroll_view)
        
        self.text_input = TextInput(
            text='',
            hint_text='اكتب استفسارك هنا...',
            size_hint=(1, 0.11),
            multiline=False,
            background_color=get_color_from_hex('#2c3e50'),
            foreground_color=get_color_from_hex('#ffffff'),
            cursor_color=get_color_from_hex('#3498db')
        )
        root_layout.add_widget(self.text_input)
        
        send_button = Button(
            text='إرسال الطلب',
            size_hint=(1, 0.11),
            background_normal='',
            background_color=get_color_from_hex('#2980b9'),
            color=(1, 1, 1, 1),
            bold=True,
            font_size='16sp'
        )
        send_button.bind(on_press=self.on_send_click)
        root_layout.add_widget(send_button)
        
        return root_layout

    def on_send_click(self, instance):
        user_text = self.text_input.text.strip()
        if user_text:
            current_text = self.output_label.text
            new_text = f"{current_text}\n\n[color=#e74c3c]أنت:[/color] {user_text}\n[color=#2ecc71]الذكاء الاصطناعي:[/color] جاري معالجة طلبك بنجاح..."
            self.output_label.text = new_text
            self.text_input.text = ''

if __name__ == '__main__':
    AISharedApp().run()
