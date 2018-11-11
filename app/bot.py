import requests
import datetime
#import configuration from config.py
from config import Config

class Tbot:
	def __init__(self):
		return print(Config.URL)
    
    #get all available updates
	def get_update_in_json(self, request):
		response = requests.get(request + "getUpdates", proxies=Config.PROXIES)
		return response.json()

    #get only last update
	def last_update(self, data):
		results = data['result']
		total_updates = len(results) - 1
		return results[total_updates]
    
    #get current chat ID
	def get_chat_id(self, update):
		return update['message']['chat']['id']

	#send message in a chat with ID==chat
	def send_message(self, chat, text):
		params = {'chat_id': chat, 'text': text}
		response = requests.post(Config.URL + 'sendMessage', data=params, proxies=Config.PROXIES)
		return response


def main():
	mybot = Tbot()
	#print(mybot.get_update_in_json(Config.URL))
	#print(mybot.last_update(mybot.get_update_in_json(Config.URL)))
	chat_id = mybot.get_chat_id(mybot.last_update(mybot.get_update_in_json(Config.URL)))
	mybot.send_message(chat_id, 'Bot says: By!')
	print('MESSAGE is SENDED!')

if __name__ == '__main__':
	main()
