from pages.restaurant_page import RestaurantPage


def test_restaurant_search(page):

    restaurant_page = RestaurantPage(page)

    restaurant_page.navigate()

    assert restaurant_page.get_results_count() > 0