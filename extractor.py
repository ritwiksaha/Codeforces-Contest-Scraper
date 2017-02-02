from bs4 import BeautifulSoup
import requests
from filehandler import *

#http://codeforces.com/contest/761?locale=en
#http://codeforces.com/contest/761/problem/F?locale=en

home = 'http://codeforces.com'
prefix = 'http://codeforces.com/contest/'
suffix = '?locale=en'

def extract(ID, base_dir_name):
	
	contest_base_url = prefix + str(ID) + suffix
	base_page = requests.get(contest_base_url)

	#Checking whether contest exists
	if base_page.status_code != 200 or base_page.url != contest_base_url:
		print('Contest %d does not exist' % (ID))
		return 0

	data = base_page.text
	soup = BeautifulSoup(data, "lxml")

	#Create Folder
	folder_name = str(ID) + ': ' + soup.title.string[12: -13]
	folder_name = folder_name.replace('/', '-')
	create_dir(folder_name, base_dir_name)

	problem_prefix = '/contest/' + str(ID) + '/problem/'

	problems = []
	tutorials = []
	for link in soup.find_all('a'):
		current = link.get('href')

		#Problems
		if current.startswith(problem_prefix) and len(current) == len(problem_prefix) + 1:
			if current not in problems:
				problems.append(current)
				print('Downloading Problem ' + current[-1])
				print_url(home + current + suffix, current[-1], base_dir_name + '/' + folder_name + '/')

		#Tutorials
		if link.text.lower().startswith('tutorial'):
			if current not in tutorials:
				tutorials.append(current)
				print('Downloading ' + link.text)
				print_url(home + current + suffix, link.text, base_dir_name + '/' + folder_name + '/')
	
	return 1
