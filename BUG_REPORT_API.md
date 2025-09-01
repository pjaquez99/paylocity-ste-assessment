# API Bugs

---

## Bug 1 – PUT with invalid ID creates a new user

**Summary:**  
Sending a PUT request with an invalid ID creates a new employee instead of denying the request with an error notification, compromising data integrity.

**Steps to Reproduce:**
1. Send a PUT request to `/api/Employees/{invalid-id}` using a UUID that does not exist.  
2. Provide a valid request body with employee details.  
3. Check the employee list with `GET /api/Employees`.  

**Expected Result:**  
API should return `404 Not Found` or a validation error, since the ID does not exist.  

**Actual Result:**  
API creates a new employee instead of rejecting the request.  

**Severity:** High  

---

## Bug 2 – DELETE with invalid ID returns 200

**Summary:**  
Sending a DELETE request with an invalid ID returns a 200 Success response, potentially misleading the user into assuming they correctly deleted the employee.

**Steps to Reproduce:**
1. Send a DELETE request to `/api/Employees/{invalid-id}` with a random UUID.  
2. Check the response.  

**Expected Result:**  
API should return `404 Not Found` or similar error, since the employee does not exist.  

**Actual Result:**  
API returns `200 Success`.  

**Severity:** High  

---

## Bug 3 – GET with invalid ID returns 200 and empty body

**Summary:**  
Sending a `GET {id}` request with an invalid ID returns a 200 response instead of a 404 response.

**Steps to Reproduce:**
1. Send a GET request to `/api/Employees/{invalid-id}` with a random UUID.  
2. Check the response.  

**Expected Result:**  
API should return `404 Not Found`.  

**Actual Result:**  
API returns `200 Success` with an empty body.  

**Severity:** Medium  

---

## Bug 4 – Name fields allow invalid characters

**Summary:**  
The API allows the first name and last name parameters to include special characters such as numbers and symbols, potentially leading to misinputs not being properly and quickly identified.

**Steps to Reproduce:**
1. Send a POST or PUT request to `/api/Employees` with a payload where `firstName` and/or `lastName` contains numbers or special characters (e.g., `"123@!?"`).  
2. Save the record.  

**Expected Result:**  
API should reject the request with a validation error.  

**Actual Result:**  
API accepts the input and creates/updates the employee with an invalid name.  

**Severity:** Medium  

---

## Bug 5 – Inconsistent spelling of "Dependents" vs. "Dependants"

**Summary:**  
The UI and challenge description use the spelling **“Dependents”** while the API responses use **“Dependants”**. Although both spellings are technically correct, the inconsistency may cause confusion for developers, testers, or users. The US standard spelling is “Dependents”.

**Steps to Reproduce:**
1. Add or query an employee record with dependents.  
2. Observe the spelling in the UI vs. the API response.  

**Expected Result:**  
Consistent spelling across API, UI, and documentation. (Preferably “Dependents” to align with US English conventions and the challenge description.)  

**Actual Result:**  
UI and documentation use “Dependents” while API response uses “Dependants”.  

**Severity:** Low  

