from nation import Nation 
import requests
import appex


class JwBestPrice:
	def __init__(self, someNations):
		self.nations = someNations
		
		
	def searchBestPrice(self, movieName):
		nationOffers = [nat.getMinimumPrice(movieName) for nat in self.nations]
		return nationOffers
	
	
	def comparePrices(self, someNationOffers, aCurrency):
		# make offers comparable and remove empty ones
		compareOffers = [self.addCurrency(x, aCurrency) for x in someNationOffers if len(x) > 0]
		compareOffers.sort(key=self.sortOffer, reverse=True)
		return compareOffers
	
			
	def addCurrency(self, someOffers, toCurrency):
		if len(someOffers) > 0:
			offer = someOffers[0]
			
			if offer['retail_price'] == 0.0:
				newAmount = 0.0
			else:
				fromCurrency = offer['currency']
				amount = offer['retail_price']
				rate = self.getCurrencyRate(fromCurrency, toCurrency)
				newAmount = round(amount * rate, 2)
				
			return [self.addCompareCurrencyFields(x, newAmount, toCurrency) for x in someOffers]
		else:
			return
		
	
	def getCurrencyRate(self, fromCurrency, toCurrency):
		rate = 1.0
		if fromCurrency != toCurrency:
			api_url = 'https://api.exchangeratesapi.io/latest?base={}&symbols={}'.format(fromCurrency, toCurrency)
			r = requests.get(api_url)
			r.raise_for_status() # Raises requests.exceptions.HTTPError if r.status_code != 200
			json = r.json()
			rate = json['rates'][toCurrency]
		return rate
	
	
	def addCompareCurrencyFields(self, anOffer, anAmount, aCurrency):
		anOffer['compare_price'] = anAmount
		anOffer['compare_currency'] = aCurrency
		return anOffer
					
	
	def sortOffer(self, val):
		return val[0]['compare_price']
		
		
		
#print("test")
