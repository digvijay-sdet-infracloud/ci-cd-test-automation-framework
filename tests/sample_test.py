from email.mime import base
from math import exp
from playwright.sync_api import  expect
import pytest

from page_objects.basePage import BasePage
from page_objects.dashboardPage import DashBoardPage
from page_objects.employeePage import EmployeePage
from utility import jsonUtility

@pytest.mark.skip(reason="Demo purpose only")
def test_verify_menu_items_list(page, credentials):
    base_page = BasePage(page)
    dashboardPage = DashBoardPage(page)
    base_page.enter_user_details(credentials["username"], credentials["password"])
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    expect(dashboardPage.get_menu_items()).to_have_count(12)
    expected_menu_items = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Claim', 'Buzz']
    menu_items = dashboardPage.get_menu_items().all_inner_texts()
    assert menu_items == expected_menu_items

def test_verify_new_employee_is_created(page,credentials):
    base_page = BasePage(page)
    employee_page = EmployeePage(page)
    base_page.enter_user_details(credentials["username"], credentials["password"])
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    employee_data = jsonUtility.getJsonData("employee")
    print(employee_data)
    # employee_page.create_new_employee(employee_data)
    # page.wait_for_url("**/pim/viewPersonalDetails/**")
    # expect(page.get_by_role("heading", name="Personal Details")).to_be_visible()