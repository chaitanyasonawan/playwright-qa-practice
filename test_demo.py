from playwright.sync_api import sync_playwright

def test_multiple_buttons_on_multiple_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

        for i in range(2):
            page.get_by_role("button", name="Add Element").click()

        delete_buttons = page.get_by_role("button", name="Delete")
        assert delete_buttons.count() == 2

        page.goto("https://the-internet.herokuapp.com/checkboxes", wait_until="domcontentloaded")
    
        
        
        checkboxes = page.locator('input[type="checkbox"]')
        
        assert checkboxes.count() == 2
        
        for i in range(2):
            if not checkboxes.nth(i).is_checked():
                checkboxes.nth(i).check()
        

        browser.close()
