from filehandler import *
from extractor import *

project_name = 'Codeforces Problemset'
covered = project_name + '/Covered Contests.txt'

print('\nEnter Contest ID range:\n(Two numbers - lowest and highest; range is inclusive)')

def work(): 

	n, m = map(int, input().split())

	#Select range
	START = min(n, m)
	END = max(n, m)

	#Creating project folder and covered file
	print()
	create_dir(project_name, '')
	create_metafile(project_name)

	#Finding out Contest numbers left to cover
	done = file_to_list(covered)
	left = [i for i in range(START, END +1) if i not in done]

	if len(left) is 0:
		print('\nAll contests already downloaded')
		return

	print(str(len(left)) + ' contests left to download')

	for i in left:
		print()
		try:
			if extract(i, 'Codeforces Problemset'):
				append_to_file(covered, str(i))
		except:
			print('Failed to download Contest ' + str(i))

	print('\nFinished')

work()
