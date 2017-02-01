import os
import pdfkit

# Makes a codeforces problemset directory
def create_dir(directory, path):
    if path is not '':
        path += '/'
    if not os.path.exists(path + directory):
        print('Creating directory ' + directory)
        os.makedirs(path + directory)
    else:
        print('Directory ' + directory + ' already exists')

# Creates a covered file
def create_metafile(project_name):
    covered = os.path.join(project_name , 'Covered Contests.txt')
    if not os.path.isfile(covered):
        write_file(covered)
    
# Create a new file
def write_file(path):
    open(path, 'w')

# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()

# Read a file and convert each line to integer lists
def file_to_list(file_name):
    results = []
    with open(file_name, 'rt') as f:
        for line in f:
            if line is not '\n':
                results.append(int(line))
    return sorted(results)

# Iterate through a list, each item will be a line in a file
def list_to_file(contests, file_name):
    with open(file_name,"w") as f:
        for l in sorted(contests):
            f.write(str(l)+"\n")

def print_url(url, pdf_name, path):
    pdfkit.from_url(url, path + pdf_name + '.pdf')
