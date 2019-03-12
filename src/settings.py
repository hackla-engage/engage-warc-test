import os




def project_path():
	return os.path.abspath('.')

def init(): 
	os.chdir(os.path.realpath(__file__ + "/../../"))

if __name__ == "__main__":
	init()
	print(project_path())