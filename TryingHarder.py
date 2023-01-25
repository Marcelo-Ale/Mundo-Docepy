from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://www.reddit.com/login/", wait_until='networkidle')
    #pagina.click('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[2]/div/div[1]/a')
    #time.sleep(2)
    pagina.fill("#loginUsername", "9873241")
    pagina.fill("#loginPassword", "1234")
    pagina.click("button[type='submit']")
    time.sleep(3)
