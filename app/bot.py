import requests
import datetime
from config import Config

class Tbot:
	def __init__(self):
		return print(Config.URL)

	def get_update_in_json(self, request):
		response = requests.get(request + "getUpdates", proxies=Config.PROXIES)
		return response.json()

	def last_update(self, data):
		results = data['result']
		total_updates = len(results) - 1
		return results[total_updates]


def main():
	mybot = Tbot()
	#print(mybot.get_update_in_json(Config.URL))
	print(mybot.last_update(mybot.get_update_in_json(Config.URL)))

if __name__ == '__main__':
	main()
	