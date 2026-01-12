from playwright.sync_api import Page


# projects page navigation test


def test_projects(page: Page):

    page.goto("https://ultimateqa.com/")

    with page.expect_navigation():
        page.get_by_role("link", name="Projects").click()

    assert "https://ultimateqaportfolio.vercel.app" in page.url
  
    
    # case About page navigation test


def test_about(page: Page):

    page.goto("https://ultimateqa.com/")

    with page.expect_navigation():
        page.get_by_role("link", name="About").nth(0).click()
        
        page.wait_for_url("**/about/")
    assert page.url.startswith("https://ultimateqa.com/about")
    
    
    # case studies page navigation test
    
    
def test_case_studies(page: Page):

     page.goto("https://ultimateqa.com/")

     with page.expect_navigation():
        page.get_by_role("link", name="Case Studies").click()
     assert "https://ultimateqa.com/case-studies/" in page.url
         
    
# blog page navigation test


def test_blog(page: Page):
    page.goto("https://ultimateqa.com/")

    # Click the first Blog link (avoids strict mode violation)
    page.get_by_role("link", name="Blog").nth(0).click()

    page.wait_for_url("**/blog/**")
    assert page.url.startswith("https://ultimateqa.com/blog")
    