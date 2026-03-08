from src.background_dealing import make_bakcground_white
from paths import FILES_DIR
import os


if __name__ == "__main__":


	file_path = os.path.join(FILES_DIR, "HW5.pdf") 
	output_file_path = os.path.join(FILES_DIR, "HW5_bg_white.pdf")
	
	make_bakcground_white(file_path, output_file_path, 160)
	

