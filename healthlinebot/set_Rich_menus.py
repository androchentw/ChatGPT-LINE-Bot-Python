import requests

headers = {"Authorization":"Bearer 09tDHaB6BkbbgAz3J/ag5Pep6H4+asC/fjZVQS7vD7vBhMnrbuv5dOV0WlxMNtMH8oVGr5FWIatAHUkapNVuhig0UVEyctIcV7YByzg0ndMndMQtahdzBSDtxlLWJfzPqr6QFTr7FqJ9YspJihgP6AdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-b505834c2b157f2525072725cd525d2a',
                       headers=headers)

print(req.text)
