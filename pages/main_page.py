class MainPage:
    URL = "https://selectel.ru/"

    def __init__(self, page):
        self.page = page
        self.products_menu = page.get_by_role("button", name="Продукты")
        self.eng_link = page.get_by_role("link", name="ENG")
        self.status_link = page.get_by_role("link", name="Все сервисы доступны")
        self.cloud_servers_link = page.get_by_role("link", name="Облачные серверы")

    def open(self):
        self.page.goto(self.URL)
