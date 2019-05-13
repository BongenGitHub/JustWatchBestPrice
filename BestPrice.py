from jwbestprice import JwBestPrice
from nation import Nation
import sys


if sys.platform == "ios":
	import clipboard
	clip_get = clipboard.get
else:
	import pyperclip
	clip_get = pyperclip.paste


def print_offer(anOffer):
	urls = anOffer['urls']
	deeplink = "deeplink_{}".format(sys.platform)
	urlType = deeplink
	if urlType not in urls:
		urlType = "standard_web"
	
	text = "\t {}".format(urls[urlType])
	print(text)

		
def print_nation_offer(someNationOffers):
	if len(someNationOffers) > 0:
		offer = someNationOffers[0]
		text = "{price} {currency} ({country})".format(
																price=offer['compare_price'],
																currency=offer['compare_currency'],
																country=offer['country'])
		print(text)
		[print_offer(x) for x in someNationOffers]


def search_and_print_offers(someNations, anOriginalItem, aCurrency):
    best = JwBestPrice(someNations) 

    print("searching best prices for \"{movie}\"...".format(movie=anOriginalItem['original_title']))
    nationOffers = best.search_best_price(anOriginalItem)
    nationOffers = [offer for offer in nationOffers if len(offer) > 0]

    if not nationOffers:
        print("No offers found!")
    else:
        print("comparing prices...")
        compareOffers = best.compare_prices(nationOffers, aCurrency)
        [print_nation_offer(offer) for offer in compareOffers]		


def main():
	url = ""
	url = sys.argv[1] if len(sys.argv) == 2 else clip_get()
	if not url:
		print('No input found.')
		return	
	originalItem = JwBestPrice.get_original_item(url)
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
	
						
	search_and_print_offers(nations, originalItem, "EUR")
	

if __name__ == '__main__':
	main()
