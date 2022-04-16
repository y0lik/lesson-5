# 5399646312:AAEE8KKx8k7i-BAS6m107jHbaCvXZZ4jiGI

import requests

url = "https://api.telegram.org/bot5399646312:AAEE8KKx8k7i-BAS6m107jHbaCvXZZ4jiGI/"


def last_update(request):
	response = requests.get(request + 'getUpdates')
	response = response.json()
	results = response['result']
	total_update = len(results) - 1
	return results[total_update]


def get_chat_id(update):
	return update['message']['chat']['id']


def get_message_test(update):
	return update['message']['text']


def send_message(chat, text):
	params = {'chat_id': chat, 'text': text}
	return requests.post(url + 'sendMessage', data=params)


def main():
	update_id = last_update(url)['update_id']
	while True:
		update = last_update(url)
		if update_id == update['update_id']:
			message = get_message_test(update).lower()
			if message == "hi":
				send_message(get_chat_id(update), 'HELLO!')
			else:
				send_message(get_chat_id(update), 'I dont now!')

			update_id += 1


main()
