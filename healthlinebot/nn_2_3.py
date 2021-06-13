import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

def n_2_3(User_ID):

    Json = 'my_project_health_2021.json'
    Url = ['https://spreadsheets.google.com/feeds']

    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)

    ##使用金鑰
    Sheet = GoogleSheets.open_by_key('1KJbPRdfwhhqblx-wjuHHq7iZiiRaF4JcKZftjsg_MzI')

    ##3
    Sheets_3=Sheet.worksheet('Sheet3')
    name=Sheets_3.col_values(1)
    hei=Sheets_3.col_values(2)
    wei=Sheets_3.col_values(3)
    ag=Sheets_3.col_values(4)
    count=0

    for a in range(len(name)):
        if name[a]==User_ID:
            count=a

    BMI=float(wei[count])/((float(hei[count])/100)**2)
    perlist=[]
    perlist.append(hei[count])
    perlist.append(wei[count])
    perlist.append(ag[count])
    perlist.append(BMI)
    return perlist

def n_n(User_ID,timeString):
    Json = 'my_project_health_2021.json'
    Url = ['https://spreadsheets.google.com/feeds']

    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)

    ##使用金鑰
    Sheet = GoogleSheets.open_by_key('1KJbPRdfwhhqblx-wjuHHq7iZiiRaF4JcKZftjsg_MzI')
    ##2
    Sheets = Sheet.worksheet('Sheet1')
    people=Sheets.col_values(1)
    ptime=Sheets.col_values(2)
    co=Sheets.col_values(4)
    Total=0
    for i in range( len(people)):
        if people[i]==User_ID and ptime[i][0:10]==timeString[0:10]:
            Total=Total+float(co[i])
    return Total
def n_n1(User_ID,timeString):
    Json = 'my_project_health_2021.json'
    Url = ['https://spreadsheets.google.com/feeds']

    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)

    ##使用金鑰
    Sheet = GoogleSheets.open_by_key('1KJbPRdfwhhqblx-wjuHHq7iZiiRaF4JcKZftjsg_MzI')
    ##2
    Sheets = Sheet.worksheet('Sheet1')
    people=Sheets.col_values(1)
    ptime=Sheets.col_values(2)
    co=Sheets.col_values(4)

    oil=Sheets.col_values(7)
    suger=Sheets.col_values(9)
    na=Sheets.col_values(10)
    k=Sheets.col_values(11)
    protein=Sheets.col_values(5)
    carbohydrates=Sheets.col_values(6)
    dietary_fiber=Sheets.col_values(8)
    category=[0,0,0,0,0,0,0]
    Total=0
    for i in range( len(people)):
        if people[i]==User_ID and ptime[i][0:10]==timeString[0:10]:
            category[0]=str(float(category[0])+float(protein[i]))
            category[1]=str(float(category[1])+float(oil[i]))
            category[2]=str(float(category[2])+float(carbohydrates[i]))
            category[3]=str(float(category[3])+float(dietary_fiber[i]))
            category[4]=str(float(category[4])+float(suger[i]))
            category[5]=str(float(category[5])+float(na[i]))
            category[6]=str(float(category[6])+float(k[i]))
    return category
