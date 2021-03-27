import requests
from bs4 import BeautifulSoup
import notify2

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
Link = input("what is the link of the product(amazon only): ")
Cost = float(input("what is the minimumcost: "))



def getinfo(url,min_cost):
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.content, "html.parser")
	try:
		price = float(soup.find(
			"span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '',).replace('₹', ""))
		print(f"current price of the product is: ₹ {price} ")
		if price >= min_cost:
			print("high")
		if price <= min_cost:
			notify2.init('app name')
			n = notify2.Notification("Shopping",
			                         f"the price of your object is: ₹ {price}",
			                         "notification-message-im"   # Icon name
			                        )
			n.show()
	except:
		pass
	try:
		dealprice = float(soup.find(
			"span", attrs={'id': 'priceblock_dealprice'}).string.strip().replace(',', '',).replace('₹', ""))
		print(f"the deal price is: {dealprice}")
		if dealprice >= min_cost:
			print("high")
		elif dealprice <= min_cost:
			notify2.init('app name')
			n = notify2.Notification("Shopping",
			                         f"the price of your object is: ₹ {dealprice}",
			                         "notification-message-im"   # Icon name
			                        )
			n.show()
	except:
		pass

while True:
	getinfo(Link,Cost)	

