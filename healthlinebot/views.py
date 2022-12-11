from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
from linebot import LineBotApi, WebhookParser
from .import nn_2_1,nn_2_2,nn_2_3

import datetime as dt

import openai
from dotenv import dotenv_values, load_dotenv
load_dotenv()
ENV_PATH = ".env"
CHAT_GPT_TOKEN = dotenv_values(ENV_PATH)["CHAT_GPT_TOKEN"]


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

def height_p(H):
    H=float(H)
    if H<3:
        H=H*100
    return H

def chatGPT(text):
    openai.api_key = CHAT_GPT_TOKEN
    ans = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        max_tokens=700,
        temperature=0.8
    )
    return ans['choices'][0]['text']

profile="泡泡糖有六種傳說中的魔法:\n依選單來實現魔法吧~\n1.飲食紀錄-記錄下您的飲食習慣\n2.健康精靈-判斷當日熱量是否有超標\n3.運動紀錄-記錄下您的運動習慣\n4.圖表繪製-將一週攝取熱量繪製成圖表，並顯示一週所捨取到的營養素表格\n5.計算BMI/BMR-客製化計算屬於您的BMI和BMR\n6.營養新聞推播-推播健康有關新聞，隨時可以輕鬆吸收新知\n快點擊下方的圖文選單跟我互動吧，泡泡~"
person=[0,1,2,3]
@csrf_exempt
def callback(request):

    if request.method == 'GET':
        return HttpResponse("hello")

    if request.method == 'POST':

        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:

            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            User_ID=event.source.user_id
            print(User_ID)
            timeString=str(dt.datetime.now())

            if isinstance(event, MessageEvent):  # 如果事件
                if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
                    prove=event.message.text.split(".")##判斷使用者回覆之事件
                    if event.message.text=='飲食紀錄':
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="台灣美食是泡泡最愛的了ε٩(๑> ₃ <)۶з來到這裡發現有好多好好吃的，可是為了身體健康，還是要記錄下自己吃了什麼喔，泡泡\n您今天吃了什麼？\n請以「＋」作為各項食物的分隔，數量請以（數量）表示\nEX:1.水餃(10)+珍珠奶茶+漢堡(2)"),

                            )
                    elif event.message.text=='健康精靈':
                        perlist=nn_2_3.n_2_3(User_ID)
                        TDEE=float(perlist[2])*40
                        Total=nn_2_3.n_n(User_ID,timeString)
                        if Total>(TDEE+299):
                            line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="紀錄小精靈由泡泡幫您計算今天的熱量有沒有超標喔，好緊張(((ﾟдﾟ)))........\n"+"霹靂卡霹靂拉拉波波莉娜貝貝魯多熱量計算中，今天有沒有超標呢?"+"\n \n \n"+"今日攝取:"+str(Total)+"\n(●▼●;)阿….您今天超標囉，要注意身體健康，明天再一起努力吧~愛心愛心。\n詳看今日攝取營養素，請回復「續看今日攝取營養素」")
                            )
                        elif Total<=(TDEE+299):
                            line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="紀錄小精靈由泡泡幫您計算今天的熱量有沒有超標喔，好緊張(((ﾟдﾟ)))........\n"+"霹靂卡霹靂拉拉波波莉娜貝貝魯多熱量計算中，今天有沒有超標呢?"+"\n \n \n"+"今日攝取:"+str(Total)+"\n(*´ω`)人(´ω`*)您今天沒有超標，恭喜呀!(泡泡撒花轉圈圈)最重要的是維持呦～\n詳看今日攝取營養素，請回復「續看今日攝取營養素」")
                            )
                    elif event.message.text=='運動紀錄':
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="泡泡每天的運動是飛行5小時和施魔法，都很消耗我的卡路里，你們人類也會飛嗎?\n您今天運動了嗎？\n請以「＋」作為各項運動的分隔，運動時間請以（分鐘）表示\nEX:2.游泳(60)+跑步(90)")
                            )
                    elif event.message.text=='BMI/BMR':
                        perlist=nn_2_3.n_2_3(User_ID)
                        if perlist[3] < 18.5:
                            t="\n您是過輕呦，泡泡建議您多吃一點也無妨、更助於身體健康喔!"
                        elif perlist[3] >= 24:
                            t="\n要注意均衡飲食、撥空運動，讓自己保持健康的體態才不會疾病容易找上門喔！泡泡關心您~"
                        else:
                            t="\n健康的正常體重！！您是優良模範生呢~泡泡"
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="讓我施個魔法@#$%*&!!!!!BMI計算中\n您的BMI是"+str(perlist[3])+t+"\nDO~RE~MI~SO!!!!!BMR計算中\n"+"請告訴我您的性別男/女")
                            )
                    elif event.message.text=='女':
                        perlist=nn_2_3.n_2_3(User_ID)
                        BMRg = str((10 *float(perlist[1])) + (6.25*float(perlist[0])) - (5  * float(perlist[2])) - 161)
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="您的BMR是"+BMRg+"\nBMR是基礎代謝率（Basal Metabolic Rate)，這是如果你打算躺在床上一整天不動的狀況下，要維持正常身體機能，器官繼續運作的所需消耗能量唷!")
                            )
                    elif event.message.text=='男':
                        perlist=nn_2_3.n_2_3(User_ID)
                        BMRb =  str((10 *float(perlist[1]) ) + (6.25 *float(perlist[0])) - (5 * float(perlist[2]) ) + 5)
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="您的BMR是"+BMRb+"\nBMR是基礎代謝率（Basal Metabolic Rate)，這是如果你打算躺在床上一整天不動的狀況下，要維持正常身體機能，器官繼續運作的所需消耗能量唷!")
                            )
                    elif prove[0]=="01":
                        H=height_p(prove[1])
                        person[1]=H
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="收到了呦~您的身高是"+str(H)+"公分\n"+"請告訴我您的體重(KG)，我不會告訴別人的⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄\n EX:02.45")
                            )
                    elif prove[0]=="02":
                        W=prove[1]
                        person[2]=W
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="收到了呦~您的體重是"+str(W)+"公斤\n"+"請告訴我您的年齡，偷偷跟你說喔，泡泡已經273歲了\n EX:03.19")
                            )
                    elif prove[0]=="03":
                        A=prove[1]
                        person[3]=A
                        person[0]=User_ID
                        nn_2_2.n_n1(person)
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="收到了呦~您的年齡是"+str(A)+"歲\n"+"開始享受與泡泡的健康之旅吧~Go!(｡◕∀◕｡)")
                            )
                    elif prove[0]=="1":
                        nn_2_1.n_2_1(User_ID,prove[1],timeString)
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="收到了呦!")
                            )
                    elif prove[0]=="2":
                        exercise = prove[1].replace('＋','+').replace(' ','').split('+')
                        exerciseList = []
                        timelist = []
                        flag = True
                        for sport in exercise:
                            if '(' in sport:
                                index1 = sport.find('(')
                                index2 = sport.find(')')
                                exerciseList.append(sport[:index1])
                                timelist.append(int(sport[index1+1:index2]))
                            elif '（' in sport:
                                index1 = sport.find('（')
                                index2 = sport.find('）')
                                exerciseList.append(sport[:index1])
                                timelist.append(int(sport[index1+1:index2]))
                            else:
                                flag = False
                                line_bot_api.reply_message(  # 回復傳入的訊息文字
                                    event.reply_token,
                                    TextSendMessage(text=sport+"沒有輸入到運動時間喔～\n請您再重新輸入一次"+sport+"和運動的時間呦～")
                                    )
                        if flag == True:
                            nn_2_2.n_2_2(User_ID,exerciseList,timelist,timeString)
                            line_bot_api.reply_message(  # 回復傳入的訊息文字
                                event.reply_token,
                                TextSendMessage(text="收到了呦！待在家也要多多運動呦～(｡◕∀◕｡)")
                                )
                    elif event.message.text=='續看今日攝取營養素':
                        category=nn_2_3.n_n1(User_ID,timeString)
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="今日攝取營養素:\n 蛋白質: "+category[0]+"\n脂肪: "+category[1]+"\n碳水化合物: "+category[2]+"\n膳食纖維: "+category[3]+"\n糖: "+category[4]+"\n鈉: "+category[5]+"\n 鉀: "+category[6])
                            )
                    elif event.message.text=='晚安':
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="晚風讓泡泡有沉沉欲睡的感覺Zzz...晚安")
                            )
                    elif event.message.text=='減肥諮詢':
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text="請輸入任何減肥問題，我將使用 text-davici-003 模型來嘗試解答您")
                            )
                    elif event.message.text!='你絕對不會輸入這個文字':
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TextSendMessage(text=chatGPT(event.message.text))
                            )

            elif isinstance(event, FollowEvent):
                line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="很高興可以認識您，請您告訴我您的一些基本資料，讓我來守護您吧，泡泡!\n請輸入您的身高~愛心愛心\nEx:01.158")
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()