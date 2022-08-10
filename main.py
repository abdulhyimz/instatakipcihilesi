# INSTA : ABDULLAHYILAR0
# GITHUB :ABDULHYIMZ
# \*UTF-8*/

global Fore
from colorama import Fore
import click

@click.command()
@click.option("--username", "-u", help="İnstagram kullanıcı adınız")
@click.option("--loop", "-l", help="Sürekli devam etsin mi [Y/n]")
@click.option("--password", "-p", help="İnstagram hesabınız şifresi")
@click.option("--time", "-t", help="İnstagramda geri takip yapıldıktan sonra kaç saniye sonra geri takip hesaplarını takipten çıksın")

def main(username, password, time, loop):
    if username == None or password == None or time == None or loop == None:
        print("""
       GITHUB :ABDULHYIMZ,INSTA : ABDULLAHYILAR0
    Instagram geri takip hesaplarını takip ederek takipçi
    kasan python programı\n
    Kullanımı : python main.py [-u] username [-p] password [-t] time [-l] loop 
    --help : Yardım
    -u : Instagram kullanıcı adınız
    -p : Instagram şifreniz
    -t : Geri takip hesaplarını takip ettikten kaç saniye sonra takipten çıksın
    -l : Sürekli tekrarlansın mı? [Y/n]
                """)
        exit()

    if str(loop).lower() == "y":
        lop = True
    elif str(loop).lower() == "n":
        lop = False
    else:
        print("-l yerine sadece y/n girilmelidir!")
        exit()

    user_1 = "https://www.instagram.com/abdullahyilar/"
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
    user10 = ["https://www.instagram.com/gt_hanesi18383/", "gt_hanesi18383"]
    user11 = ["https://www.instagram.com/gt_sayfasi_gttakip/", "gt_sayfasi_gttakip"]
    user12 = ["https://www.instagram.com/gt.sayfasi49_/", "gt.sayfasi49_"]
    user13 = ["https://www.instagram.com/follow_back_800/", "follow_back_800"]
    user14 = ["https://www.instagram.com/follow___for___follow_____back/", "follow___for___follow_____back"]
    user15 = ["https://www.instagram.com/follow_for_followback_army/", "follow_for_followback_army"]

    while lop == True:
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
            from selenium import webdriver
            from time import sleep
            print(Fore.BLUE + "Modüller Yüklendi!")

        def browser():
            try:
                global driver
                edge_options = webdriver.EdgeOptions()
                edge_options.add_argument("-inprivate")
                '''edge_options.add_argument('--headless')
                edge_options.add_argument('--disable-gpu')'''
                driver = webdriver.Edge(options=edge_options)
                print(Fore.BLUE + "Tarayıcı başlatıldı!")
            except Exception as ex:
                print("Hata oluştu : {0}".format(str(ex)))
                exit()

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
                exit()

        def code():
            login()
            sleep(6)
            later = driver.find_element("xpath", '//*[@id="react-root"]/section/main/div/div/div/div/button')
            later.click()
            sleep(4)

        def find():
            code()

            sleep(1)
            lister = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            def myhesap():
                try:
                    driver.get(user_1)
                    sleep(3)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                except:
                    clear()
                    if lister[16] < 3:
                        lister[16] = lister[16] + 1
                        return myhesap()

            def bir():
                try:
                    driver.get(user0[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "1. hesap takip edildi" + " :", user0[1])
                except:
                    clear()
                    print(Fore.RED + "1. hesap takip edilemedi")
                    if lister[0] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[0] = lister[0] + 1
                        return bir()

            def iki():
                try:
                    driver.get(user1[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "2. hesap takip edildi" + " :", user1[1])
                except:
                    print(Fore.RED + "2. hesap takip edilemedi")
                    if lister[1] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[1] = lister[1] + 1
                        return iki()

            def uc():
                try:
                    driver.get(user2[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "3. hesap takip edildi" + " :", user2[1])
                except:
                    print(Fore.RED + "3. hesap takip edilemedi")
                    if lister[2] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[2] = lister[2] + 1
                        return uc()

            def dort():
                try:
                    driver.get(user3[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "4. hesap takip edildi" + " :", user3[1])
                except:
                    print(Fore.RED + "4. hesap takip edilemedi")
                    if lister[3] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[3] = lister[3] + 1
                        return dort()

            def bes():
                try:
                    driver.get(user4[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "5. hesap takip edildi" + " :", user4[1])
                except:
                    print(Fore.RED + "5. hesap takip edilemedi")
                    if lister[4] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[4] = lister[4] + 1
                        return bes()

            def alti():
                try:
                    driver.get(user5[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "6. hesap takip edildi" + " :", user5[1])
                except:
                    print(Fore.RED + "6. hesap takip edilemedi")
                    if lister[5] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[5] = lister[5] + 1

                        return alti()

            def yedi():
                try:
                    driver.get(user6[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "7. hesap takip edildi" + " :", user6[1])
                except:
                    print(Fore.RED + "7. hesap takip edilemedi")
                    if lister[6] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[6] = lister[6] + 1
                        return yedi()

            def sekiz():
                try:
                    driver.get(user7[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "8. hesap takip edildi" + " :", user7[1])
                except:
                    print(Fore.RED + "8. hesap takip edilemedi")
                    if lister[7] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[7] = lister[7] + 1
                        return sekiz()

            def dokuz():
                try:
                    driver.get(user8[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "9. hesap takip edildi" + " :", user8[1])
                except:
                    print(Fore.RED + "9. hesap takip edilemedi")
                    if lister[8] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[8] = lister[8] + 1
                        return dokuz()

            def on():
                try:
                    driver.get(user9[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "10. hesap takip edildi" + " :", user9[1])
                except:
                    print(Fore.RED + "10. hesap takip edilemedi")
                    if lister[9] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[9] = lister[9] + 1
                        return on()

            def on1():
                try:
                    driver.get(user10[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "11. hesap takip edildi" + " :", user10[1])
                except:
                    print(Fore.RED + "11. hesap takip edilemedi")
                    if lister[10] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[10] = lister[10] + 1
                        return on1()

            def on2():
                try:
                    driver.get(user11[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "12. hesap takip edildi" + " :", user11[1])
                except:
                    print(Fore.RED + "12. hesap takip edilemedi")
                    if lister[11] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[11] = lister[11] + 1
                        return on2()

            def on3():
                try:
                    driver.get(user12[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "13. hesap takip edildi" + " :", user12[1])
                except:
                    print(Fore.RED + "13. hesap takip edilemedi")
                    if lister[12] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[12] = lister[12] + 1
                        return on3()

            def on4():
                try:
                    driver.get(user13[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "14. hesap takip edildi" + " :", user13[1])
                except:
                    print(Fore.RED + "14. hesap takip edilemedi")
                    if lister[13] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[13] = lister[13] + 1
                        return on4()

            def on5():
                try:
                    driver.get(user14[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "15. hesap takip edildi" + " :", user14[1])
                except:
                    print(Fore.RED + "15. hesap takip edilemedi")
                    if lister[14] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[14] = lister[14] + 1
                        return on5()


            def on6():
                try:
                    driver.get(user15[0])
                    sleep(2)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                    follow.click()
                    clear()
                    print(Fore.GREEN + "16. hesap takip edildi" + " :", user15[1])
                except:
                    print(Fore.RED + "16. hesap takip edilemedi")
                    if lister[15] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        lister[15] = lister[15] + 1
                        return on6()

            myhesap()
            bir()
            iki()
            uc()
            dort()
            bes()
            alti()
            yedi()
            sekiz()
            dokuz()
            on()
            on1()
            on2()
            on3()
            on4()
            on5()
            on6()

        def unfollower():
            find()
            sleep(1)
            liste = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            k = 0
            while k < int(time):
                tis = int(time) - k
                clear()
                print("{0} saniye sonra takipten çıkarılmaya başlanacak!".format(str(tis)))
                k += 1
                sleep(1)

            def onbir():
                try:
                    driver.get(user0[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    print(Fore.GREEN + "1. hesap takipten çıkıldı" + " :", user0[1])
                except:
                    print(Fore.RED + "1. hesap takipten çıkarılamadı")
                    if liste[0] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[0] = liste[0] + 1
                        return onbir()

            def oniki():
                try:
                    driver.get(user1[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "2. hesap takipten çıkıldı" + " :", user1[1])
                except:
                    print(Fore.RED + "2. hesap takipten çıkarılamadı")
                    if liste[1] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[1] = liste[1] + 1

                        return oniki()

            def onuc():

                try:
                    driver.get(user2[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "3. hesap takipten çıkıldı" + " :", user2[1])
                except:
                    print(Fore.RED + "3. hesap takipten çıkarılamadı")
                    if liste[2] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[2] = liste[2] + 1

                        return onuc()

            def ondort():
                try:
                    driver.get(user3[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "4. hesap takipten çıkıldı" + " :", user3[1])
                except:
                    print(Fore.RED + "4. hesap takipten çıkarılamadı")
                    if liste[3] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[3] = liste[3] + 1

                        return ondort()

            def onbes():

                try:
                    driver.get(user4[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "5. hesap takipten çıkıldı" + " :", user4[1])
                except:
                    print(Fore.RED + "5. hesap takipten çıkarılamadı")
                    if liste[4] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[4] = liste[4] + 1

                        return onbes()

            def onalti():

                try:
                    driver.get(user5[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "6. hesap takipten çıkıldı" + " :", user5[1])
                except:
                    print(Fore.RED + "6. hesap takipten çıkarılamadı")
                    if liste[5] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[5] = liste[5] + 1

                        return onalti()

            def onyedi():

                try:
                    driver.get(user6[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "7. hesap takipten çıkıldı" + " :", user6[1])
                except:
                    print(Fore.RED + "7. hesap takipten çıkarılamadı")
                    if liste[6] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[6] = liste[6] + 1

                        return onyedi()

            def onsekiz():

                try:
                    driver.get(user7[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "8. hesap takipten çıkıldı" + " :", user7[1])
                except:
                    print(Fore.RED + "8. hesap takipten çıkarılamadı")
                    if liste[7] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[7] = liste[7] + 1

                        return onsekiz()

            def ondoguz():

                try:
                    driver.get(user8[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "9. hesap takipten çıkıldı" + " :", user8[1])
                except:
                    print(Fore.RED + "9. hesap takipten çıkarılamadı")
                    if liste[8] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[8] = liste[8] + 1

                        return ondoguz()

            def yirmi():

                try:
                    driver.get(user9[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "10. hesap takipten çıkıldı" + " :", user9[1])
                except:
                    print(Fore.RED + "10. hesap takipten çıkarılamadı")
                    if liste[9] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[9] = liste[9] + 1

                        return yirmi()
            def yirmi1():

                try:
                    driver.get(user10[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "11. hesap takipten çıkıldı" + " :", user10[1])
                except:
                    print(Fore.RED + "11. hesap takipten çıkarılamadı")
                    if liste[10] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[10] = liste[10] + 1

                        return yirmi1()

            def yirmi2():

                try:
                    driver.get(user11[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "12. hesap takipten çıkıldı" + " :", user11[1])
                except:
                    print(Fore.RED + "12. hesap takipten çıkarılamadı")
                    if liste[11] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[11] = liste[11] + 1

                        return yirmi2()

            def yirmi3():

                try:
                    driver.get(user9[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "13. hesap takipten çıkıldı" + " :", user9[12])
                except:
                    print(Fore.RED + "13. hesap takipten çıkarılamadı")
                    if liste[12] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[12] = liste[12] + 1

                        return yirmi3()

            def yirmi4():

                try:
                    driver.get(user13[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "14. hesap takipten çıkıldı" + " :", user13[1])
                except:
                    print(Fore.RED + "14. hesap takipten çıkarılamadı")
                    if liste[13] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[13] = liste[13] + 1

                        return yirmi4()

            def yirmi5():

                try:
                    driver.get(user14[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "15. hesap takipten çıkıldı" + " :", user14[1])
                except:
                    print(Fore.RED + "15. hesap takipten çıkarılamadı")
                    if liste[14] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[14] = liste[14] + 1

                        return yirmi5()


            def yirmi6():

                try:
                    driver.get(user15[0])
                    sleep(4)
                    follow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button')
                    follow.click()
                    sleep(1)
                    unfollow = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    unfollow.click()
                    clear()
                    print(Fore.GREEN + "16. hesap takipten çıkıldı" + " :", user15[1])
                except:
                    print(Fore.RED + "16. hesap takipten çıkarılamadı")
                    if liste[15] < 3:
                        print(Fore.YELLOW + "Tekrar deneniyor...")
                        liste[15] = liste[15] + 1

                        return yirmi6()


            onbir()
            oniki()
            onuc()
            ondort()
            onbes()
            onalti()
            onyedi()
            onsekiz()
            ondoguz()
            yirmi()
            yirmi1()
            yirmi2()
            yirmi3()
            yirmi4()
            yirmi5()
            yirmi6()


        def end():
            unfollower()

        modules()
        end()

main()
