
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Megnyitjuk az Instagramot")
    page.goto("https://instagram.com")

    # 1. LePeS: Megvarjuk, amig felugrik a suti ablak
    print("Varakozas a suti ablakra")
    time.sleep(4)

    # 2. LÉPÉS: Rákattintunk a süti elfogadására
    print("Sutik elfogadasa...")
    page.get_by_role("button", name="Allow all cookies").click()
    time.sleep(2) # Várunk egy kicsit, amíg eltűnik az ablak

    page.get_by_role("button", name="Log in").click(force=True)
    print("bejelentkezes")

    print("Felhasznalonev beirasa...")
    page.locator("input[name='email']").fill("Youremailhere")
    time.sleep(1)
    

    page.locator("input[name='pass']").fill("yourpasswordhere")
    time.sleep(1)
    print("kitoltve")

    
    time.sleep(50)

    page.get_by_role("link", name="Reels").click()
    time.sleep(4)
    print("get it")
   
