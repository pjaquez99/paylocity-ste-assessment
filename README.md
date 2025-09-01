# Paylocity STE Assessment

This submission includes:
- **Bug reports** (API & UI) in Markdown
- **API automation** (Postman collection with assertions)
- **UI automation** (Playwright + Pytest in Python: add / edit / delete flows with assertions)

## Repository Structure
```
paylocity-ste-assessment/
├─ BUG_REPORT_API.md
├─ BUG_REPORT_UI.md
├─ api-tests/
│ └─ Paylocity_Automation_Challenge_PabloJaquez.postman_collection.json
└─ ui-tests/
  ├─ pytest.ini
  ├─ requirements.txt
  └─ tests/
    └─ test_ui.py
```

## How to Run – API Tests (Postman)
1. Open Postman → **Import** → select `api-tests/Paylocity_Automation_Challenge_PabloJaquez.postman_collection.json`.
2. If needed, update the `{{baseUrl}}` and the authorization headers.
3. Run the `API Testing` folder; assertions (`pm.test`) validate status codes and behaviors.

## How to Run – UI Tests (Playwright + Pytest)
**Prereqs:** Python 3.10+, pip.

```
cd ui-tests
# Create virtual environment if necessary
pip install -r requirements.txt
python -m playwright install
python -m pytest -v --headed tests/test_ui.py
```

To run in other browsers:

Chromium (default), Firefox, WebKit:
```
python -m pytest -v --headed --browser=chromium --browser=firefox --browser=webkit tests/test_ui.py
```
Update the login URL / credentials at the top of test_ui.py if needed.


## Notes

UI tests generate unique names per run to avoid collisions.

Tests use explicit assertions on table content and modal visibility.

Bug reports list steps to reproduce, expected vs. actual, and severity.
