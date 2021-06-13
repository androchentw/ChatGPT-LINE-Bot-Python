
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC


def n_2_2(User_ID,exerciseList,timelist,timeString):


    Json = 'my_project_health_2021.json'
    Url = ['https://spreadsheets.google.com/feeds']

    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)

    ##使用金鑰
    Sheet = GoogleSheets.open_by_key('1KJbPRdfwhhqblx-wjuHHq7iZiiRaF4JcKZftjsg_MzI')
    ##2
    Sheets = Sheet.worksheet('Sheet2')
    sport=Sheets.col_values(1)
    htime=Sheets.col_values(2)

    ##3
    Sheets_3=Sheet.worksheet('Sheet3')
    name=Sheets_3.col_values(1)
    wei=Sheets_3.col_values(3)
    count=0

    for a in range(len(name)):
        if name[a]==User_ID:
            count=a

    summ=0
    for j in range(len(exerciseList)):
        for i in range(len(sport)):
            if exerciseList[j]==sport[i]:
                summ=summ+float(timelist[j])/60*float(wei[count])*float(htime[i])
    ss=""
    for key in exerciseList:
        ss=ss+key+","

    Sheets_4=Sheet.worksheet('Sheet4')

    ##填入數據
    quantity=[User_ID,timeString,ss[0:-1],summ]

    Sheets_4.append_row(quantity)

    print("輸入成功")
def n_n1(person):
    Json = 'my_project_health_2021.json'
    Url = ['https://spreadsheets.google.com/feeds']

    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)

    ##使用金鑰
    Sheet = GoogleSheets.open_by_key('1KJbPRdfwhhqblx-wjuHHq7iZiiRaF4JcKZftjsg_MzI')
    Sheets = Sheet.worksheet('Sheet3')
    datas = person

    Sheets.append_row(datas)
