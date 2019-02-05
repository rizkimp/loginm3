from selenium import webdriver

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    context.browser = webdriver.Chrome(executable_path='../features/browsers/chromedriver',chrome_options=options)
    #context.browser = webdriver.Chrome('../features/browsers/chromedriver')
    context.browser.maximize_window()
    context.browser.implicitly_wait(10)

def after_all(context):
    context.browser.quit()
