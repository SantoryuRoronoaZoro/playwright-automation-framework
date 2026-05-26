import os
import allure
from datetime import datetime

class Screenshot_Capture:

    counter = 1

    @staticmethod
    def capture(page, step_name="Step"):

        # Create folder if not exists
        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_name = f"{Screenshot_Capture.counter}_{step_name}_{timestamp}.png"
        path = os.path.join("screenshots", file_name)

        # Take screenshot
        page.screenshot(path=path)

        # Attach to Allure
        allure.attach.file(
            path,
            name=file_name,
            attachment_type=allure.attachment_type.PNG
        )

        Screenshot_Capture.counter += 1