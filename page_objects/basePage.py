import random
from playwright.sync_api import Page
class BasePage:


    def __init__(self, page: Page):
        self.page = page

    def enter_user_details(self, username: str, password: str):
        
        if not username or not password:
            raise ValueError("Username and password must be provided")
       
        self.page.goto("auth/login")
        self.page.fill('input[name="username"]', username)
        self.page.fill('input[name="password"]', password)
        self.page.click('button[type="submit"]')

    def create_random_user_details(self):

        user_details : dict = {}
        first_name = ""
        middle_name = ""
        last_name = ""

        first_name = f"Automation_first_name" + random.randint(1000, 9999).__str__()
        middle_name = f"Automation_middle_name" + random.randint(1000, 9999).__str__()
        last_name = f"Automation_last_name" + random.randint(1000, 9999).__str__()
        user_details["first_name"] = first_name
        user_details["middle_name"] = middle_name
        user_details["last_name"] = last_name
        return user_details