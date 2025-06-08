import os
import time
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new")  # ou "--headless=chrome"
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")




# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
)

logging.info("🚀 - Démarrage du scrapping")

# URL cible (via variable d’environnement)
url = os.getenv("TARGET_URL", "https://example.com")

# Delay avant la capture
delay = int(os.getenv("LOAD_DELAY", 3))

# Résolutions portrait de smartphones (width x height)
resolutions = [
    (375, 812, "iPhone_X"),
    (414, 896, "iPhone_XR"),
    (390, 844, "iPhone_12"),
    (360, 780, "Galaxy_S20"),
    (360, 760, "Pixel_5"),
    (360, 800, "Galaxy_A10"),
    (360, 640, "Galaxy_J2"),
    (375, 667, "iPhone_6_7_8"),
    (360, 740, "OnePlus_6T"),
    (360, 720, "Nokia_6_1"),
    (384, 854, "Moto_G5"),
    (375, 812, "iPhone_11_Pro"),
    (375, 812, "iPhone_12_Mini"),
    (320, 568, "iPhone_SE_1st_gen"),
    (360, 640, "Huawei_Y6"),
    (411, 823, "Galaxy_S9"),
    (393, 786, "Galaxy_S8"),
    (360, 747, "LG_G7_ThinQ"),
    (414, 896, "iPhone_11"),
    (360, 740, "Redmi_Note_8"),
    (375, 812, "iPhone_13_Mini"),
    (390, 844, "iPhone_13_14"),
    (428, 926, "iPhone_14_Pro_Max"),
    (375, 812, "iPhone_XS"),
    (412, 869, "Pixel_6"),
    (360, 780, "Pixel_4a"),
    (384, 640, "Nexus_4"),
    (411, 731, "Nexus_5X"),
    (360, 592, "Moto_E4"),
    (320, 480, "Old_Models"),
    (412, 846, "Pixel_5_2"),
    (414, 736, "iPhone_6_7_8_Plus"),
    (375, 812, "iPhone_SE_2nd_gen"),
    (412, 732, "Galaxy_A50"),
    (393, 786, "Galaxy_Note_8"),
    (360, 740, "Galaxy_Note_9"),
    (412, 869, "Pixel_6a"),
    (412, 915, "Pixel_7"),
    (360, 740, "Xiaomi_Mi_A2"),
    (360, 672, "Galaxy_J5"),
    (411, 823, "Galaxy_S10e"),
    (375, 667, "iPhone_8"),
    (412, 892, "Pixel_7a"),
    (393, 873, "Galaxy_S10_Plus"),
    (360, 720, "Honor_8"),
    (412, 915, "Pixel_7_Pro"),
    (428, 926, "iPhone_14_Pro_Max_2"),
    (375, 812, "iPhone_SE_2020"),
    (384, 854, "Sony_Xperia_M2"),
    (360, 760, "Galaxy_S21_FE"),
]

output_dir = "screenshots"
os.makedirs(output_dir, exist_ok=True)

# Sous-répertoire avec date (ex: 2025-06-07)
timestamp = datetime.now().strftime("%Y-%m-%d")
session_dir = os.path.join(output_dir, timestamp)
os.makedirs(session_dir, exist_ok=True)



# Change la taille de la fenêtre à chaque itération
for width, height, model in resolutions:
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(width, height)
    logging.info(f"{model} {width}x{height} - Chargement de la page {url}")
    driver.get(url)
    time.sleep(delay)

    # Scroll jusqu'en bas de la page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Hauteur totale
    scroll_height = driver.execute_script("return document.body.scrollHeight")

    # Redimensionner pour voir toute la page
    driver.set_window_size(width, scroll_height)
    time.sleep(1)

    filename = f"{session_dir}/screenshot_{model}_{width}x{scroll_height}.png"
    driver.save_screenshot(filename)
    logging.info(f"✅ - Capture enregistrée : {filename}")
    driver.quit()

logging.info("🎯 - Scrapping terminé avec succès.")