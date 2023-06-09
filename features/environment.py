from selenium import webdriver
from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from app.application import Application
#from support.logger import logger, MyListener
# from selenium.webdriver.firefox.options import Options


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    service = Service('/Users/emreisik/CureSkin-Project/chromedriver')
    # service = Service('/Users/emreisik/CureSkin-Project/geckodriver')

    context.driver = webdriver.Chrome(service=service)
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox(service=service)
    # options = Options()
    # options.headless = True
    # context.driver = webdriver.Firefox(options=options)

    # # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )

    # fireFoxOptions = webdriver.FirefoxOptions()
    # fireFoxOptions.set_headless()
    # fireFoxOptions.add_argument('--private')
    # #fireFoxOptions.add_argument('--headless')
    # context.driver = webdriver.Firefox(
    #     firefox_options=fireFoxOptions,
    #     service=service
    # )


    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(
    #     webdriver.Chrome(service=service),
    #     MyListener()
    # )
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    # for browerstack ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings

    desired_cap = {
        'browserName': 'Chrome',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '11',
            'sessionName': test_name
        }
    }
    bs_user ='emreik_8BQhaI'
    bs_key = 'ZPjRgU4NMcWimhWsx7JE'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    mobile_emulation = {"deviceName": "Galaxy S5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(executable_path='/chromedriver.exe', chrome_options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    # context.app = Application(driver=context.driver)
    context.app = Application(context.driver)

#  ALLURE =behave -f allure_behave.formatter:AllureFormatter -o test_results/features/tests etc..

#allure serve test_results/ == to launch allure web page


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'Started Scenario:{scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    # logger.info(f'Started Step:',step)
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        # logger.error(f'Step Failed:{step}')
        print('\nStep failed: ', step)
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

