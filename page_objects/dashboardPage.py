from page_objects.basePage import BasePage


class DashBoardPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        self.menu_items_locator = page.locator("ul>li>a>span")

    def get_menu_items(self):
        return self.menu_items_locator
