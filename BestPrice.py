from justwatch import JustWatch

def getMovieName(url):
	parts = url.split('/')
	return parts[len(parts) -1]


url = "https://www.justwatch.com/de/Film/Aquaman"

# No English Sound: MX, BR, RU
nations = ["US", "CA", "DE", "AT", "CH"
					,"GB", "IE", "IT", "FR", "ES"
					,"NL", "NO", "SE", "DK", "FI"
					,"LT", "LV", "EE", "PT", "PL"
					,"ZA", "AU","NZ", "IN", "JP"
					,"KR", "TH", "MY", "PH" "SG", "ID"]
					
					
					
movieName = getMovieName(url)

for i in nations:
	jw = JustWatch(country=i)
	results = jw.search_for_item(query=movieName)
