from justwatch import JustWatch

# No English Sound: MX, BR, RU
# No Func: NL, NO, SE, DK, LT, LV, EE, IN, TH, MY, PH, ID
nations = ["US", "CA", "DE", "AT", "CH"
					,"GB", "IE", "IT", "FR", "ES"
					,"FI", "PT", "PL", "ZA", "AU"
					,"NZ", "JP", "KR", "SG"]

jw = JustWatch(country='ID')

results = jw.search_for_item(query='aquaman')

print("hello")
