from justwatch import JustWatch


class Nation:
    def __init__(self, aCountry='DE', someProviders=["Netflix"]):
        self.country = aCountry
        self.api = JustWatch(aCountry)
        result = self.api.get_providers()
        self.providers = [x for x in result if x['clear_name'] in someProviders]
        
    def get_minimum_price(self, anOriginalItem):
        ret = []
        results = self.api.search_for_item(query=anOriginalItem['original_title'])
        
        if len(results['items']) > 0:
            item = results['items'][0]
            if item['id'] == anOriginalItem['id'] and 'offers' in item:
                offers = item['offers']
                
                flatrates = self._search_for_flatrate(offers)
                ret.extend(flatrates)
                
                if len(ret) == 0:
                    minimum = self._search_for_lowest_price(offers)
                    ret.extend(minimum)
                        
        return ret
        
    def _search_for_flatrate(self, someOffers):    
        ids = [i['id'] for i in self.providers]
        flatrates = [
                                    x for x in someOffers
                                    if x['monetization_type'] == 'flatrate' and
                                    x['presentation_type'] != 'sd' and
                                    x['provider_id'] in ids]
        flatrates = [self._add_zero_price(x) for x in flatrates]
        return flatrates


    def _add_zero_price(self, aVal):
        aVal['retail_price'] = 0.00
        return aVal


    def _search_for_lowest_price(self, someOffers):
        rents = [
                            x for x in someOffers
                            if x['monetization_type'] == 'rent' and
                            x['presentation_type'] != 'sd']
        rents.sort(key = self._sort_price)
        if len(rents) > 0:
                lowest = rents[0]['retail_price']
                rents = [x for x in rents if x['retail_price'] == lowest]
                
        return rents
    

    def _sort_price(self, aVal):
        return aVal['retail_price']

    
    def get_item(self, aTitle):
        results = self.api.search_for_item(query=aTitle)
        if len(results['items']) > 0:
            item = results['items'][0]
            return item

        return ""

def __debug_method():
    test = Nation("DE", ["Netflix", "Amazon Prime Video"])
    result = test.get_minimum_price("matrix")
    print(result)
    
#debugMethod()
