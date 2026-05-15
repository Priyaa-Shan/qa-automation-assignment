from pages.home_page import HomePage

def test_home_page(page):

    home = HomePage(page)

    home.navigate()

    assert "Playwright" in home.get_title()

    assert home.get_started_button.is_visible()

    assert home.navbar.is_visible()