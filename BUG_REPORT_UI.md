# UI Bugs

---

## Bug 6 – No error notifications for invalid data entries

**Summary:**  
The UI does not provide clear error notifications when entering invalid data into the required fields, creating usability issues towards the end user.

**Steps to Reproduce:**
1. Go to the **Add Employee** form.  
2. Enter invalid data in fields (e.g., Name with >50 characters; Dependents with string text, or a number >32 or <0).  
3. Click **Add Employee**.  

**Expected Result:**  
UI should show an error notification and prevent submission.  

**Actual Result:**  
Clicking **Add Employee** does nothing, no feedback is displayed, and the record is not created.  

**Severity:** High  

---

## Bug 7 – Table sorted by ID instead of user-friendly column

**Summary:**  
The UI sorts the employee table by the randomly generated UUID of each employee, making the list inconsistent each time a new employee is added to the table.

**Steps to Reproduce:**
1. Add several employees.  
2. View the **Employees Table**.  

**Expected Result:**  
Table should be sorted by a logical column (e.g., Name, Salary, Date created) to be consistent and user-friendly.  

**Actual Result:**  
Table is sorted by UUID Id, which is random and makes the list inconsistent.  

**Severity:** Low  

---

## Bug 8 – UI becomes unresponsive after idle time

**Summary:**  
The UI stops working after idle time with no automatic logout or error notification, end-user might think the app is broken if it silently stops working.

**Steps to Reproduce:**
1. Log into the Paylocity Benefits Dashboard with valid credentials.
2. Leave the application idle for a period of time (e.g., 10–15 minutes).
3. Attempt to interact with the UI, such as:
    - Clicking Add Employee
    - Editing an existing employee
    - Deleting a record

**Expected Result:**
The application should either remain responsive and continue working after idle time, or log the user out automatically with a clear notification that the session has expired.

**Actual Result:**
The UI becomes unresponsive, no logout occurs, no error or timeout notification is shown to the user and user must log in again to regain functionality.

**Severity:** Medium
