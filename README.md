# Playwright_Spring2026

Playwright test automation project for nop-qa.portnov.com e-commerce site testing.

## Setup

### Clone the repository
```bash
git clone https://github.com/EllieSky/Playwright_Spring2026.git
cd Playwright_Spring2026
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Install Playwright browsers
```bash
playwright install
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/test_login_logout.py
```

### Run with verbose output
```bash
pytest -vv
```

### Run in headed mode (show browser)
```bash
pytest --headed
```

## Mobile Testing

Mobile tests use the `@pytest.mark.mobile` marker and require the `MOBILE` environment variable to be set.

### Run mobile tests
```bash
export MOBILE="iPhone 15" && pytest -m "mobile" tests/test_mobile_categories_view.py -vv
```

### Available mobile devices
Common Playwright device names include:
- iPhone 15
- iPhone 14
- iPhone 13
- iPad Pro
- iPad (gen 11)
- Pixel 5
- Galaxy S9

## Test Markers

The project uses pytest markers to categorize tests:

- `@pytest.mark.mobile` - Tests that run on mobile devices
- `@pytest.mark.desktop-only` - Tests that only run in full browser window

Run tests by marker:
```bash
pytest -m mobile
pytest -m "not mobile"
pytest -m desktop-only
```

## Project Structure

- `tests/` - Test files
- `menus/` - Page object classes (UserMenu, HeaderMenu)
- `fixtures/` - Pytest fixtures (menu, new_user, extended_page)
- `conftest.py` - Pytest configuration and fixtures
- `config.py` - Centralized configuration
- `pytest.ini` - Pytest settings and markers