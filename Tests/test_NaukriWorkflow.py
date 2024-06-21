import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.NaukriTestData import HomePageData
from PageObjects.NaukriPageObjects import HomePage
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_Login(self, getData):
        homepage = HomePage(self.driver)
        homepage.Login().click()
        print("Clicked on login button")
        time.sleep(5)
        homepage.userName().send_keys(getData["username"])
        homepage.passWord().send_keys(getData["password"])
        homepage.pageLogin().click()
        time.sleep(5)
        homepage.viewProfile().click()
        time.sleep(5)
        homepage.editButton().click()
        homepage.resumeTextarea().clear()
        homepage.resumeTextarea().send_keys(HomePageData.test_HomePage_data1)
        homepage.saveButton().click()
        time.sleep(5)


    @pytest.fixture(params=HomePageData.test_HomePage_data)

    def getData(self, request):
        return request.param

