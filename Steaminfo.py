"""
VALUE DEVELOPER COMMUNITY 
https://developer.valvesoftware.com/wiki/Steam_Web_API#GetNewsForApp_.28v0001.29

"""
import json
import urllib.request

class SteamAPI:
	def __init__(self):
		self.key = self.getApiKey()

	def getApiKey(self):
		try:
			with open('steam_key', 'r') as file:
				return file.read()
		except FileNotFoundError:
			print('key file not found')

	def getAppsDict(self):
		appdict = {}
		url = 'http://api.steampowered.com/ISteamApps/GetAppList/v2'
		response = urllib.request.urlopen(url).read().decode('gbk', 'ignore')
		data = json.loads(response)
		for app in data['applist']['apps']:
			appids = app['appid']
			names = app['name']
			appdict[appids] = names
		return appdict

	def getAPIDictWithKey(self):
		pass

	def getAPIDictwithoutKey(self):
		pass


def main():
    steamapi = SteamAPI()
    dic = steamapi.getAppsDict()


if __name__ == "__main__":
	main()


