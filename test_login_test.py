from playwright.sync_api import sync_playwright

def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")
        
        page.fill('input[name="username"]', "tomsmith")
        page.fill('input[name="password"]', "SuperSecretPassword!")

        page.click("button[type='submit']")
        
        assert page.is_visible("text=You logged into a secure area!")
        browser.close()