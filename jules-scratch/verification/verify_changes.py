from playwright.sync_api import sync_playwright, expect
import os

def run_verification(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    file_path = os.path.abspath('trash3.html')
    file_url = f'file://{file_path}'

    # 1. Verify "For Family & Friends" section on Contact Us page
    page.goto(f'{file_url}#contact')
    family_friends_section = page.locator('h2:has-text("For Family & Friends 👨‍👩‍👧‍👦")')
    expect(family_friends_section).to_be_visible()
    page.screenshot(path="jules-scratch/verification/contact_page.png")

    # 2. Verify "Study Guide" link on Resources page
    page.goto(f'{file_url}#resources')
    study_guide_link = page.locator('a[href="#study-guide"]')
    expect(study_guide_link).to_be_visible()
    page.screenshot(path="jules-scratch/verification/resources_page.png")

    # 3. Verify "Study Guide" back button
    study_guide_link.click()
    back_button = page.locator('button:has-text("← Back to Resources")')
    expect(back_button).to_be_visible()
    back_button.click()
    expect(page).to_have_url(f"{file_url}#resources")
    page.screenshot(path="jules-scratch/verification/study_guide_back_button.png")

    # 4. Verify "Resources" link is not in navigation
    desktop_nav = page.locator('div.hidden.lg\\:flex a[href="#resources"]')
    expect(desktop_nav).to_have_count(0)

    mobile_nav = page.locator('#mobile-menu a[href="#resources"]')
    expect(mobile_nav).to_have_count(0)

    print("All verifications passed!")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run_verification(playwright)