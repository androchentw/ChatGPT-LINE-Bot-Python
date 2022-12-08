# 啟動方式
```
docker build . -f Dockerfile -t bot

docker run -d -p 8000:8000 --name bot-container bot
```

# .env 放置位置
跟 manage.py 一樣