"""
import webbrowser
import time
import random
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import win32api, win32con
browser_path = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
l = 0
f = open('text.txt').read().splitlines()
i = 0
j = 0
 # не должно быть открыто вкладок в мозиле, мышь не трогать до конца сеанса 
while i<1:
    print(*f)
    i=i+1
    
#print(len(f))
#print (f[2])
    #f = open('text.txt', '+')
while l<10:

    f[j]=random.choice(f)
    #f.write(*f)
    url = f[j]
    webbrowser.register('Mozilla', None, webbrowser.BackgroundBrowser('C:/Program Files/Mozilla Firefox/firefox.exe'))
    
    webbrowser.get('Mozilla').open(url)
    time.sleep(3)

    l=l+1

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
click(1050,10) #
time.sleep(1)
click(1050,10) #2
time.sleep(1)
click(1050,10) #3
time.sleep(1)
click(1050,10) #4
time.sleep(1)
click(1050,10) #5
time.sleep(1)
click(1050,10) #6
time.sleep(1)
click(1050,10) #7
time.sleep(1)
click(880,10)  #8
time.sleep(1)
click(660,10) #9
time.sleep(1)
click(440,10) #
time.sleep(1)
click(210,10)
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
sites = []
openedsites = []

driver = webdriver.Firefox(executable_path=r'C:\Users\MSII\Desktop\geckodriver.exe')
def init():
    with open("text.txt","r") as f:
        for line in f.readlines():
            sites.append(line)

def open_and_focus_new_tab():
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[len(openedsites)])

def random_open():
    count = len(sites)
    for i in range(0,count):
        open = random.choice(sites)
        driver.get(open)
        openedsites.append(open)
        sites.remove(open)
        open_and_focus_new_tab()
    driver.close()
    print("все вкладки открыты!")
    time.sleep(5)

def close_everything():
    print("закрытие вкладок")
    temp_list = openedsites.copy()
    temp_list.reverse()
    for site in temp_list:
        # Закрываем все вкладки в обратном порядке
        driver.switch_to.window(driver.window_handles[openedsites.index(site)])
        openedsites.remove(site)
        driver.close()
        time.sleep(1)
    print("Все закрыто ")

if __name__ == "__main__":
    init()
    random_open()
    close_everything()

