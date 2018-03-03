#### Developed by Ojas Joshi #####
import subprocess
import os
import argparse,sys

def run_command(command):
	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	for line in process.stdout:
				print(line)
	process.wait()

def main():

	input_img = sys.argv[1]
	wtfile = "yolo-obj_trained.weights"	#default weights assuming location is in same dir as ./darknet

	if(len(sys.argv) == 3):
		wtfile = str(sys.argv[2])

	os.chdir('..')
	os.chdir('darknet')
	open('results/test.txt', 'w').close()

	if(input_img[len(input_img)-4:len(input_img)] != ".jpg" and input_img[len(input_img)-4:len(input_img)] != ".png"):
		print("Please give a .jpg or .png format image\n", input_img[len(input_img)-5:len(input_img)])
	else:
		command = "./darknet detector test cfg/obj.data cfg/yolo-obj.cfg "+ wtfile + " " + str(input_img)
		run_command(command)

if __name__ == '__main__':
    main()
	
