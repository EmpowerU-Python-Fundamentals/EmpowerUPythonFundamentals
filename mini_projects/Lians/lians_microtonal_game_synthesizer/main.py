import arcade as a
from arcade.gui.widgets.buttons import UIFlatButtonStyle
from arcade.gui import (
    UIAnchorLayout,
    UIBoxLayout,
    UIDropdown,
    UIFlatButton,
    UILabel,
    UISlider,
    UITextureToggle,
    UIView,
    UIGridLayout,
    UIManager,
)
from random import choice
from collections import defaultdict
import webbrowser

import wave
from defines import (
    SCREEN_WIDTH, SCREEN_HEIGHT, TITLE,
    DIATONIC, CHROMATIC, MICROTONAL, SCALE_CHROMATIC, SCALE_MICROTONAL,
    TEX_TOGGLE_RED, TEX_TOGGLE_GREEN, TEX_CHECKBOX_CHECKED, TEX_CHECKBOX_UNCHECKED,
    SPRITE_SCALE, SPRITE_POS_X, SPRITE_POS_Y, SPRITE_STEP, SPRITE_ANGLE,
    FONT, FONT_MENU,
    PITCH, GAME_VARIANT, SELECTED, OCTAVE_MODIFIERS, QUESTIONS, ANSWERS,
    LINK_ABOUT, LINK_PROFILE,
    BUTTON_COLOR_1, BUTTON_COLOR_2, BUTTON_COLOR_3, BUTTON_COLOR_4,
)

            
class SliderDisable(UISlider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enabled = True         
    def on_event(self, event):
        if not self.enabled:
            return
        return super().on_event(event)


class SideButton(UIFlatButton):
    def __init__(
        self, text, font=FONT_MENU,
        font_size=18, size_hint=(0.09, 0.05),
        color_dark=BUTTON_COLOR_1, 
        color_middle=BUTTON_COLOR_2, 
        color_light=BUTTON_COLOR_3):
        super().__init__()
        
        self.text = f"{text}"
        self.style = {
        "press": UIFlatButtonStyle(
            font_name=font,
            font_color=color_dark,
            bg=color_middle,
            font_size=font_size),
        "normal": UIFlatButtonStyle(            
            font_name=font,
            font_color=color_dark,
            bg=color_light,
            font_size=font_size),
        "hover": UIFlatButtonStyle(
            font_name=font,
            font_color=color_light,
            bg=color_dark,                        
            font_size=font_size)}
        self.size_hint = size_hint
        
   
class StyledDropdown(UIDropdown):
    def __init__(
        self, default=None, options=None,
        font=FONT_MENU, font_size=18,
        color_dark=BUTTON_COLOR_1,
        color_middle=BUTTON_COLOR_2,
        color_light=BUTTON_COLOR_3,
        color_darkest=BUTTON_COLOR_4):
        
        self.primary_style = {
            "normal": UIFlatButtonStyle(
                font_name=font,
                font_color=color_light,
                bg=color_dark,
                font_size=font_size),
            "hover": UIFlatButtonStyle(
                font_name=font,
                font_color=color_light,
                bg=color_middle,
                font_size=font_size),
            "press": UIFlatButtonStyle(
                font_name=font,
                font_color=color_dark,
                bg=color_middle,
                font_size=font_size)}
        self.dropdown_style = {
            "normal": UIFlatButtonStyle(
                font_name=font,
                font_color=color_middle,
                bg=color_darkest,
                font_size=font_size),
            "hover": UIFlatButtonStyle(
                font_name=font,
                font_color=color_light,
                bg=color_dark,
                font_size=font_size),
            "press": UIFlatButtonStyle(
                font_name=font,
                font_color=color_light,
                bg=color_middle,
                font_size=font_size)}
        self.active_style = {
            "normal": UIFlatButtonStyle(
                font_name=font,
                font_color=color_dark,
                bg=color_middle,
                font_size=font_size),
            "hover": UIFlatButtonStyle(
                font_name=font,
                font_color=color_light,
                bg=color_middle,
                font_size=font_size),
            "press": UIFlatButtonStyle(
                font_name=font,
                font_color=color_light,
                bg=color_dark,
                font_size=font_size)}
        super().__init__(
            default=default,
            options=options,
            primary_style=self.primary_style,
            dropdown_style=self.dropdown_style,
            active_style=self.active_style)
   
   
class MenuView(UIView):
    def __init__(self):        
        super().__init__()
        self.ui.enable()
        self.background_color = a.color.FLORAL_WHITE       
        
        self.grid = UIGridLayout(
            horizontal_spacing=150, 
            vertical_spacing=80, 
            column_count=2, 
            row_count=4)
        self.anchor = UIAnchorLayout(children=[self.grid])
        self.ui.add(self.anchor)     
        
        self.open_github_button()
        self.open_about_button()  
        self.title()
        self.add_pitch_things()
        self.set_notes_selected()
        self.set_octave_checkboxes()
        self.set_game_variant()
        self.set_questions()
        self.start()
    
    def open_github_button(self):     
        button = self.anchor.add(
            SideButton(text="Author"),
            anchor_y="top",
            align_y=-128,
            anchor_x="left",
            align_x=250)
        @button.event("on_click")
        def on_click(_):
            webbrowser.open(LINK_PROFILE)

    def open_about_button(self):
        button = self.anchor.add(
            SideButton(text="About"),
            anchor_y="top",
            align_y=-128,
            anchor_x="right",
            align_x=-250)
        @button.event("on_click")
        def on_click(_):
            webbrowser.open(LINK_ABOUT)        
                
    def title(self):    
        title = UILabel(
            text="Menu Screen",
            font_name=FONT,
            font_size=32,
            text_color=a.color.GRAY)
        self.grid.add(title, column=0, column_span=2, row=0)
        
    def set_game_variant(self):          
        self.variant = StyledDropdown(
            default="Challenge",
            options=["Challenge", "Training", "Synthesizer"])
        self.variant_warning = UILabel(
                    text="\n",
                    font_name=FONT_MENU,
                    font_size=18,
                    text_color=a.color.GRAY)
        self.sync_game_variant()  
              
        self.grid.add(UIBoxLayout(
            align="center",
            space_between=20,
            children=[
                UILabel(
                    text="Game Variant",
                    font_name=FONT_MENU,
                    font_size=26,
                    text_color=a.color.GRAY),
                self.variant,
                self.variant_warning]),
            column=1, row=1)        
        
        @self.variant.event("on_change")
        def on_game_variant_change(event):  
            global GAME_VARIANT
            var = self.variant.value 
            GAME_VARIANT = var    
            if var == "Synthesizer":
                self.question_slider.enabled = False
                self.variant_warning.text = "All notes will be playable"
            else:
                self.question_slider.enabled = True
                if GAME_VARIANT == "Training":
                    self.variant_warning.text = "Feedback after each guess"
                else:
                    self.variant_warning.text = "No feedback during the game"
        
    def set_notes_selected(self):
        self.notes = UITextureToggle(            
                on_texture=TEX_TOGGLE_GREEN,
                off_texture=TEX_TOGGLE_RED,
                value=True)                      
        self.sync_selected()        
        self.grid.add(UIBoxLayout(
            vertical=False,
            align="left",
            space_between=20,
            children=[
                UILabel(
                    text="Chromatic",
                    font_name=FONT_MENU,
                    font_size=26,
                    text_color=a.color.GRAY),
                self.notes,
                UILabel(
                    text="All notes",
                    font_name=FONT_MENU,
                    font_size=26,
                    text_color=a.color.GRAY)]),            
            column=0, row=3)
        
        @self.notes.event("on_change")
        def on_change_notes(event):
            global SELECTED
            if self.notes.value:
                SELECTED = "All notes"
            else:
                SELECTED = "Chromatic"                

    def set_octave_checkboxes(self):   
        self.oct_4 = UITextureToggle(
            on_texture=TEX_CHECKBOX_CHECKED,
            off_texture=TEX_CHECKBOX_UNCHECKED,
            width=52,
            height=52)
        self.oct_5 = UITextureToggle(
            on_texture=TEX_CHECKBOX_CHECKED,
            off_texture=TEX_CHECKBOX_UNCHECKED,
            width=52,
            height=52)
        self.oct_6 = UITextureToggle(
            on_texture=TEX_CHECKBOX_CHECKED,
            off_texture=TEX_CHECKBOX_UNCHECKED,
            width=52,
            height=52)                    
        self.sync_octave_checkboxes()                   
        self.grid.add(UIBoxLayout(
            vertical=False,
            align="center",
            space_between=20,
            children=[
                UILabel(
                    text="Octaves:",
                    font_name=FONT_MENU,
                    font_size=26,
                    text_color=a.color.GRAY),
                UIBoxLayout(children=[                    
                    UILabel(
                        text="4th",
                        font_name=FONT_MENU,
                        font_size=20,
                        text_color=a.color.GRAY),
                    self.oct_4,]),
                UIBoxLayout(children=[                    
                    UILabel(
                        text="5th",
                        font_name=FONT_MENU,
                        font_size=20,
                        text_color=a.color.GRAY),
                    self.oct_5,]),
                UIBoxLayout(children=[                    
                    UILabel(
                        text="6th",
                        font_name=FONT_MENU,
                        font_size=20,
                        text_color=a.color.GRAY),
                    self.oct_6,])]),
            column=0, row=2)
        
        global OCTAVE_MODIFIERS
        def set_octave_modifiers(state, modifier):
            if state:
                if modifier not in OCTAVE_MODIFIERS:
                    OCTAVE_MODIFIERS.append(modifier)
            else:
                if modifier in OCTAVE_MODIFIERS:
                    OCTAVE_MODIFIERS.remove(modifier)
            if len(OCTAVE_MODIFIERS) == 0:
                ch = choice([4, 5, 6])
                name = f"oct_{ch}"
                getattr(self, name).value = True           
                        
        @self.oct_4.event("on_change")
        def on_check_oct_4(event):
            set_octave_modifiers(self.oct_4.value, 1)                    
            
        @self.oct_5.event("on_change")
        def on_check_oct_5(event):
            set_octave_modifiers(self.oct_5.value, 2)  
            
        @self.oct_6.event("on_change")
        def on_check_oct_6(event):
            set_octave_modifiers(self.oct_6.value, 4)  
            
    def set_questions(self):           
        self.question_slider = SliderDisable(
            value=30,
            min_value=5,
            max_value=100,
            step=5)        
        self.sync_questions()        
        self.question_label = UILabel(
            text=f"Questions: {self.question_slider.value}",
            font_name=FONT_MENU,
            font_size=26,
            text_color=a.color.GRAY)
        self.grid.add(UIBoxLayout(
            align="center",
            space_between=20,
            children=[self.question_label, self.question_slider]),
            column=1, row=2)
        
        @self.question_slider.event("on_change")
        def on_slider_change(event):
            questions = int(self.question_slider.value)
            self.question_label.text = f"Questions: {questions}"
            global QUESTIONS
            QUESTIONS = questions
            
    def add_pitch_things(self):    
        self.pitch_slider = UISlider(
            value=440,
            min_value=380,
            max_value=480,
            step=1)
        self.sync_pitch()
        self.pitch_label = UILabel(
            text=f"Pitch: A = {PITCH} Hz",
            font_name=FONT_MENU,
            font_size=26,
            text_color=a.color.GRAY)
        self.grid.add(UIBoxLayout(
            align="center",
            space_between=20,
            children=[self.pitch_label, self.pitch_slider]),
            column=0,row=1)
        
        @self.pitch_slider.event("on_change")
        def on_slider_change(event):
            pitch = int(self.pitch_slider.value)
            self.pitch_label.text = f"Pitch: A = {pitch} Hz"
            global PITCH
            PITCH = pitch
            wave.set_frequencies(PITCH)
                    
    def start(self):   
        self.start_button = SideButton(
            text="Start", font=FONT, font_size=30, size_hint=(1, 1))
        self.grid.add(self.start_button, column=1, row=3)
        @self.start_button.event("on_click")
        def on_start(event):
            match GAME_VARIANT:
                case "Challenge":
                    game_view = Challenge()
                case "Training":
                    game_view = Training()
                case "Synthesizer":
                    game_view = Synthesizer()   
            game_view.setup()
            self.window.show_view(game_view)    

    def sync_pitch(self):
        self.pitch_slider.value = int(PITCH)
               
    def sync_octave_checkboxes(self):
        self.oct_4.value = 1 in OCTAVE_MODIFIERS
        self.oct_5.value = 2 in OCTAVE_MODIFIERS
        self.oct_6.value = 4 in OCTAVE_MODIFIERS   
            
    def sync_game_variant(self):
        self.variant.value = GAME_VARIANT        
    
    def sync_selected(self):
        self.notes.value = "All notes" in SELECTED
        
    def sync_questions(self):
        self.question_slider.value = int(QUESTIONS)         
                     
    def on_show_view(self):
        self.sync_octave_checkboxes()
        self.sync_pitch()
        self.sync_game_variant()
        self.sync_selected()
        self.sync_questions()
    

class Synthesizer(a.View):
    def __init__(self):
        super().__init__()
        self.window.background_color = a.color.OLD_LACE
        self.sprite_list = None
        self.sprite_dict = None
        self.sprite_dict_inverted = None
        self.labels = None
                
    def setup(self, text="Synthesizer"):         
        self.init_sprites_storages()
        self.create_diatonic()
        self.create_chromatic()
        self.create_microtonal()
        self.sprites_dict_inversion()
        self.set_ui(text=text)      
        
    def set_ui(self, text=None):
        self.ui_manager = UIManager()        
        self.anchor = UIAnchorLayout(children=[])
        self.ui_manager.add(self.anchor) 
        self.open_menu_button()
        self.open_about_button()
        self.title(text=text)
    
    def title(self, text=None):   
        self.anchor.add(
            UILabel(
                text=f"{text}",
                font_name=FONT,
                font_size=32,
                text_color=a.color.GRAY),
            anchor_y="top",
            align_y=-150,
            anchor_x="center")
    
    def open_about_button(self):
        button = self.anchor.add(
            SideButton(
                text="About",
                font_size=16),
            anchor_y="top",
            align_y=-50,
            anchor_x="right",
            align_x=-250)
        @button.event("on_click")
        def on_click(_):
            webbrowser.open(LINK_ABOUT)  

    def open_menu_button(self):
        self.open_menu_button = self.anchor.add(
            SideButton(
                text="Menu",
                font_size=16),
            anchor_y="top",
            align_y=-50,
            anchor_x="left",
            align_x=250)        
        @self.open_menu_button.event("on_click")
        def to_menu(event):
            game_view = MenuView()
            self.window.show_view(game_view)
               
    def init_sprites_storages(self):
        self.sprite_list = a.SpriteList()  # <sprite_obj_list>
        self.sprite_dict = {}              # SD  {note : <sprite_obj>}
        self.sprite_dict_inverted = {}     # SDI {<sprite_obj> : note}
        self.labels = {}
       
    def create_diatonic(self, accuracy=-2, enabled=True):
        textures = self._get_textures("diatonic")
        self.create_sprites_with_labels(
            notes=DIATONIC, textures=textures, accuracy=accuracy, font_size=30, enabled=enabled)     
        
    def create_chromatic(self, accuracy=-2, enabled=True):  
        textures = self._get_textures("chromatic")
        self.create_sprites_with_labels(
            notes=CHROMATIC,  textures=textures, accuracy=accuracy, x=0.5, y=1, enabled=enabled) 
        
    def create_microtonal(self, accuracy=-2, enabled=True):   
        textures = self._get_textures("microtonal")
        self.create_sprites_with_labels(
            notes=MICROTONAL, textures=textures, accuracy=accuracy, 
            x=0.25, y=0.5, x_offset=0.5, rotation=True, off=[4, 12], font_size=22,
            enabled=enabled)                    
    
    def _get_textures(self, name):
        textures = [
            f"./assets/images/{name}_regular.png",
            f"./assets/images/{name}_right.png",
            f"./assets/images/{name}_wrong.png",
            f"./assets/images/{name}_not_used.png",
        ]      
        return textures 
    
    def create_sprites_with_labels(self, notes, accuracy=None, enabled=True, **kwargs):
        positions = self.create_sprites(notes, accuracy=accuracy, enabled=enabled, **kwargs)
        for note, (x, y) in positions.items():
            self._create_label(x, y, text=note, note=note, 
                               font_size=kwargs.get("font_size", 26)) 
            
    def _set_accuracy(self, note):
        pass
    
    def _get_texture_index(self, acc=None):
        if acc == -2:         
            i = 0
        elif acc == -1:
            i = 3
        elif acc >= 90:
            i = 1
        elif acc <= 10:
            i = 2
        else:
            i = 0
        return i
    
    def _create_base_sprite(self, textures=None, scale=None):
        sprite = a.Sprite(img=None, scale=scale)
        for texture in textures:
            sprite.append_texture(a.load_texture(texture))
        return sprite
    
    def _get_sprite_position(self, i, x=0, y=0, x_offset=1, step=SPRITE_STEP):
        sprite_x = SPRITE_POS_X + (x + i * x_offset) * step
        sprite_y = SPRITE_POS_Y + y * step
        return (sprite_x, sprite_y)
    
    def _set_angle(self, i, rotation=False, off=None):
        if rotation:
            angle = SPRITE_ANGLE
            if i % 2 == 1:
                angle *= -1
            if i in off:
                angle = 0
            return angle
        return 0    
         
    def create_sprites(self, notes, 
                       x=0, y=0, x_offset=1,
                       textures=None, 
                       accuracy=None,
                       scale=SPRITE_SCALE,
                       rotation=False, off=[],
                       enabled=True, **kwards):
        positions = {}
        
        for i, note in enumerate(notes):
            if not note:
                continue
            sprite = self._create_base_sprite(textures=textures, scale=scale)

            acc = accuracy or self._set_accuracy(note)   
            index = self._get_texture_index(acc)
            sprite.set_texture(index)
            
            sprite.is_enabled = enabled
            sprite.is_clicked = False            
            sprite.timer = 0.0

            sprite_x, sprite_y = self._get_sprite_position(i=i, x=x, y=y, x_offset=x_offset)
            if i in off:
                sprite_x += 0.25 * SPRITE_STEP
                sprite_y -= 0.25 * SPRITE_STEP                
            sprite.position = sprite_x, sprite_y
            angle = self._set_angle(i, rotation=rotation, off=off)
            sprite.angle = angle
            
            self.sprite_list.append(sprite)
            self.sprite_dict[note] = sprite            
            positions[note] = sprite.position
        return positions
        
    def _create_label(
        self, sx, sy, text, note, 
        color=a.color.LIGHT_SLATE_GRAY, font_size=26, font=FONT, 
        ax="center", ay="center"):
        label = a.Text(
            text=text,
            x=sx,
            y=sy,
            color=color,
            font_size=font_size,
            font_name=font,
            anchor_x=ax,
            anchor_y=ay)
        self.labels[note] = label
                  
    def sprites_dict_inversion(self):
        self.sprite_dict_inverted = {v: k for k, v in self.sprite_dict.items()} 
             
    def on_draw(self, color=a.color.OLD_LACE):
        self.clear(color)
        self.ui_manager.draw()
        self.sprite_list.draw()
        for label in self.labels.values():
            label.draw()
    
    def on_mouse_press(self, x, y, button, _, audio=True):
        if button == a.MOUSE_BUTTON_LEFT:
            colliding_sprites = a.get_sprites_at_point((x, y), self.sprite_list) 
            if colliding_sprites:
                s = colliding_sprites[-1]
                if s.is_enabled:
                    s.is_clicked = True
                    s.timer = 0.0
                    if audio:
                        note=self.sprite_dict_inverted[s]
                        self.play_note(note)                            
                       
    def play_note(self, note):
        wave.play_note(note,
            octave_modifiers=OCTAVE_MODIFIERS)  

    def on_key_press(self, symbol, _):
        if symbol == a.key.ESCAPE:
            game_view = MenuView()
            self.window.show_view(game_view)
            
    def on_update(self, delta_time):
        for s in self.sprite_list:
            if s.is_clicked:
                self.animate_sprite(delta_time, s)
                
    def animate_sprite(self, dt, s):
        t_half = 0.2
        sc = SPRITE_SCALE
        sc_change = 0.04
        s.timer += dt
        if s.timer < t_half:
            s.scale = sc + sc_change * (s.timer / t_half)
        elif s.timer < t_half * 2:
            s.scale = sc - sc_change * ((s.timer - t_half) / t_half)
        else:
            s.scale = sc
            s.is_clicked = False
   
    def on_show_view(self):
        self.ui_manager.enable() 
        
                        
class Challenge(Synthesizer):
    def __init__(self):
        super().__init__()
        self.waiting_for_click = False
        self.current_answers = []
        self.note = ""  
        self.q = QUESTIONS
        self.previous = None
        self.transition_timer = None
    
    def setup(self, text="Challenge"):
        self.transition_delay = 0
        self.init_sprites_storages()
        self.create_diatonic()
        self.create_chromatic()
        if SELECTED == "Chromatic":
            self.create_microtonal(accuracy=-1, enabled=False)
        else:
            self.create_microtonal()
        self.sprites_dict_inversion()
        self.set_ui(text=text)
        
    def on_update(self, delta_time):
        super().on_update(delta_time)
        self.questions_left()
        if self.transition_timer is not None:
            self.transition_timer += delta_time
            if self.transition_timer >= self.transition_delay:
                self.go_to_stats()
                self.transition_timer = None 
            
        while not self.waiting_for_click:
            if self.q > 0:            
                if SELECTED == "All notes":
                    self.note = choice(SCALE_MICROTONAL)
                else:
                    self.note = choice(SCALE_CHROMATIC) 
                self.play_note(self.note)
                self.waiting_for_click = True
            else:
                break
                   
    def set_stats(self, s):
        self.previous = s
        guess = self.sprite_dict_inverted[s]
        self.change_texture_on_answ(s, guess)
        note_dict = {
            "note": self.note,
            "guess": guess,
            "correct": self.note == guess}
        ANSWERS.append(note_dict)
        self.current_answers.append(note_dict)
        self.feedback()
    
    def feedback(self):
        pass
    
    def questions_left(self, align_y=-250):
        if getattr(self, "q_left", None) and self.q_left in self.anchor.children:
            self.anchor.remove(self.q_left)            
        self.q_left = UILabel(
            text=f"Questions left: {self.q}",
            font_name=FONT_MENU,
            font_size=20,
            text_color=a.color.GRAY,
            height=80)
        self.anchor.add(
            self.q_left,
            anchor_y="top",
            align_y=align_y,
            anchor_x="center")
    
    def change_texture_on_answ(self, s, guess):
        pass
    
    def change_texture_back(self):
        pass
            
    def on_mouse_press(self, x, y, button, _, audio=False):
        super().on_mouse_press(x, y, button, _, audio=False)
        if button == a.MOUSE_BUTTON_LEFT:
            colliding_sprites = a.get_sprites_at_point((x, y), self.sprite_list)
            if colliding_sprites:
                s = colliding_sprites[-1]                    
                if s.is_enabled:
                    if self.previous:
                        self.change_texture_back()
                    self.set_stats(s)
                    self.waiting_for_click = False
                    self.q -= 1
                if self.q == 0:
                    self.transition_timer = 0.0

    def go_to_stats(self):
        game_view = StatisticsViev()
        game_view.setup()
        self.window.show_view(game_view)
    

class Training(Challenge):
    def __init__(self):
        super().__init__()
        self.right_sprite = None  
    
    def setup(self):
        super().setup(text="Training")        
        self.transition_delay = 0.7
        self.feedback() 
    
    def feedback(self):
        if not self.current_answers:
            return
        last_answer = self.current_answers[-1]
        note = last_answer["note"]
        guess = last_answer["guess"]
        correct = last_answer["correct"]
        
        for label in getattr(self, "feedback_labels", []):
            if label in self.anchor.children:
                self.anchor.remove(label)
        self.feedback_labels = []
        
        lines = [f"Played: {note}", f"Guess: {guess}"]     
        if correct:
            color = a.color.SHAMROCK_GREEN
        else:
            color = a.color.RED
        for i, line in enumerate(lines):    
            label = UILabel(
                text=line,
                font_name=FONT_MENU,
                font_size=28,
                text_color=color,
                height=80)        
            self.anchor.add(
                label,
                anchor_y="top",
                align_y=-220 - (i * 48),
                anchor_x="center")
            self.feedback_labels.append(label)
                
    def change_texture_on_answ(self, s, guess):
        if self.note == guess:
            s.set_texture(1)
        else:
            s.set_texture(2)
            self.right_sprite = self.sprite_dict[self.note]
            self.right_sprite.set_texture(1)
            
    def change_texture_back(self):
        self.previous.set_texture(0)
        if self.right_sprite:
            self.right_sprite.set_texture(0)
    
    def on_update(self, delta_time):
        super().on_update(delta_time)
        self.questions_left(align_y=-100)
        

class StatisticsViev(Synthesizer):     
    def __init__(self):
        super().__init__()
        self.statistics = self.get_statistics()
          
    def setup(self):  
        super().setup(text="Statistics")
        self.overall_stats()
        self.new_game_button()
        self.reset_stats_button()   
        self.create_diatonic(accuracy=None, enabled=False)
        self.create_chromatic(accuracy=None, enabled=False)
        self.create_microtonal(accuracy=None, enabled=False)
    
    def overall_stats(self):
        if len(ANSWERS) == 0:
            stats = 0
        else:
            right_answers = sum(note["correct"] for note in ANSWERS)
            stats = round(right_answers / len(ANSWERS) * 100, 2)
        self.anchor.add(
            UILabel(
                text=f"Right answers overall: {stats:.4g}%",
                font_name=FONT_MENU,
                font_size=26,
                text_color=a.color.GRAY),
            anchor_y="top",
            align_y=-250,
            anchor_x="center")
    
    def reset_stats_button(self):
        self.reset_stats_button = self.anchor.add(
            SideButton(
                text="Reset statistics",
                font_size = 16),
            anchor_y="top",
            align_y=-50,
            anchor_x="right",
            align_x=-250)        
        @self.reset_stats_button.event("on_click")
        def on_start(event):
            global ANSWERS
            ANSWERS = []
            game_view = StatisticsViev()
            game_view.setup()
            self.window.show_view(game_view)

    def new_game_button(self):
        self.new_game_button = self.anchor.add(
            SideButton(
                text="New Game",
                font_size = 16,
                color_dark=BUTTON_COLOR_3, 
                color_middle=BUTTON_COLOR_2, 
                color_light=BUTTON_COLOR_1),
            anchor_y="top",
            align_y=-50,
            anchor_x="center")        
        @self.new_game_button.event("on_click")
        def new_game(event):
            match GAME_VARIANT:
                case "Challenge":
                    game_view = Challenge()        
                case "Training":
                    game_view = Training()
            game_view.setup()
            self.window.show_view(game_view)    

    def _set_accuracy(self, note):
        if note not in self.statistics:
            return -1
        return self.statistics[note]["accuracy"]
    
    def create_sprites_with_labels(self, notes, accuracy=None, enabled=False, **kwargs):
        positions = self.create_sprites(notes, accuracy=accuracy, enabled=enabled, **kwargs)
        for note, (x, y) in positions.items():
            if note not in self.statistics:
                text = ""
            else:
                acc = round(self.statistics[note]["accuracy"])
                text = f"{acc}%"
            self._create_label(x, y, text=text, note=note, font=FONT_MENU, font_size=kwargs.get("font_size", 26)) 
                
    def on_draw(self):
        super().on_draw()
        self.ui_manager.draw()
                      
    @staticmethod          
    def get_statistics():
        statistics = defaultdict(lambda: {"played": 0, "correct": 0})    
        for entry in ANSWERS:
            note = entry["note"]
            statistics[note]["played"] += 1
            if entry["correct"]:
                statistics[note]["correct"] += 1                
        for note, stats in statistics.items():
            stats["accuracy"] = stats["correct"] / stats["played"] * 100
        return dict(statistics)
    
       
def main():
    window = a.Window(
        title=TITLE,
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT)
    window.center_window()
    game = MenuView()
    window.show_view(game)
    a.run()    
    
if __name__ == "__main__":
    main()