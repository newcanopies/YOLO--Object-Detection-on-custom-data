#### Developed by Ojas Joshi #####
import subprocess
from bounding_box import *
from preprocess import *
from make_cfg import set_configs
import os
import argparse,sys
import shlex

def run_command(command):
	process = subprocess.Popen(shlex.split(command), shell=False, stdout=subprocess.PIPE)
	for line in process.stdout:
			print(line)
	process.wait()

# def main(args):
def main():

	# parser = argparse.ArgumentParser(description='train_phone_finder')
	# parser.add_argument('--filepath',dest='file',type=str,default='/Users/ojasjoshi/Desktop/phone_finder/find_phone')
	# parser.add_argument('--train',dest='train',type=str,default=True)
	# args = parser.parse_args()

	input_file = sys.argv[1]
	train = "do_not_train"
	if(len(sys.argv) == 3):
		train = str(sys.argv[2])

	path_to_train = input_file

	make_labels(path_to_train)
	process_labels(path_to_train)
	set_configs(path_to_train)

	if(train=="train"):
		print("in")
		os.chdir('..')
		os.chdir('darknet')
		command = './darknet detector train cfg/obj.data cfg/yolo-obj.cfg darknet19_448.conv.23'
		run_command(command)
	else:
		print("\nNetwork Configured.... :)\n\nTo start training do:\ncd ../darknet\n./darknet detector train cfg/obj.data cfg/yolo-obj.cfg darknet19_448.conv.23\n")


if __name__ == '__main__':
    # main(sys.argv)
    main()