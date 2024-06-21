from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    MainLogin = (By.ID, "login_Layer")
    Username = (By.XPATH, "(//input[@type ='text'])[1]")
    Password = (By.XPATH, "(//input[@type ='password'])[1]")
    PageLogin = (By.XPATH, "//button[@type ='submit']")
    ViewProfile = (By.XPATH, "(//a[@href = '/mnjuser/profile'])[1]")
    EditButton = (By.XPATH, "(//span[@class = 'edit icon'])[1]")
    ResumeTextArea = (By.ID, "resumeHeadlineTxt")
    SaveButton = (By.XPATH, "//button[text()='Save']")


    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def Login(self):
        return self.driver.find_element(*HomePage.MainLogin)

    def userName(self):
        return self.driver.find_element(*HomePage.Username)

    def passWord(self):
        return self.driver.find_element(*HomePage.Password)

    def pageLogin(self):
        return self.driver.find_element(*HomePage.PageLogin)

    def viewProfile(self):
        return self.driver.find_element(*HomePage.ViewProfile)

    def editButton(self):
        return self.driver.find_element(*HomePage.EditButton)

    def resumeTextarea(self):
        return self.driver.find_element(*HomePage.ResumeTextArea)

    def saveButton(self):
        return self.driver.find_element(*HomePage.SaveButton)


