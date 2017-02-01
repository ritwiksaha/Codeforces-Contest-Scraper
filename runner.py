from filehandler import *
from extractor import *

project_name = 'Codeforces Problemset'
covered = project_name + '/Covered Contests.txt'

print('Enter Contest ID range:\n(Two numbers - lowest and highest; range is inclusive)')

def work(): 

	n, m = map(int, input().split())

	#Select range
	START = min(n, m)
	END = max(n, m)

	#Creating project folder and covered file
	create_dir(project_name, '')
	create_metafile(project_name)

	#Finding out Contest numbers left to cover
	done = file_to_list(covered)
	left = [i for i in range(START, END +1) if i not in done]

	for i in left:
		extract(i, 'Codeforces Problemset')
		done.append(i)

	delete_file_contents(covered)
	list_to_file(sorted(done), covered)

work()
