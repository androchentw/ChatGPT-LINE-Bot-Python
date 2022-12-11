# 串接 OpenAI ChatGPT 機器人教學

## 前言

今天要實作的語言是 Python 版，若希望使用 Node.js 或 C# 可以左轉其他大神的：

Node.js : [memochou1993/ai-assistant](https://github.com/memochou1993/ai-assistant?fbclid=IwAR14FiBM2-FuI36QpXDcq9G52x9FuUWeI4KtfqFinJgnyA6whL2BQTZD4_k)

C# : [isdaviddong/chatGPTLineBot](https://github.com/isdaviddong/chatGPTLineBot?fbclid=IwAR1ktXUcivo8eG6MmTntY-dlG0SqyoRVyoGKEmMXHogc37jxrnxyuhrVFi4)

基本上串 ChatGPT 很簡單，尤其是 python 已經有套件的狀況下
都是看一下官方文件就可以串起來的簡單步驟
讀者們如果有 Docker 的基礎，應該二十分鐘內就可以串好並部署了！

## 懶人包

1. 申請 API key
[https://beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys)
2. 設定 .env 並放在 manage.py 旁邊

```bash
DJANGO_SECRET_KEY=secret
DATABASE_URL=sqlite://YOUR_PASSWORD/db.sqlite3
EMAIL_URL=smtp://user:YOUR_PASSWORD@localhost:25
LINE_CHANNEL_ACCESS_TOKEN=
LINE_CHANNEL_SECRET=
CHAT_GPT_TOKEN=
```

3. 部署
    1. 申請 line 官方帳號[這篇](https://ithelp.ithome.com.tw/users/20117701/ironman/2634)
    2. docker 安裝[連結](https://www.docker.com/products/docker-desktop/)
    3. ngrok 安裝[這篇](https://ithelp.ithome.com.tw/articles/10197345)
    4. docker compose up -d

## 以下正式教學

### 第一步：到 openAI 網站申請 `API key`

連結在這：[https://beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys)

切記，這個 api key 不可以推上來 github 喔，可能會不明人士盜用！

![1](https://user-images.githubusercontent.com/96360357/206909022-2dcb4fff-5b27-411d-94bb-cb6194099c9b.png)

### 第二步：使用 .env 來設定環境變數

我在 repo 中有放置 `.env.sample` ，大家可以根據自己的環境設置不一樣的變數

[https://github.com/Lanznx/HealthLineBot/blob/main/.env.sample](https://github.com/Lanznx/HealthLineBot/blob/main/.env.sample)

```bash
DJANGO_SECRET_KEY=secret
DATABASE_URL=sqlite://YOUR_PASSWORD/db.sqlite3
EMAIL_URL=smtp://user:YOUR_PASSWORD@localhost:25
LINE_CHANNEL_ACCESS_TOKEN=
LINE_CHANNEL_SECRET=
CHAT_GPT_TOKEN=
```

這邊要注意的是，你的 `.env` 應該要放置於跟 `manage.py` 相同的路徑底下

這樣我在專案設定的路徑 `ENV_PATH = ".env"`才吃的到環境變數喔！

再來是 google 金鑰憑證的部分，這個金鑰是我朋友的陳年老金鑰，我想說方便才拿它來串 ChatGPT

我已經盡量把需要的地方拆出來了，但礙於申請這個 google API 金鑰可能會有點麻煩

而目前感覺起來應該也不太會有爆流量的問題，所以就先暫時暴露在 github 上給大家方便吧！

如果想要把金鑰替換成自己的，可以參考以下文章申請！

[蛤！原來串接 Google Sheet API 那麼簡單?](https://ithelp.ithome.com.tw/articles/10234325)

### 第三步（可略過）：根據官方文件，你可以選擇使用 HTTP request 或者 python 套件

官方文件在這：[Create completion](https://beta.openai.com/docs/api-reference/completions/create)

但這邊我跟官方文件使用的引入方式不太一樣，是使用 python-dotenv 這個套件

但功能基本上大同小異，讀者可以自行斟酌

![2](https://user-images.githubusercontent.com/96360357/206909228-121fa235-4608-4e51-bc8b-33d8ca1ce575.png)

基本上我都寫好了，所以只要環境變數有塞進去 .env 應該就可以跑起來了

### 第四步：核心程式碼解說（可略過）

[/healthlinebot/view.py 的連結](https://github.com/Lanznx/HealthLineBot/blob/main/healthlinebot/views.py)

![截圖 2022-12-11 20.48.56.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/58c97d4b-e894-44b1-9faf-c4e2dc9d902d/%E6%88%AA%E5%9C%96_2022-12-11_20.48.56.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221211T142343Z&X-Amz-Expires=86400&X-Amz-Signature=910d6ec83fc3b8fec2d53b3d8073183febe99efdd2d769952f2b4bc92c294dd2&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25E6%2588%25AA%25E5%259C%2596%25202022-12-11%252020.48.56.png%22&x-id=GetObject)

我在第十三行引入 `openai` 的官方套件，並且完成 .env 的載入

這個套件很明顯還在實驗階段，版本只出到 0.25.0

下面是官方連結，有興趣可以看看：

[官方連結](https://pypi.org/project/openai/)

![截圖 2022-12-11 20.49.08.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/05696714-ba50-4e1f-b05b-86a0a25d9739/%E6%88%AA%E5%9C%96_2022-12-11_20.49.08.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221211T142418Z&X-Amz-Expires=86400&X-Amz-Signature=c9a4e2c7dd37461579ac8b74e17d9184a2fb5de7669320ad13da185a8e31e632&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25E6%2588%25AA%25E5%259C%2596%25202022-12-11%252020.49.08.png%22&x-id=GetObject)

接下來就是整個程式碼最核心的部分了！！

我定義了 `chatGPT` 這個函式，`text` 是使用者回覆的訊息

然後我呼叫了 `openai.Completion.create` 這個函式

必填的參數只有一個，就是一定要指定 model

而我所使用的語言模型是 `text-davinci-003` ，跟大家一般在網頁版所看到的並不一樣

但這部分我沒有多做研究，可能網頁版的模型已經釋出 API 讓大家玩了？

歡迎大家可以研究一下並讓我知道喔！

總之我覺得目前這個已經很厲害了

來簡單解釋一下我現在填進去的參數

1. model: 這個就不解釋了，可以在這裡查看所有的語言模型種類
    1. [https://beta.openai.com/docs/api-reference/models/list](https://beta.openai.com/docs/api-reference/models/list)

2. prompt：使用者輸入的訊息，給模型的 input

3. max_tokens：模型回覆的長度
    1. 大部分的模型可以支援到 2048 個 token，就是回覆很長很多的意思！
    2. 詳細定義可以看這裡：[https://beta.openai.com/tokenizer](https://beta.openai.com/tokenizer)

4. temperature：溫度，我把它解讀為人性的「溫度」
    1. 這個參數應該是介於 0 ~ 1 之間，預設為 1
    2. 設成 0 的話模型給出的回覆會很無聊，1 的話會很更 creative，我自己是設定中庸的 0.8

![截圖 2022-12-11 21.07.43.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/376448e2-93a1-4227-b3d2-bd1d63a409b9/%E6%88%AA%E5%9C%96_2022-12-11_21.07.43.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221211T142516Z&X-Amz-Expires=86400&X-Amz-Signature=4dba463f5f5e192744c2ea656c361da148399cfe3c3e71204a4e708cab7ef81b&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25E6%2588%25AA%25E5%259C%2596%25202022-12-11%252021.07.43.png%22&x-id=GetObject)

最後最後，只要使用者不是輸入我們指定的字，我們就可以透過呼叫剛剛定義好的 `chatGPT` 這個函式來用 text-davinci-003 模型來回覆使用者囉！

### 第五步：部署

我使用了 docker 去做打包，所以部署起來特別的方便

如果你是沒有用過 docker 的讀者，可以參考這篇[教學](https://github.com/twtrubiks/docker-tutorial)學習一下

也可以用官方的[連結](https://www.docker.com/products/docker-desktop/)安裝

最後我是開放 8000 port，如果希望使用別的 port 來開通服務的話可以去改

`docker-compose.yaml` 當中的 `8000:8000` 把左邊的八千改成你想要的 port

```bash
version: '3.8'

services:
  server:
    container_name: bot
    build:
      context: .
    ports:
      - 8000:8000 // 改左邊的 8000，他代表 host_port，右邊是 container_port 不用動
    restart: always
```

Ngrok 的教學可以參考[這篇](https://ithelp.ithome.com.tw/articles/10197345)

架設 Linebot 的教學可以參考[這篇](https://ithelp.ithome.com.tw/users/20117701/ironman/2634)

---
!!! 注意 !!!
感謝你的注意

Line Webhook URL 的路徑我是設定 `/healthlinebot/callback`

Line Webhook URL 的路徑我是設定 `/healthlinebot/callback`

Line Webhook URL 的路徑我是設定 `/healthlinebot/callback`

也就是 `https://BASE_URL/healthlinebot/callback`

很重要，所以我要講三遍，這是一個很容易踩雷的部分
---

最後輸入 `docker compose up -d` 以及 `Ngrok 8000`

就可以部署囉！

### 進階：圖文選單設定

我在底下有放我當初設定這個圖文選單的 postman 設定

可以透過 import 進來，然後把參數改成自己的

[https://api.postman.com/collections/20112142-5056931c-5f27-493c-8e59-99383408e5f6?access_key=PMAT-01GKZYJG9R0K17VPR3QEAEWYZT](https://api.postman.com/collections/20112142-5056931c-5f27-493c-8e59-99383408e5f6?access_key=PMAT-01GKZYJG9R0K17VPR3QEAEWYZT)

教學的話可以參考[這篇](https://ithelp.ithome.com.tw/articles/10294287)

恭喜大家！終於完成了一個附加功能有點多的 OpenAI 聊天機器人
還偷渡了一些 docker 進來
如果成功的話歡迎讓我知道你完成了！
也很歡迎點個星星或 fork 過去改寫喔！
