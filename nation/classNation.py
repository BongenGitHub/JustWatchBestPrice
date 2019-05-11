from justwatch import JustWatch


def sortPrice(val): 
    return val['retail_price']  

class Nation:
	def __init__(self, aCountry='DE', someProviders=["Netflix"]):
		self.country = aCountry
		self.api = JustWatch(aCountry)
		result = self.api.get_providers()
		self.providers = [x for x in result if x['clear_name'] in someProviders]
		
	def getMinimumPrice(self, aMovieName):
		ret = []
		results = self.api.search_for_item(query=aMovieName)
		
		if len(results['items']) > 0:
			item = results['items'][0]
			offers = item['offers']
			
			flatrates = self.searchForFlatrate(offers)
			ret.extend(flatrates)
			
			if len(ret) == 0:
				minimum = self.searchForLowestPrice(offers)
				ret.extend(minimum)
				
		return ret
		
	def searchForFlatrate(self, someOffers):	
		ids = [i['id'] for i in self.providers]
		flatrates = [
									x for x in someOffers
									if x['monetization_type'] == 'flatrate' and
									x['presentation_type'] != 'sd' and
									x['provider_id'] in ids]
		return flatrates
		
	def searchForLowestPrice(self, someOffers):
		rents = [
							x for x in someOffers
							if x['monetization_type'] == 'rent' and
							x['presentation_type'] != 'sd']
		rents.sort(key = sortPrice)
		return rents[:1]

def debugMethod():
	test = Nation("DE", ["Netflix", "Amazon Prime Video"])
	result = test.getMinimumPrice("aquaman")
	print("t")
	
#debugMethod()
