import urllib.request, json

# Introduction:
name = "Avivit Hubara"
print("Welcome -", name,  "- to currency converter.")

amount = 100
print("The amount in ILS is:", amount)

# Calculate the currency with API:
try:
    with urllib.request.urlopen("http://free.currencyconverterapi.com/api/v5/convert?q=USD_ILS&compact=n&apiKey=cd60448290a2e0b42c5d") as url:
        json_data = json.loads(url.read().decode())
        results = json_data['results']
        USD_ILS = results['USD_ILS']
        convert = USD_ILS['val']
except urllib.error.HTTPError as err:
    print(err)
    exit()

# Display the amount in USD to the user:
result = amount * convert
print("The amount in USD is:", result)
print("Thanks for using our currency converter.")
