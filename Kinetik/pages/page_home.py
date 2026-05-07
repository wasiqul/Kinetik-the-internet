from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.environment_url_1 = "https://the-internet.herokuapp.com/login"
        self.environment_url_2 = "https://www.example.com/"
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, environment_url: str, username: str, password: str):
        self.page.goto(environment_url)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()