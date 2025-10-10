import schedule
import time
import pytest


def run_pytest():
    # Run the pytest tests programmatically
    pytest.main(['-v', 'C:\\repos\\test-automation\\src\\Tests\\test_Logic.py'])


# Schedule the task to run pytest every day at a specific time (e.g., 3:00 PM)
schedule.every().day.at("16:01").do(run_pytest)

while True:
    schedule.run_pending()
    time.sleep(1)