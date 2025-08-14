import arcade 

# --- Window ---

SCREEN_WIDTH  = 1220
SCREEN_HEIGHT = 800
TITLE         = "Microtonal Guessing Game"

# --- Notes ---

DIATONIC         = ["C", "D", "E", "F", "G", "A", "B"]
CHROMATIC        = ["C♯|D♭", "D♯|E♭", None, "F♯|G♭", "G♯|A♭", "A♯|B♭", None]
MICROTONAL       = ["C𝄲", "D𝄳", "D𝄲", "E𝄳", "E𝄲|F𝄳", None, "F𝄲", "G𝄳", "G𝄲", "A𝄳", "A𝄲", "B𝄳", "B𝄲|C𝄳", None]
micro            = list(filter(lambda m: m, MICROTONAL))
SCALE_CHROMATIC  = [note for pair in zip(DIATONIC, CHROMATIC) for note in pair if note]
SCALE_MICROTONAL = [note for pair in zip(SCALE_CHROMATIC, micro) for note in pair if note]

# --- Textures fron arcade ---

TEX_TOGGLE_RED          = arcade.load_texture(":resources:gui_basic_assets/toggle/red.png")
TEX_TOGGLE_GREEN        = arcade.load_texture(":resources:gui_basic_assets/toggle/green.png")
TEX_CHECKBOX_CHECKED    = arcade.load_texture(":resources:gui_basic_assets/checkbox/blue_check.png")
TEX_CHECKBOX_UNCHECKED  = arcade.load_texture(":resources:gui_basic_assets/checkbox/empty.png")

# --- Sprite settings ---

SPRITE_SCALE = 0.8
SPRITE_POS_X = 112
SPRITE_POS_Y = 180
SPRITE_STEP  = 160
SPRITE_ANGLE = 5

# --- Fonts ---
# TODO load fonts from assets
FONT      = "Castellar"
FONT_MENU = "Agency FB"

# --- Game settings ---

PITCH = 440
GAME_VARIANT     = "Challenge"
SELECTED         = "All notes"
OCTAVE_MODIFIERS = [1,]
QUESTIONS        = 30
ANSWERS = []

# --- Links ---

LINK_ABOUT   = "https://github.com/Lians-coder/microtonal_game_synthesizer/readme.md"
LINK_PROFILE = "https://github.com/Lians-coder"

# --- Button colors ---

BUTTON_COLOR_1 = arcade.color.LEMON_CURRY
BUTTON_COLOR_2 = arcade.color.JASMINE
BUTTON_COLOR_3 = arcade.color.FLORAL_WHITE

# --- Colors ---

BATTLESHIP_GREY  = (132, 132, 130)
FLORAL_WHITE     = (255, 250, 240)
GRAY             = (128, 128, 128)
DIAMOND          = (185, 242, 255)
LIGHT_GRAY_CH    = (221, 221, 221)
BRINK_PINK       = (251, 96,  127)
SHAMROCK_GREEN   = (  0, 158, 96 )
PINK             = (255, 218, 235)
