import time

from playwright.sync_api import Page, expect
from utils.screenshot_utils import Screenshot_Capture as ss


def test_all(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/",wait_until="domcontentloaded")
    ss.capture(page, "homepage_opened")

    page.locator("#name").fill("Niraj")
    ss.capture(page, "name_entered")

    page.locator("#email").fill("niraj@test.com")
    ss.capture(page, "email_entered")

    page.locator("#phone").fill("9876543210")
    ss.capture(page, "Phone_number_entered")

    page.locator("#textarea").fill("7th Floor, MTNL Exchange, GD Somani Marg, Cuff Parade, Colaba, Mumbai - 400 005")
    ss.capture(page, "Address_entered")

    page.locator("#male").click()
    print(page.locator("#male").is_checked())
    ss.capture(page, "Gender_selected")

    days_to_select = ["Sunday", "Wednesday", "Friday"]

    options = page.locator("//label[text() = 'Days:']/following-sibling::div//label")

    for option in options.all():
        day_text = option.text_content().strip()

        print(day_text)

        if day_text in days_to_select:
            option.click()
            print(option.is_checked())
            # ss.capture(page, "Days_selected")
    ss.capture(page, "Days_selected")

    country_op = page.locator("//select[@id = 'country']//option")
    for option in country_op.all():
        country = option.text_content().strip()
        print(country)

        if country == "India":
            page.locator("//select[@id='country']").select_option(value=country)
    ss.capture(page, "Country_selected")

    colour_op = page.locator("//select[@id = 'colors']//option")
    for option in colour_op.all():
        colour = option.text_content().strip()
        print(colour)

        if colour == "Yellow":
            page.locator("//select[@id='colors']").select_option(value=colour)
    ss.capture(page, "Color_selected")

    date_input = page.locator("//input[@id='datepicker']")

    date_input.click()
    date_input.press_sequentially("05/23/2026")
    ss.capture(page, "Datepicker_selected")

    file_opened = "//input[@id = 'singleFileInput']"
    page.set_input_files(file_opened,"test_files/file1.pdf")
    page.locator("//button[normalize-space() = 'Upload Single File']").click()
    ss.capture(page, "File_selected")

    file_opened = "//input[@id = 'multipleFilesInput']"
    page.set_input_files(file_opened,["test_files/file1.pdf","test_files/file2.png"])
    page.locator("//button[normalize-space() = 'Upload Multiple Files']").click()
    ss.capture(page, "MultiFile_selected")

    # def handle_dialog(dialog):
    #     assert dialog.message == "I am an alert box!"
    #     time.sleep(5)
    #     dialog.accept()
    # page.on("dialog", handle_dialog)
    # ss.capture(page, "Simple_alert")
    # page.get_by_role("button", name="Simple Alert").click()
    #
    # page.remove_listener("dialog", handle_dialog)
    #
    # def handle_dismiss(dialog):
    #     assert dialog.message == "Press a button!"
    #     time.sleep(5)
    #     dialog.dismiss()
    # ss.capture(page, "Confirmation Alert")
    # page.on("dialog", handle_dismiss)
    # page.get_by_role("button", name="Confirmation Alert").click()

    def handle_dialog(dialog):
        if dialog.message == "I am an alert box!":
            # time.sleep(2)
            dialog.accept()

        elif dialog.message == "Press a button!":
            # time.sleep(2)
            dialog.dismiss()

        elif dialog.message == "Please enter your name:":
            # time.sleep(2)
            dialog.accept("Niraj Alert")

    page.on("dialog", handle_dialog)

    page.get_by_role("button", name="Simple Alert").click()
    ss.capture(page, "Simple_alert")

    page.get_by_role("button", name="Confirmation Alert").click()
    ss.capture(page, "Confirmation Alert")

    page.get_by_role("button", name="Prompt Alert").click()
    ss.capture(page, "Prompt Alert")

    with page.expect_popup() as popup:
        page.get_by_role("button", name="New Tab").click()

    new_page = popup.value

    new_page.wait_for_load_state()

    print(new_page.title())
    assert new_page.title() == "SDET-QA Blog"
    ss.capture(new_page, "Window Handle")

    new_page.close()
    ss.capture(page, "Window Handle closed")

    page.get_by_role("button", name="Point Me").hover()
    ss.capture(page, "Point Me")
    page.get_by_role("link", name="Mobiles").click()
    ss.capture(page, "Mobiles")

    page.get_by_role("button", name="Copy Text").dblclick()
    ss.capture(page, "Copy Text")
    assert page.locator("#field2").input_value() == "Hello World!"

    page.get_by_text("Drag me to my target").drag_to(page.get_by_text("Drop here"))
    ss.capture(page, "Drop here")