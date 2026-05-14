class RestaurantPage:

    def __init__(self, page):
        self.page = page
        self.results = page.locator("li")

    def navigate(self):
        self.page.goto("file:///C:/Projects/qa-automation-assignment/test_data/restaurants.html")

    def get_results_count(self):
        return self.results.count()