class HomePage:

    def __init__(self, page):
        self.page = page

        self.get_started_button = page.locator("text=Get started")
        self.navbar = page.locator(".navbar")

    def navigate(self):
        self.page.goto("https://playwright.dev/")

    def get_title(self):
        return self.page.title()