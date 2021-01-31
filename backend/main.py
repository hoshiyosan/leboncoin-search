from apartment.leboncoin import Leboncoin, SELL, LOCATION

lbc = Leboncoin()
anounces = lbc.search(anounce_type=SELL, min_price=400, max_price=620)
print(anounces)