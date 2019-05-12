from jwbestprice import JwBestPrice
from nation import Nation
import sys
import clipboard
	
													
def getMovieName(url):
	parts = url.split('/')
	return parts[len(parts) - 1]


def printOffer(anOffer):
	urls = anOffer['urls']
	deeplink = "deeplink_{}".format(sys.platform)
	urlType = deeplink
	if urlType not in urls:
		urlType = "standard_web"
	
	text = "\t {}".format(urls[urlType])
	print(text)

		
def printNationOffer(someNationOffers):
	if len(someNationOffers) > 0:
		offer = someNationOffers[0]
		text = "{price} {currency} ({country})".format(
																price=offer['compare_price'],
																currency=offer['compare_currency'],
																country=offer['country'])
		print(text)
		[printOffer(x) for x in someNationOffers]
		

def main():
	url = ""
	url = sys.argv[1] if len(sys.argv) == 2 else clipboard.get()
	if not url:
		print('No input URL found.')
		return

	print("initialize JustWatch nations for search...")
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
	best = JwBestPrice(nations)
	
	print("searching best prices for \"{movie}\"...".format(movie=movieName))
	nationOffers = best.searchBestPrice(movieName)
	
	print("comparing prices...")
	compareOffers = best.comparePrices(nationOffers, "EUR")
	
	[printNationOffer(offer) for offer in compareOffers]
	

if __name__ == '__main__':
	main()
