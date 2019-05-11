from nation import Nation
import requests
	
	
def getMovieName(url):
	parts = url.split('/')
	return parts[len(parts) - 1]
	
def getCurrencyRate(fromCurrency, toCurrency):
	rate = 1.0
	if fromCurrency != toCurrency:		
		api_url = 'https://api.exchangeratesapi.io/latest?base={}&symbols={}'.format(fromCurrency, toCurrency)
		r = requests.get(api_url)
		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200
		json = r.json()
		rate = json['rates'][toCurrency] 
	return rate
	
def addCompareCurrencyFields(anOffer, anAmount, aCurrency):
	anOffer['compare_price'] = anAmount
	anOffer['compare_currency'] = aCurrency
	return anOffer

def addCurrency(someOffers, toCurrency):
	if len(someOffers) > 0:
		offer = someOffers[0]
		fromCurrency = offer['currency']
		amount = offer['retail_price']
		rate = getCurrencyRate(fromCurrency, toCurrency)
		newAmount = round(amount * rate, 2)
		return [addCompareCurrencyFields(x, newAmount, toCurrency) for x in someOffers]	
	else:
		return
	
def searchBestPrice(url):
	# No English Sound: MX, BR, RU
	nations = [
							Nation("US"), Nation("CA"),
							Nation("DE", ["Netflix", "Amazon Prime Video"]),
							Nation("AT"), Nation("CH"), Nation("GB"), Nation("IE"),
							Nation("IT"), Nation("FR"), Nation("ES"), Nation("NL"),
							Nation("NO"), Nation("SE"), Nation("DK"), Nation("FI"),
							Nation("LT"), Nation("LV"), Nation("EE"), Nation("PT"),
							Nation("PL"), Nation("ZA"), Nation("AU"), Nation("NZ"),
							Nation("IN"), Nation("JP"), Nation("KR"), Nation("TH"),
							Nation("MY"), Nation("PH"), Nation("SG"), Nation("ID")]
									
	movieName = getMovieName(url)
	results = [nat.getMinimumPrice(movieName) for nat in nations]
	return results
	
def sortOffer(val): 
    return val[0]['compare_price']  
	
url = "https://www.justwatch.com/de/Film/Aquaman"
nationOffers = searchBestPrice(url)
compareOffers = [addCurrency(x, "EUR") for x in nationOffers if len(x) > 0] #make offers comparable and remove empty ones
compareOffers.sort(key = sortOffer)
print(prices)
