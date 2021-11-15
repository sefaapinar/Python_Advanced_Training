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
        self.followers = []

        self.driverProfile = webdriver.ChromeOptions()
        self.driverProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})

        self.driver = webdriver.Chrome(Instagram.driver_path, options=self.driverProfile)

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
            
            print(i)
            link = user.find_element_by_tag_name("a").get_attribute("href")
            self.followers.append(link)
            i+=1
            if i == max:
                break

        self.saveToFile(self.followers)

        def saveToFile(self,followers):
            with open("followers.txt", "w",encoding="UTF-8") as file:
                for user in followers:
                    file.write(user + "\n")
    
    def followUser(self,username):
        self.driver.get(f"https://www.instagram.com/{username}")
        time.sleep(2)

        followButton = self.driver.find_element_by_tag_name("button")

        if followButton.text =="Follow":
            followButton.click()
            time.sleep(2)
        else:
            print(f"{username} sayfasını zaten takip ediyorsunuz.")
    
    def followUsers(self,users):
        for user in users:
            self.followUser(user)

    def unFollowUser(self,username):
        self.driver.get(f"https://www.instagram.com/{username}")

        btn = self.driver.find_element_by_tag_name('button')


        if btn.text == "Message":
            self.driver.find_elements_by_tag_name('button')[1].click()
            time.sleep(2)
            
            self.driver.find_element_by_css_selector('div[role=dialog] button').click()

        else:
            print(f"{username} sayfasını zaten takip etmiyorsunuz.")

    def unFollowUers(self,users):
        for user in users:
            self.unFollowUser(user)

    def __del__(self):
        time.sleep(2)
        self.browser.close()



app = Instagram(username,password)
app.signIn()
# app.getFollowers(50)
# app.followUsers("kodevreni","yazilimataolyesi")
# app.unFollowUser('kodevreni')


# kod evreni, yazilimataolyesi