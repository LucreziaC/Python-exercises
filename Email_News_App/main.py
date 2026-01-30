import requests
import send_email

topic="tesla"

apy_key = '1e6a9fc56a64418681dc17a9c7939781'

url = 'https://newsapi.org/v2/everything?"\
    "q={topic}&"\
        "from=2025-12-28" \
    "&sortBy=publishedAt&apiKey=1e6a9fc56a64418681dc17a9c7939781&language=en'

#Make request
request= requests.get(url)

# get a dictionary with data
content= request.json()

body=""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + body + article["title"]+"\n" \
            + article["description"] \
                + "\n" + article["url"] + "2*"\n"
    
body= body.encode("utf-8")
send_email.send_email(message=body)