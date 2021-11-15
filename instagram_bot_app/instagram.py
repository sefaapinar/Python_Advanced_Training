from selenium import webdriver
import time

from selenium.webdriver.common import keys
from userinfo import username,password
from selenium.webdriver.common.keys import Keys



class Instagram:
    driver_path = "C:\pydriver\chromedriver"


    def __init__(self,username,password) -> None:
        self.driver = webdriver.Chrome(Instagram.driver_path)
        self.username = username
        self.password = password


    def signIn(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        usernameInput = self.driver.find_element_by_name('username')
        passwordInput = self.driver.find_element_by_name('password')

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        passwordInput.send_keys(Keys.ENTER)

        time.sleep(3)

       


        if self.driver.find_element_by_class_name('cmbtv'):
            el = self.driver.find_element_by_class_name('cmbtv')
            el.find_element_by_tag_name('button').click()

        time.sleep(2)

        # if self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button'):
        #     self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

        if self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]'):
            self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()

        time.sleep(1)


    def getFollowers(self,max):

        self.driver.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.driver.find_element_by_class_name("_3dEHb").find_element_by_tag_name("a").click()    
        time.sleep(2)

        model = self.driver.find_element_by_css_selector("main[role=main] ul")
        count = len(model.find_element_by_tag_name("li"))


        action = webdriver.ActionChains(self.driver) #tuşlara tıklama fonksiyonu


        print(f"takipci sayısı: {count}")

        while count <max:
            model.click()

            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)


            newCount = len(model.find_elements_by_tag_name("li"))

            if count != newCount:
                count = newCount
                print(f"takipci sayısı: {count}")
                time.sleep(1)
            else:
                break

       

        i=0
        followers = self.driver.find_element_by_class_name("PZuss").find_elements_by_tag_name("li")
        for user in followers:
            i+=i
            print(i)
            link = user.find_element_by_tag_name("a").get_attribute("href")
            print(link)

    def followUser(self,username):
        pass

    
    def followUsers(self,users):
        pass

    def unFollowUser(self,username):
        pass

    def __del__(self):
        time.sleep(2)
        self.browser.close()



app = Instagram(username,password)

app.signIn()
app.getFollowers(50)
app.followUser('abc')
app.unFollowUser('abc')