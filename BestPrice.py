from nation import Nation
	
	
def getMovieName(url):
	parts = url.split('/')
	return parts[len(parts) - 1]


url = "https://www.justwatch.com/de/Film/Aquaman"

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
movieName = "matrix"

for nat in nations:
	nat.getMinimumPrice(movieName)
