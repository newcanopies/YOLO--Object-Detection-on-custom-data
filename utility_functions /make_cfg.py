#### Developed by Ojas Joshi #####
import os

def set_configs(filepath):

	tf = open(os.path.abspath('..')+'/darknet/cfg'+'/obj.data', 'w')
	tf.write('classes = 1\n')
	tf.write('train = '+filepath+'train.txt\n')
	tf.write('valid = '+filepath+'test.txt\n')
	tf.write('names = data/obj.names\n')
	tf.write('backup = backup/\n') 

	tf2 = open(os.path.abspath('..')+'/darknet/data'+'/obj.names', 'w')
	tf2.write('ojas phone') 
