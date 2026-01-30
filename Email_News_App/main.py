import requests


apy_key = '1e6a9fc56a64418681dc17a9c7939781'

url = 'https://newsapi.org/v2/everything?q=tesla&from=2025-12-28" \
    "&sortBy=publishedAt&apiKey=1e6a9fc56a64418681dc17a9c7939781'

#Make request
request= requests.get(url)

# get a dictionary with data
content= request.json()

print(content["articles"])