#encoding:utf-8
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC


def n_2_1(User_ID,eat,timeString):
    import sys
    import io


    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    ##使用者輸入

    eat = eat.replace('＋','+').replace(' ','').split('+')
    foodList = []
    quantity = []
    for food in eat:
        if '(' in food:
            index1 = food.find('(')
            index2 = food.find(')')
            foodList.append(food[:index1])
            quantity.append(int(food[index1+1:index2]))
        elif '（' in food:
            index1 = food.find('（')
            index2 = food.find('）')
            foodList.append(food[:index1])
            quantity.append(int(food[index1+1:index2]))
        else:
            foodList.append(food)
            quantity.append(1)
    print("收到了呦！")
    ##結束使用者輸入
    energy=0
    oil=0
    suger=0
    na=0
    k=0
    protein=0
    carbohydrates=0
    dietary_fiber=0
    digit=-1
    ##判斷使用者輸入的食品項目做數據更正
    for name in foodList:
        digit=digit+1
        enter=str(name)
        number=int(quantity[digit])
        if "麵" in enter:
          number=number*1.4
        elif "飯"in enter:
            number=number*2.8
        elif "奶" in enter:
            number=number*1.6
    ##開啟瀏覽器
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(50)
        driver.get("https://www.cfs.gov.hk/tc_chi/nutrient/presearch3.php")
        inputElement = driver.find_element_by_name("keyword")
    ##輸入食品項目
        inputElement.send_keys(enter)
        driver.find_element_by_name("image1").click()

    ##決定點進的頁面
        address="tbody > tr:nth-child(2)"
        prove=0
        for i in range(1,len(driver.find_elements_by_css_selector("tbody>tr"))):
            for locate in range( len(enter)):
                tt="tbody > tr:nth-child("+str(i)+")"
                if driver.find_element_by_css_selector(tt).text[locate]!=enter[locate]:
                    break;
                elif driver.find_element_by_css_selector(tt).text[-1]==enter[len(enter)-1]:
                    address=tt
                    prove=1
                if i==(len(driver.find_elements_by_css_selector("tbody>tr"))-1):
                    prove=1
            if(prove==1):
                print(1)
                break;
        driver.find_element_by_css_selector(address+" > td > ul > li > a").click()
    ##進新分頁
        for handle in driver.window_handles:
            driver.switch_to_window(handle)

    ##隱性等待50秒
        driver.implicitly_wait(50)
        prove="TraceNANDtrace"
        print("7869")
    ##抓取營養素資料
        if driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[2]/td[3]").text not in prove:
            energy=energy+float(driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[2]/td[3]").text)*number
        if driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[4]/td[3]").text not in prove:
            protein=protein+float(driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[4]/td[3]").text)*number
        if driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[5]/td[3]").text not in prove:
            carbohydrates=carbohydrates+float(driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[5]/td[3]").text)*number
        if driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[6]/td[1]").text not in prove:
            oil=oil+float(driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[6]/td[3]").text)*number
        if driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[7]/td[3]").text not in prove:
            dietary_fiber=dietary_fiber+float(driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[7]/td[3]").text)*number
        if driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[8]/td[3]").text not in prove:
            suger=suger+float(driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[8]/td[3]").text)*number
        if driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[21]/td[3]").text not in prove:
            na=na+float(driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[21]/td[3]").text)*number
        if driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[20]/td[3]").text not in prove:
            k=k+float(driver.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[20]/td[3]").text)*number
        ##driver.quit()

    print("2323")

    ##連接資料庫

    Json = 'my_project_health_2021.json'
    Url = ['https://spreadsheets.google.com/feeds']

    Connect =SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)

    ##使用金鑰
    Sheet = GoogleSheets.open_by_key('1KJbPRdfwhhqblx-wjuHHq7iZiiRaF4JcKZftjsg_MzI')
    Sheets = Sheet.worksheet('Sheet1')
    ss=""
    for key in foodList:
        ss=ss+key+","

    ##填入數據
    quantity=[User_ID,timeString,ss[0:-1],energy,protein,carbohydrates,oil,dietary_fiber,suger,na,k]

    Sheets.append_row(quantity)

    print("輸入成功")
