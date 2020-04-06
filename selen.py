from selenium import webdriver
import time

class Jobs_tut_by_bot(object):
    def __init__(self, driver):
        self.driver = driver
        self.label_show = []
        self.site_form = []
        self.login = "YourLogin"
        self.password = "YourPassword"
        self.button = []
        self.button_update = []
        #self.pas = pas
        #self.log = log

    def parse(self):
        self.go_to_page()
        time.sleep(5)

    def go_to_page(self):
        site = 'https://jobs.tut.by/account/login?backurl=%2F'
        self.driver.get(site)
        self.find_form()

    def find_form(self):
        self.site_form1 = self.driver.find_element_by_name("username")
        print(self.site_form1.get_attribute("name"))

        self.site_form2 = self.driver.find_element_by_name("password")
        print(self.site_form2.get_attribute("name"))

        self.button = self.driver.find_element_by_class_name("account-form-actions")
        
        #for input in site_form1:
        #    self.label_show = input.get_attribute("name")
        #    print(self.label_show)
        self.enter_values()

    def enter_values(self):
        self.site_form1.send_keys(self.login)
        self.site_form2.send_keys(self.password)
        self.button.click()
        self.go_to_update_page()

    def go_to_update_page(self):
        site_update = 'https://jobs.tut.by/applicant/resumes?from=header_new'
        self.driver.get(site_update)
        self.find_button_update()

    def find_button_update(self):
        self.button_update = self.driver.find_element_by_class_name("applicant-resumes-action")
        text_update = self.button_update.text
        print(text_update) 


        


def main():
    driver = webdriver.Chrome()
    parser = Jobs_tut_by_bot(driver)
    parser.parse()
    #login = log("login")
    #password = pas('password')

if __name__ == "__main__": # to start the programm 
    main()