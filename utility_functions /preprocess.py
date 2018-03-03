#### Developed by Ojas Joshi #####
import glob, os

def process_labels(filepath):

	path_data = filepath

	# Percentage of images to be used for validation/test
	percentage_test = 10

	file_train = open(filepath+'train.txt', 'w')  
	file_test = open(filepath+'test.txt', 'w')

	counter = 1  
	index_test = round(100 / percentage_test)  

	for pathAndFilename in glob.iglob(os.path.join(filepath, "*.jpg")):  
	    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
	    if counter == index_test:
	        counter = 1
	        file_test.write(path_data + title + '.jpg' + "\n")
	    else:
	        file_train.write(path_data + title + '.jpg' + "\n")
	        counter = counter + 1
