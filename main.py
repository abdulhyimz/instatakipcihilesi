# INSTA : ABDULLAHYILAR0
# GITHUB :ABDULHYIMZ
# \*UTF-8*/

global Fore
from colorama import Fore
import click

@click.command()
@click.option("--username", "-u", help="İnstagram kullanıcı adınız")
@click.option("--password", "-p", help="İnstagram hesabınız şifresi")
@click.option("--time", "-t", help="İnstagramda geri takip yapıldıktan sonra kaç saniye sonra geri takip hesaplarını takipten çıksın")

def main(username, password, time):
    if username == None or password == None or time == None:
        print("""
   GITHUB :ABDULHYIMZ,INSTA : ABDULLAHYILAR0
Instagram geri takip hesaplarını takip ederek takipçi
kasan python programı\n
Kullanımı : python main.py [-u] username [-p] password [-t] time
--help : Yardım
-u : Instagram kullanıcı adınız
-p : Instagram şifreniz
-t : Geri takip hesaplarını takip ettikten kaç saniye sonra takipten çıksın
            """)
        exit()

    def clear():
        import os
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'mac':
            os.system('clear')
        elif os.name == 'posix':
            os.system('clear')
        else:
            os.system('clear')

    def modules():
        global webdriver
        global sleep
        global pyautogui
        global json
        from selenium import webdriver
        from time import sleep
        import pyautogui
        import json
        print(Fore.BLUE + "Modüller Yüklendi!")

    def browser():
        global driver
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("-inprivate")
        edge_options.add_argument('--headless')
        edge_options.add_argument('--disable-gpu')
        driver = webdriver.Edge(options=edge_options)
        print(Fore.BLUE + "Tarayıcı başlatıldı!")

    def login():
        try:
            browser()
            driver.get("https://www.instagram.com/")
            sleep(1.3)
            user = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input')
            pas = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')
            log = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]/button')

            user.send_keys(username)
            pas.send_keys(password)
            log.click()
            print(Fore.BLUE + "Giriş Yapıldı!")
        except Exception as ex:
            print(Fore.RED + "Giriş yapılamadı [!] : " + str(ex))

    def code():
        login()
        sleep(6)
        later = driver.find_element("xpath", '//*[@id="react-root"]/section/main/div/div/div/div/button')
        later.click()
        sleep(4)

    def find():
        code()

        sleep(1)
        user0 = ["https://www.instagram.com/gt_hanesi00/", "gt_hanesi00"]
        user1 = ["https://www.instagram.com/gt_sayfasi_m1/", "gt_sayfasi_m1"]
        user2 = ["https://www.instagram.com/gt_takip_ett1/", "gt_takip_ett1"]
        user3 = ["https://www.instagram.com/gttakipsayfam/", "gttakipsayfam"]
        user4 = ["https://www.instagram.com/gt_takipcinizz_/", "gt_takipcinizz_"]
        user5 = ["https://www.instagram.com/gt.hesabin/", "gt.hesabin"]
        user6 = ["https://www.instagram.com/geri_takip_yap2022/", "geri_takip_yap2022"]
        user7 = ["https://www.instagram.com/_geri._takip_/", "_geri._takip_"]
        user8 = ["https://www.instagram.com/gtetkinlikleri/", "gtetkinlikleri"]
        user9 = ["https://www.instagram.com/gt.ozgun/", "gt.ozgun"]

        try:
            driver.get(user0[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
            follow.click()
            clear()
            print(Fore.GREEN + "1. hesap takip edildi")
        except:
            print(Fore.RED + "1. hesap takip edilemedi")

        try:
            driver.get(user1[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
            follow.click()
            clear()
            print(Fore.GREEN + "2. hesap takip edildi")
        except:
            print(Fore.RED + "2. hesap takip edilemedi")

        try:
            driver.get(user2[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
            follow.click()
            clear()
            print(Fore.GREEN + "3. hesap takip edildi")
        except:
            print(Fore.RED + "3. hesap takip edilemedi")

        try:
            driver.get(user3[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
            follow.click()
            clear()
            print(Fore.GREEN + "4. hesap takip edildi")
        except:
            print(Fore.RED + "4. hesap takip edilemedi")

        try:
            driver.get(user4[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
            follow.click()
            clear()
            print(Fore.GREEN + "5. hesap takip edildi")
        except:
            print(Fore.RED + "5. hesap takip edilemedi")

        try:
            driver.get(user5[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
            follow.click()
            clear()
            print(Fore.GREEN + "6. hesap takip edildi")
        except:
            print(Fore.RED + "6. hesap takip edilemedi")

        try:
            driver.get(user6[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
            follow.click()
            clear()
            print(Fore.GREEN + "7. hesap takip edildi")
        except:
            print(Fore.RED + "7. hesap takip edilemedi")

        try:
            driver.get(user7[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
            follow.click()
            clear()
            print(Fore.GREEN + "8. hesap takip edildi")
        except:
            print(Fore.RED + "8. hesap takip edilemedi")

        try:
            driver.get(user8[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
            follow.click()
            clear()
            print(Fore.GREEN + "9. hesap takip edildi")
        except:
            print(Fore.RED + "9. hesap takip edilemedi")

        try:
            driver.get(user9[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
            follow.click()
            clear()
            print(Fore.GREEN + "10. hesap takip edildi")
        except:
            print(Fore.RED + "10. hesap takip edilemedi")

    def unfollower():
        find()
        sleep(1)
        user0 = ["https://www.instagram.com/gt_hanesi00/", "gt_hanesi00"]
        user1 = ["https://www.instagram.com/gt_sayfasi_m1/", "gt_sayfasi_m1"]
        user2 = ["https://www.instagram.com/gt_takip_ett1/", "gt_takip_ett1"]
        user3 = ["https://www.instagram.com/gttakipsayfam/", "gttakipsayfam"]
        user4 = ["https://www.instagram.com/gt_takipcinizz_/", "gt_takipcinizz_"]
        user5 = ["https://www.instagram.com/gt.hesabin/", "gt.hesabin"]
        user6 = ["https://www.instagram.com/geri_takip_yap2022/", "geri_takip_yap2022"]
        user7 = ["https://www.instagram.com/_geri._takip_/", "_geri._takip_"]
        user8 = ["https://www.instagram.com/gtetkinlikleri/", "gtetkinlikleri"]
        user9 = ["https://www.instagram.com/gt.ozgun/", "gt.ozgun"]
        k = 0
        while k < int(time):
            tis = int(time) - k
            clear()
            print("{0} saniye sonra takipten çıkarılmaya başlanacak!".format(str(tis)))
            k += 1
            sleep(1)
        try:
            driver.get(user0[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
            follow.click()
            sleep(0.8)
            unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            unfollow.click()
            print(Fore.GREEN + "1. hesap takipten çıkıldı")
        except:
            print(Fore.RED + "1. hesap takipten çıkarılamadı")

        try:
            driver.get(user1[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
            follow.click()
            sleep(0.8)
            unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            unfollow.click()
            clear()
            print(Fore.GREEN + "2. hesap takipten çıkıldı")
        except:
            print(Fore.RED + "2. hesap takipten çıkarılamadı")
        try:
            driver.get(user2[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
            follow.click()
            sleep(0.8)
            unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            unfollow.click()
            clear()
            print(Fore.GREEN + "3. hesap takipten çıkıldı")
        except:
            print(Fore.RED + "3. hesap takipten çıkarılamadı")

        try:
            driver.get(user3[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            follow.click()
            sleep(0.8)
            unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            unfollow.click()
            clear()
            print(Fore.GREEN + "4. hesap takipten çıkıldı")
        except:
            print(Fore.RED + "4. hesap takipten çıkarılamadı")

        try:
            driver.get(user4[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
            follow.click()
            sleep(0.8)
            unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            unfollow.click()
            clear()
            print(Fore.GREEN + "5. hesap takipten çıkıldı")
        except:
            print(Fore.RED + "5. hesap takipten çıkarılamadı")

        try:
            driver.get(user5[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
            follow.click()
            sleep(0.8)
            unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            unfollow.click()
            clear()
            print(Fore.GREEN + "6. hesap takipten çıkıldı")
        except:
            print(Fore.RED + "6. hesap takipten çıkarılamadı")

        try:
            driver.get(user6[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
            follow.click()
            sleep(0.8)
            unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            unfollow.click()
            clear()
            print(Fore.GREEN + "7. hesap takipten çıkıldı")
        except:
            print(Fore.RED + "7. hesap takipten çıkarılamadı")

        try:
            driver.get(user7[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
            follow.click()
            sleep(0.8)
            unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            unfollow.click()
            clear()
            print(Fore.GREEN + "8. hesap takipten çıkıldı")
        except:
            print(Fore.RED + "8. hesap takipten çıkarılamadı")

        try:
            driver.get(user8[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
            follow.click()
            sleep(0.8)
            unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            unfollow.click()
            clear()
            print(Fore.GREEN + "9. hesap takipten çıkıldı")
        except:
            print(Fore.RED + "9. hesap takipten çıkarılamadı")

        try:
            driver.get(user9[0])
            sleep(2)
            follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
            follow.click()
            sleep(0.8)
            unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            unfollow.click()
            clear()
            print(Fore.GREEN + "10. hesap takipten çıkıldı")
        except:
            print(Fore.RED + "10. hesap takipten çıkarılamadı")

    def end():
        unfollower()


    modules()
    end()

main()