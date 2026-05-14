import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page(request):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    yield page

    # SAFE teardown (no crash)
    try:
        if request.node.rep_call.failed:
            page.screenshot(path="screenshots/failure.png")
    except Exception:
        pass

    context.close()
    browser.close()
    playwright.stop()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)