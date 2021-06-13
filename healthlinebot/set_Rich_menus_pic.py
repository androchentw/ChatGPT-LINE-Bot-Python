from linebot import  LineBotApi, WebhookHandler

line_bot_api = LineBotApi('09tDHaB6BkbbgAz3J/ag5Pep6H4+asC/fjZVQS7vD7vBhMnrbuv5dOV0WlxMNtMH8oVGr5FWIatAHUkapNVuhig0UVEyctIcV7YByzg0ndMndMQtahdzBSDtxlLWJfzPqr6QFTr7FqJ9YspJihgP6AdB04t89/1O/w1cDnyilFU=')
with open("linebot(rich menu).jpg", 'rb') as f:
      line_bot_api.set_rich_menu_image("richmenu-d719b6324c6c9a6cf12b153bd72f5c04", "image/jpeg", f)
