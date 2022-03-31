from black import diff
import requests
import creds
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
UP = "🔺"
DOWN = "🔻"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": creds.av_api_key
}
stock_response = requests.get(STOCK_ENDPOINT,params=stock_parameters)
stock_data = stock_response.json()
date_yesterday = list(stock_data["Time Series (Daily)"])[0]
date_before_yesterday = list(stock_data["Time Series (Daily)"])[1]

close_yesterday = float(stock_data["Time Series (Daily)"][date_yesterday]["4. close"])
close_before_yesterday = float(stock_data["Time Series (Daily)"][date_before_yesterday]["4. close"])

difference = abs(close_yesterday - close_before_yesterday)
difference_pct = int((difference/close_before_yesterday)*100)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
news_parameters = {
    "q": STOCK,
    "from": date_yesterday,
    "sortBy": "publishedAt",
    "apikey": creds.news_api_key
}
news_response = requests.get(NEWS_ENDPOINT,params=news_parameters)
news_data = news_response.json()
news_articles = news_data["articles"][:3]
news_articles = [(x['title'], x["description"]) for x in news_data["articles"][:3]]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
client = Client(creds.account_sid, creds.auth_token) 

if difference > (close_yesterday * .05):
    for article in news_articles:
        if close_yesterday > close_before_yesterday:
            icon = UP
        else:
            icon = DOWN
        message_body = f"{STOCK}: {icon} {difference_pct}%\nHeadline: {article[0]} \nBrief: {article[1]}"

        message = client.messages.create(
                            body=message_body,
                            from_='+13344715177',
                            to=creds.my_phone_number
                        )
else:
    print("less than 5%")