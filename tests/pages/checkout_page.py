"""Page objects for the three-step Sauce Demo checkout flow."""


class CheckoutStepOnePage:
    PATH = "/checkout-step-one.html"

    def __init__(self, page):
        self.page = page
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")

    def fill_info(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()


class CheckoutStepTwoPage:
    PATH = "/checkout-step-two.html"

    def __init__(self, page):
        self.page = page
        self.finish_button = page.locator("#finish")

    def finish(self):
        self.finish_button.click()


class CheckoutCompletePage:
    PATH = "/checkout-complete.html"

    def __init__(self, page):
        self.page = page
        self.complete_header = page.locator(".complete-header")
