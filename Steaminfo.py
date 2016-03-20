"""
VALUE DEVELOPER COMMUNITY 
https://developer.valvesoftware.com/wiki/Steam_Web_API#GetNewsForApp_.28v0001.29

"""
import json
import urllib.request

DOMAIN_ = "http://api.steampowered.com"

class SteamAPI:
	def __init__(self):
		self.key = self.getApiKey()

	def getApiKey(self):
		try:
			with open('steam_key', 'r') as file:
				return file.read()
		except FileNotFoundError:
			print('key file not found')

	#return apps dictionary{appid, app name}
	def getAppsDict(self):
		appdict = {}
		url = '{domain}/ISteamApps/GetAppList/v2'.format(domain=DOMAIN_)
		response = urllib.request.urlopen(url).read().decode('gbk', 'ignore')
		data = json.loads(response)
		for app in data['applist']['apps']:
			appids = app['appid']
			names = app['name']
			appdict[appids] = names
		return appdict

	#http://api.steampowered.com/ISteamEconomy/GetAssetPrices/v0001/?appid=440&key=075F586AC2F92DBA876BF91656E0FFFF
	def getAppsPriceDict(self, appid):
		url = '{domain}/ISteamEconomy/GetAssetPrices/v0001/?appid={id}&key={key}'.format(domain=DOMAIN_, id = appid, key = self.key)
		try:
			response = urllib.request.urlopen(url).read().decode('gbk', 'ignore')
			data = json.loads(response)
			print(data)
		except urllib.error.HTTPError as e:
			content = e.read()

	def getAPIDictWithKey(self):
		pass

	def getAPIDictwithoutKey(self):
		pass




def main():
    steamapi = SteamAPI()
    dic = steamapi.getAppsDict()
    steamapi.getAppsPriceDict(730)


if __name__ == "__main__":
	main()


