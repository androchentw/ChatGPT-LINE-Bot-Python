##解決matplotlib中文字體問題: https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/359974/\n",
import numpy as np
import matplotlib.pyplot as plt
##
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from datetime import datetime
def n_n_2_4(User_ID,timeString):
    Json = 'my_project_health_2021.json'
    Url = ['https://spreadsheets.google.com/feeds']
    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)

    ##使用金鑰
    Sheet = GoogleSheets.open_by_key('1KJbPRdfwhhqblx-wjuHHq7iZiiRaF4JcKZftjsg_MzI')
    ##2
    Sheets = Sheet.worksheet('Sheet2')

    ##3
    Sheets_3=Sheet.worksheet('Sheet3')
    name=Sheets_3.col_values(1)
    hei=Sheets_3.col_values(2)
    wei=Sheets_3.col_values(3)
    count=0
    for a in range(len(name)):
        if name[a]==User_ID:
            count=a

    height = float(hei[count])
    weight = float(wei[count])
    max_calories = 40*weight


    date=datetime.date(datetime(year=int(timeString[0:4]), month=int(timeString[5:7]), day=int(timeString[8:10])))
    #使用isoweekday()函式，得出0~6表示星期一到星期日
    n=int(str(date.isoweekday()))
    print(n)
    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if n==2:
        week = [ "Tue", "Wed", "Thu", "Fri", "Sat","Sun","Mon"]
    elif n==3:
        week = [ "Wed", "Thu", "Fri", "Sat", "Sun","Mon","Tue"]
    elif n==4:
        week = [ "Thu", "Fri", "Sat", "Sun", "Mon","Tue","Wed"]
    elif n==5:
        week = [ "Fri", "Sat", "Sun", "Mon", "Tue","Wed","Thu"]
    elif n==6:
        week = [ "Sat", "Sun", "Mon", "Tue", "Wed","Thu","Fri"]
    elif n==7:
        week = [ "Sun", "Mon", "Tue", "Wed", "Thu","Fri", "Sat"]


    Sheets = Sheet.worksheet('Sheet1')

    people=Sheets.col_values(1)
    ptime=Sheets.col_values(2)
    co=Sheets.col_values(4)


    daily_calories_lst=[]
    breakfast_calories_lst=[]
    lunch_calories_lst=[]
    dinner_calories_lst=[]


    Total=0
    bTotal=0
    lTotal=0
    dTotal=0
    ##day
    wday=""

    for i in range (1,8):
        Total=0
        bTotal=0
        lTotal=0
        dTotal=0
        re=int(timeString[8:10])-(8-i)
        if re<10:
            re="0"+str(re)
        wday=timeString[0:8]+str(re)
        for i in range( len(people)):
            if people[i]==User_ID and ptime[i][0:10]==wday[0:10]:
                Total=Total+float(co[i])
            if people[i]==User_ID and ptime[i][0:10]==wday[0:10] and int(str(ptime[i][11:13]))<11:
                bTotal=bTotal+float(co[i])
                ##lun
            elif people[i]==User_ID and ptime[i][0:10]==wday[0:10] and int(str(ptime[i][11:13]))<15:
                lTotal=lTotal+float(co[i])
                #din
            elif people[i]==User_ID and ptime[i][0:10]==wday[0:10] and int(str(ptime[i][11:13]))<24:
                dTotal=dTotal+float(co[i])
        daily_calories_lst.append(Total)
        breakfast_calories_lst.append(bTotal)
        lunch_calories_lst.append(lTotal)
        dinner_calories_lst.append(dTotal)


    x = week
    fig1 = plt.figure(figsize=(5, 5))
    breakfast_calories_lst = np.array(breakfast_calories_lst)
    lunch_calories_lst = np.array(lunch_calories_lst)
    dinner_calories_lst = np.array(dinner_calories_lst)
    plt.bar(x, breakfast_calories_lst, color=['lightsteelblue'],  tick_label = week)
    plt.bar(x, lunch_calories_lst, bottom=breakfast_calories_lst, color='blue', tick_label=week)
    plt.bar(x, dinner_calories_lst, bottom=breakfast_calories_lst+lunch_calories_lst, color='mediumblue', tick_label=week)
    plt.ylabel('大卡數', fontproperties="Microsoft JhengHei")
    plt.title('本週攝取大卡數長條圖',fontproperties="Microsoft JhengHei")
    plt.axhline(y=max_calories, c="r", ls="--", lw=2)

    fig1.savefig("calories_bar.jpg", dpi=500)
    import sys
    import io
    import os

    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import requests


    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(50)
    driver.get("https://img.onl/")

    place=['C:/Users/User/NTUproject/mylinebot00/calories_bar.jpg']
    driver.implicitly_wait(10)

    driver.find_element_by_xpath('//*[@id="file-select"]').send_keys(place)##//*[@id="anywhere-upload-input"]
    driver.find_element_by_xpath('//*[@id="termsCheckbox"]').click()
    driver.find_element_by_xpath('//*[@id="terms_agree_button"]').click()
    time.sleep(10)

    URLL=driver.find_element_by_xpath('//*[@id="result_img_link"]').text
    return(URLL)
