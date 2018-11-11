import os

class Config():
	#in shell type: export TELTOKEN=past_you_bot_token_here
	TOKEN = os.environ.get('TELTOKEN')
	URL = "https://api.telegram.org/bot" + TOKEN + "/"
	#for proxying requests to the api, you can configure TOR+privoxy:
	#on ubuntu 16.04:
	##apt-get install tor privoxy
	##nano /etc/privoxy/config
	#add to end of file these three lines:
	##forward-socks5 / localhost:9050 .
	##forward-socks4 / localhost:9050 .
	##forward-socks4a / localhost:9050 .
	#start services:
	##service tor start
	##service privoxy start
	#use proxy on localhost:8118
	PROXIES = {
        "http": "localhost:8118",
        "https": "localhost:8118",
    }

