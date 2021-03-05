from selenium import webdriver


def open_driver(url):
    """
    Open the webpage from the given url.
    :param url: link to webpage
    :return: driver object
    """

    # Defining firefox webdriver
    driver = webdriver.Firefox(executable_path='/lib/geckodriver-v0.27.0-linux64/geckodriver')

    driver.get(url)

    return driver


def wait_for_login_page_to_load(driver):
    """
    Checks if some elements exist on the page to see if the page is loaded
    :param driver: webdriver
    :return: nothing
    """
    xpath_email_field = '//*[@id="email"]'
    # Check if the email field is on the page (in case we're on the login page) and check if the dashboard/schedule
    #   title element exists (in case we're on the dashboard/schedule page).
    while len(driver.find_elements_by_xpath(xpath_email_field)) == 0:
        print('waiting for login page to load ...')


def wait_for_dashboard_to_load(driver):
    """
    Checks if some elements exist on the page to see if the page is loaded
    :param driver: webdriver
    :return: nothing
    """
    # xpath_dashboard_schedule_box = '/html/body/div/div/div[1]/div[2]/main/div/div/div/div[1]/div/div/div/div'
    # xpath_dashboard_no_events_box = '/html/body/div/div/div[1]/div[2]/main/div/div/div/div[1]/div/div/div/h3/span'
    xpath = '/html/body/div/div/div[1]/div[2]/main/div/div/div/div[1]/div/div/div'

    while len(driver.find_elements_by_xpath(xpath)) == 0:
        print('waiting for dashboard to load')


def wait_for_schedule_to_load(driver):
    """
    Checks if some elements exist on the page to see if the page is loaded
    :param driver: webdriver
    :return: nothing
    """

    # Check if the email field is on the page (in case we're on the login page) and check if the dashboard/schedule
    #   title element exists (in case we're on the dashboard/schedule page).
    while len(driver.find_elements_by_class_name('event-content')) == 0:
        print('waiting for schedule page to load ...')


def login_page(driver):
    """
    Checks if the current page is the login page
    :param driver: webdriver
    :return: boolean
    """
    xpath_email_field = '//*[@id="email"]'
    if len(driver.find_elements_by_xpath(xpath_email_field)) > 0:
        return True
    else:
        return False


def login(driver, eml, password):
    """
    Fill in the user email and password and press enter.
    :param driver: webdriver
    :param eml: user email
    :param password: user password
    :return: nothing
    """
    xpath_email_field = '//*[@id="email"]'
    xpath_password_field = '//*[@id="password"]'
    xpath_enter_button = '//*[@id="submit"]'

    driver.find_element_by_xpath(xpath_email_field).clear()
    driver.find_element_by_xpath(xpath_email_field).send_keys(eml)
    driver.find_element_by_xpath(xpath_password_field).clear()
    driver.find_element_by_xpath(xpath_password_field).send_keys(password)
    driver.find_element_by_xpath(xpath_enter_button).click()


def go_to_schedule(driver):
    """
    Opens the schedule page.
    :param driver: webdriver
    :return: nothing
    """

    xpath_dashboard_schedule_box = '/html/body/div/div/div[1]/div[2]/main/div/div/div/div[1]/div/div/div/div'
    xpath_dashboard_no_events_box = '/html/body/div/div/div[1]/div[2]/main/div/div/div/div[1]/div/div/div/h3/span'

    if len(driver.find_elements_by_xpath(xpath_dashboard_schedule_box)) > 0:
        driver.find_element_by_xpath(xpath_dashboard_schedule_box).click()
    elif len(driver.find_elements_by_xpath(xpath_dashboard_no_events_box)) > 0:
        driver.find_element_by_xpath(xpath_dashboard_no_events_box).click()


def get_days(driver):
    """
    Returns a list with the days as webelement of the week (monday - friday)
    :param driver: webdriver
    :return: list with webelement objects days (containing the lessons)
    """

    ls = []

    for day in driver.find_elements_by_class_name('day'):
        if len(ls) < 5:
            ls.append(day)

    return ls


