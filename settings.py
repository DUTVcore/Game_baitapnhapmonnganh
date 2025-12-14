# settings.py
import os
import sys

# --- CẤU HÌNH MÀN HÌNH ---
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
GAME_CAPTION = "Fruit Catcher - 2 Player Chaos"

# --- MÀU SẮC CƠ BẢN ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE_BTN = (0, 128, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)    

# PLAYERS' COLORS
COLOR_P1 = RED    
COLOR_P2 = CYAN   

# -----------------------------------------------------------------
# --- DUONG DAN ---
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(folder, filename):
    return os.path.join(BASE_DIR, folder, filename)
# -----------------------------------------------------------------

# --- TÊN FILE ẢNH CƠ BẢN ---
IMG_FILES = {
    "bucket": "bucket.png",
    "bomb": "bomb.png",
    "heart": "heart.png",
    "return": "return_to_menu.png",
    "volume": "volume.png",
    "mute": "mute.png",
    "logo": "logo_bkdn.png"
}

FRUIT_FILES = ["apple.png", "banana.png", "watermelon.png", "strawberry.png"]

# --- BG ---
BG_CONFIG = [
    ("bg_spring.png", (144, 238, 144)),  # Xuân
    ("bg_summer.png", (255, 255, 224)),  # Hạ
    ("bg_autumn.png", (255, 228, 181)),  # Thu
    ("bg_winter.png", (224, 255, 255))   # Đông
]

# --- RULES (LASTED UPDATE) ---
RULES_TEXT = [
    "--- CHE DO 1 NGUOI ---",
    "Dung PHIM MUI TEN di chuyen.",
    "Hung truot trai cay se mat mang!",
    "",
    "--- CHE DO 2 NGUOI ---",
    "P1: Mui ten | P2: Phim A, D",
    "Moi nguoi co mang rieng biet.",
    "Hung truot KHONG bi tru mang.",
    "LUU Y: Chi can 1 nguoi het mang,",
    "Game se KET THUC ngay lap tuc!",
]