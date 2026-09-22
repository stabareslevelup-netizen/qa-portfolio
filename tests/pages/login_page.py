"""Page object for the Sauce Demo login page (saucedemo.com/)."""


class LoginPage:
    PATH = "/"

    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

    def goto(self):
        self.page.goto(self.PATH)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
