from playwright.sync_api import expect

BASE_URL = "https://selectel.ru/"

def test_status_page_link_exists(page):
    page.goto(BASE_URL)
    link = page.get_by_role("link", name="Все сервисы доступны")
    expect(link).to_be_visible()

    href = link.get_attribute("href")
    assert href is not None
    assert "selectel.live" in href
