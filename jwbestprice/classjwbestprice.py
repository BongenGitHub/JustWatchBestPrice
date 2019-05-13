from nation import Nation 
import requests


class JwBestPrice:
    def __init__(self, someNations):
        self.nations = someNations
    
    
    @staticmethod
    def get_original_item(anUrl):
        parts = anUrl.split('/')
        if len(parts) >= 6 and parts[2] == "www.justwatch.com":
            country = parts[3].upper()
            title = parts[5]
            nation = Nation(country)
            return nation.get_item(title)

        return ""


    def search_best_price(self, anOriginalItem):
        nationOffers = [nat.get_minimum_price(anOriginalItem) for nat in self.nations]
        return nationOffers
    
    
    def compare_prices(self, someNationOffers, aCurrency):
        # make offers comparable and remove empty ones
        compareOffers = [self._add_currency(x, aCurrency) for x in someNationOffers if len(x) > 0]
        compareOffers.sort(key=self._sort_offer, reverse=True)
        return compareOffers
    
            
    def _add_currency(self, someOffers, atoCurrency):
        if len(someOffers) > 0:
            offer = someOffers[0]
            
            if offer['retail_price'] == 0.0:
                newAmount = 0.0
            else:
                fromCurrency = offer['currency']
                amount = offer['retail_price']
                rate = self._get_currency_rate(fromCurrency, atoCurrency)
                newAmount = round(amount * rate, 2)
                
            return [self._add_compare_currency_fields(x, newAmount, atoCurrency) for x in someOffers]
        else:
            return
        
    
    def _get_currency_rate(self, aFromCurrency, aToCurrency):
        rate = 1.0
        if aFromCurrency != aToCurrency:
            api_url = 'https://api.exchangeratesapi.io/latest?base={}&symbols={}'.format(aFromCurrency, aToCurrency)
            r = requests.get(api_url)
            r.raise_for_status() # Raises requests.exceptions.HTTPError if r.status_code != 200
            json = r.json()
            rate = json['rates'][aToCurrency]
        return rate
    
    
    def _add_compare_currency_fields(self, anOffer, anAmount, aCurrency):
        anOffer['compare_price'] = anAmount
        anOffer['compare_currency'] = aCurrency
        return anOffer
                    
    
    def _sort_offer(self, aVal):
        return aVal[0]['compare_price']
        
        
        
#print("test")
