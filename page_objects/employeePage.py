from page_objects.basePage import BasePage
from utility import jsonUtility


class EmployeePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.add_employee_locator = page.get_by_role("button", name="Add Employee")
        self.first_name_locator = page.locator('input[name="firstName"]')
        self.last_name_locator = page.locator('input[name="lastName"]')
        self.middle_name_locator = page.locator('input[name="middleName"]')
        self.save_button_locator = page.get_by_role("button", name="Save")
        self.cancel_button_locator = page.get_by_role("button", name="Cancel")


   
    def create_new_employee(self):

        emp_details : dict = self.create_random_user_details()
        self.page.goto("pim/addEmployee")
         
        emp_details_json = jsonUtility.load_json()
        if emp_details_json["firstname"] == "random":
            first_name = emp_details["first_name"]
        else:
            first_name = emp_details_json["firstname"]

        if emp_details_json["lastname"] == "random":
            last_name = emp_details["last_name"]
        else:
            last_name = emp_details_json["lastname"]
        
        if emp_details_json["middlename"] == "random":
            middle_name = emp_details["middle_name"]
        else:   
            middle_name = emp_details_json["middlename"]

        self.first_name_locator.fill(first_name)
        self.middle_name_locator.fill(middle_name)
        self.last_name_locator.fill(last_name)
        self.save_button_locator.click()