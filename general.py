import os
from re import X

# Buat project (folder) tergantung nama website yang diinputkan pertama kali
# Each website you crawl is a separated project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print ('Creating directory ' + directory)
        os.makedirs(directory)

#Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    found = project_name + '/found.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(found):
        write_file(found, '')

#Create new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
    
#Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')

#Delete the contentns of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass #used for do nothing

# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

# Iterate throguh a set, each item will be a new line in the file
def set_to_file(links, file_name):
    with open (file_name, "w", errors="ignore") as f:
        for link in sorted(links):
            f.write(link+"\n")

#Measuring processing time
def count_time(seconds):
	seconds = seconds % (24 * 3600)
	hour = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60
	
	if hour == 0 and minutes == 0:
	    return "%d Second" % (seconds)    
	elif hour == 0:
	    return "%d Minute %d Second" % (minutes, seconds)
	else:
	    return "%d Hour %d Minute %d Second" % (hour, minutes, seconds)

#Read the pattern.txt
def read_pattern():
    with open('pattern.txt','r', encoding='utf8') as file:
        pat = file.readlines()
        pat = [i.replace("\n","") for i in pat]
        pat = list(filter(None, pat))
        return pat