import re
from playwright.sync_api import expect

BASE_URL = "https://selectel.ru/"

def test_eng_version_opens(page):
    page.goto(BASE_URL)

    page.get_by_role("button", name="RU").click()
    page.get_by_role("link", name="ENG").click()

    expect(page).to_have_url(re.compile(r"/en/?$|selectel\.com"))
