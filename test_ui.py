import pytest
from playwright.sync_api import Page, expect
import uuid

base_url = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login"
username = "TestUser789"
password = "&q}xCYT{VgO/"

def unique(s: str) -> str:
    # Generate random characters so each test case has unique names.
    return f"{s}-{str(uuid.uuid4())[:3]}"

def login(page: Page):
    page.goto(base_url)
    page.fill("input[name='Username']", username)
    page.fill("input[name='Password']", password)
    page.click("button[type='submit']")
    expect(page.locator("#employeesTable")).to_be_visible()

def find_row(page: Page, first_name: str, last_name: str):
    return page.locator("#employeesTable tbody tr").filter(has_text=first_name).filter(has_text=last_name)

@pytest.mark.ui
def test_add_employee(page: Page):
    login(page)

    first = unique("James")
    last = unique("Hetfield")

    # Add new employee
    page.wait_for_load_state("networkidle")
    page.locator("#add").click()
    page.fill("#firstName", first)
    page.fill("#lastName", last)
    page.fill("#dependants", "2")
    page.click("#addEmployee")

    # Assert row is in table
    row = find_row(page, first, last)
    expect(row).to_have_count(1)
    expect(row).to_contain_text("2")

@pytest.mark.ui
def test_edit_employee(page: Page):
    login(page)

    first = unique("Lars")
    last = unique("Ulrich")

    # Add a fresh employee to edit
    page.wait_for_load_state("networkidle")
    page.locator("#add").click()
    page.fill("#firstName", first)
    page.fill("#lastName", last)
    page.fill("#dependants", "1")
    page.click("#addEmployee")
    row = find_row(page, first, last)
    expect(row).to_have_count(1)

    # Edit this row
    row.locator(".fa-edit").first.click()
    new_last = "Updated"
    page.fill("#lastName", new_last)
    page.fill("#dependants", "3")
    page.click("#updateEmployee")

    # Assert changes applied
    updated_row = find_row(page, first, new_last)
    expect(updated_row).to_have_count(1)
    expect(updated_row).to_contain_text("3")

@pytest.mark.ui
def test_delete_employee(page: Page):
    login(page)

    first = "Deleted"
    last = "Employee"

    # Add employee to delete
    page.wait_for_load_state("networkidle")
    page.locator("#add").click()
    page.fill("#firstName", first)
    page.fill("#lastName", last)
    page.fill("#dependants", "0")
    page.click("#addEmployee")
    row = find_row(page, first, last)
    expect(row).to_have_count(1)

    # Delete it
    row.locator(".fa-times").first.click()
    page.click("#deleteEmployee")

    # Assert no row remains
    expect(find_row(page, first, last)).to_have_count(0)

