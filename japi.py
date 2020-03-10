import urllib.request
import json

def main():
    
    ticker = input("Enter the Symbol of a stock to get its' price or quit to exit \n Symbol: ")

    #loops stock price
    while ticker != "quit":        
        #get price and prints json data format
        jsonData = getStockData(ticker)
        print(jsonData)

        #prints formatted
        jsonData = json.loads(jsonData)
        output = "The current price of " + jsonData["Global Quote"]["01. symbol"] + " is: " + jsonData["Global Quote"]["05. price"]
        print(output)
        ticker = input("Enter the Symbol of a stock to get its' price or quit to exit \n Symbol:")
    print("Stock quotes retrieved successfully!")


def getStockData(ticker):
    api = '&apikey=Y1KBYU6TVYJB3WII'
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='
    connection = urllib.request.urlopen(str(url + ticker + api))
    return connection.read().decode()
    


#auto runs main
if __name__ =="__main__":
  main()
