from justwatch import JustWatch

nations = ["US", "CA", "MX"]

jw = JustWatch(country='MX')

results = jw.search_for_item(query='aquaman')

print("hello")
