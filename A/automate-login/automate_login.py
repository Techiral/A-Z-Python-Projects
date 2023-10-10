from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def automate_login(username, password):
    # initialize the Chrome driver
    driver = webdriver.Chrome(r"chromedriver")
    # head to github login page
    driver.get("https://github.com/login")
    # find username/email field and send the username itself to the input field
    driver.find_element_by_id("login_field").send_keys(USERNAME)
    # find password input field and insert password as well
    driver.find_element_by_id("password").send_keys(PASSWORD)
    # click login button
    driver.find_element_by_name("commit").click()
    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    error_message = "Incorrect username or password."
    # get the errors (if there are)
    errors = driver.find_elements_by_class_name("flash-error")
    # print the errors optionally
    # for e in errors:
    #     print(e.text)
    # if we find that error message within errors, then login is failed
    if any(error_message in e.text for e in errors):
        print("[!] Login failed")
    else:
        print("[+] Login successful")
    # close the driver
    driver.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple Python script to login on github using selenium")
    parser.add_argument("username", help="Login username")
    parser.add_argument("password", help="Login password")
    args = parser.parse_args()
    automate_login(args.username, args.password)
