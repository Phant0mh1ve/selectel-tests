import re
from playwright.sync_api import expect

BASE_URL = "https://selectel.ru/"

def test_homepage_opens(page):
    page.goto(BASE_URL)
    expect(page).to_have_url(BASE_URL)
    expect(page).to_have_title(re.compile(r".+"))

def test_products_menu_visible(page):
    page.goto(BASE_URL)
    expect(page.get_by_role("button", name="Продукты")).to_be_visible()

def test_contacts_visible(page):
    page.goto(BASE_URL)
    expect(page.get_by_role("link", name="sales@selectel.ru").first).to_be_visible()
