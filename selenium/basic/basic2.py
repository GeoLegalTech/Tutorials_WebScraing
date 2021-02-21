from selenium import webdriver

class FindByIdName():

    def test(self):
        baseUrl = "https://www.holzwickede.de/amtsblatt/index.php"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//div[@id='content']/div[7]/table//form[@name='gazette_52430']/a[@href='#gazette_52430']")

        if elementByXpath is not None:
            driverprint("We found an element by xpath")


ff = FindByIdName()
ff.test()
