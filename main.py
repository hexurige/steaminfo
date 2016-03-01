"""
this is the start-up class
"""

from Steaminfo import *

#main function
def main():
    steamapi = SteamAPI()
    dic = steamapi.getAppsDict()


if __name__ == "__main__":
	main()