def get_week_date(driver):
    """
    Returns the dates of the week.
    :param driver: webdriver
    :return: list of dates (
    """
    xpath_date = '/html/body/div/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div/h3'
    return driver.find_element_by_xpath(xpath_date).text


def get_lessons_of_day(day):
    """
    Returns the lessons as a string for the given day webelement
    :param day: day webelement
    :return: dictionary with day as key and list with lessons as value
    """

    day_lessons = []

    to_iterate = day.find_elements_by_class_name('event-content')
    to_iterate.reverse()

    for lesson in to_iterate:
        text = lesson.text
        day_lessons.append(text)

    return day_lessons


def parse_all_days(strings_of_days):
    """
    Returns a dictionary of lessons for each day as strings
    :param strings_of_days: full strings for all the days of the week (need to be parsed)
    :return: dictionary of lessons for each day as strings
    """
    result = {}

    monday = parse_list(strings_of_days[0])
    tuesday = parse_list(strings_of_days[1])
    wednesday = parse_list(strings_of_days[2])
    thursday = parse_list(strings_of_days[3])
    friday = parse_list(strings_of_days[4])

    result['monday'] = monday
    result['tuesday'] = tuesday
    result['wednesday'] = wednesday
    result['thursday'] = thursday
    result['friday'] = friday

    return result


def longest_string(strings_of_days):
    """
    Returns the length of the longest string in the given
    :param strings_of_days:
    :return:
    """


def parse_list(li):
    """
    Convert the string from the given list into a usable format.
    :param li: list with text e.g. 'Computerarchitectuur en systeemsoftware: hoorcollege\n08:30-10:30'
    :return: list with converted text
    """

    ls = []

    max_len = 0

    # Find longest string
    for el in li:
        arr = el.split('\n')[0:2]
        txt = arr[0]
        if len(txt) > max_len:
            max_len = len(txt)

    # Format text
    for el in li:
        arr = el.split('\n')[0:2]
        front = arr[0].ljust(max_len)
        ls.append(front + '\t' + arr[1])

    return ls


def write_to_file(dic, date, path):
    """
    Write the
    :param dic: dictionary containing the lessons for every day
    :param date: date of the week
    :param path: path of the text file to write to
    :return: nothing
    """

    file_object = open(path, 'a')
    file_object.write('{dt}\n'.format(dt=date))
    file_object.write('\n')
    file_object.write('Monday: ' + '\n' + '\n')
    for i in dic['monday']:
        file_object.write(i + '\n')
    file_object.write('\n\n')
    file_object.write('Tuesday: ' + '\n' + '\n')
    for i in dic['tuesday']:
        file_object.write(i + '\n')
    file_object.write('\n\n')
    file_object.write('Wednesday: ' + '\n' + '\n')
    for i in dic['wednesday']:
        file_object.write(i + '\n')
    file_object.write('\n\n')
    file_object.write('Thursday: ' + '\n' + '\n')
    for i in dic['thursday']:
        file_object.write(i + '\n')
    file_object.write('\n\n')
    file_object.write('Friday: ' + '\n' + '\n')
    for i in dic['friday']:
        file_object.write(i + '\n')

    file_object.close()

def quivr_main():
    # Call functions
    d = open_driver('https://app.quivr.be')
    wait_for_login_page_to_load(d)
    if login_page(d):  # Login if we're on the login page
        login(d, input('Email: '), input('Password: '))

    wait_for_dashboard_to_load(d)
    go_to_schedule(d)
    wait_for_schedule_to_load(d)

    days = get_days(d)
    week_date = get_week_date(d)
    lessons = []
    for dy in days:
        lessons.append(get_lessons_of_day(dy))
    temp1 = parse_all_days(lessons)

    d.close()  # Close the driver
    write_to_file(temp1, week_date, '/home/jaak/Documents/KULeuven/todo.txt')
