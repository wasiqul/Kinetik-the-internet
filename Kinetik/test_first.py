from playwright.sync_api import Page, expect
from pages.page_home import HomePage

def test_login(page: Page):

    home_page = HomePage(page)

    home_page.login(home_page.environment_url_1, "tomsmith", "SuperSecretPassword!")

    home_page.login(home_page.environment_url_2, "tomsmith", "SuperSecretPassword!") # this will fail as it's an example URL only