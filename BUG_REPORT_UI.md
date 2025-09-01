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
