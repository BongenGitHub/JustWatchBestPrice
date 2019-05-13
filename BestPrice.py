from jwbestprice import JwBestPrice
from nation import Nation
import sys


if sys.platform == "ios":
	import clipboard
	clip_get = clipboard.get
else:
	import pyperclip
	clip_get = pyperclip.paste
	
											
def getOriginalItem(url):
	parts = url.split('/')
	if len(parts) >= 6 and parts[2] == "www.justwatch.com":
		country = parts[3].upper()
		title = parts[5]
		nation = Nation(country)
		return nation.getItem(title)

	return ""


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


def searchAndPrintOffers(nations, originalItem, aCurrency):
    best = JwBestPrice(nations) 

    print("searching best prices for \"{movie}\"...".format(movie=originalItem['original_title']))
    nationOffers = best.searchBestPrice(originalItem)
    nationOffers = [offer for offer in nationOffers if len(offer) > 0]

    if not nationOffers:
        print("No offers found!")
    else:
        print("comparing prices...")
        compareOffers = best.comparePrices(nationOffers, aCurrency)
        [printNationOffer(offer) for offer in compareOffers]		


def main():
	url = ""
	url = sys.argv[1] if len(sys.argv) == 2 else clip_get()
	if not url:
		print('No input found.')
		return	
	originalItem = getOriginalItem(url)
	if not originalItem:
		print('Input is not a JustWatch URL: "{}"'.format(url))
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
	
						
	searchAndPrintOffers(nations, originalItem, "EUR")
	

if __name__ == '__main__':
	main()
