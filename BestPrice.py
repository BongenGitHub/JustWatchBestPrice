from justwatch import JustWatch

# No English Sound: MX, BR, RU
# No Func: NL, NO, SE, DK
nations = ["US", "CA", "DE", "AT", "CH"
					,"GB", "IE", "IT", "FR", "ES"
					,"FI"]

jw = JustWatch(country='FI')

results = jw.search_for_item(query='aquaman')

print("hello")
