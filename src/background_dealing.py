import os
import fitz
import numpy as np
from PIL import Image
import io

AVG_THRESHOLD = 150



def make_image_background_white(pillow_image, avg_threshold):
	img_arr = np.array(pillow_image.convert("RGB"))
	r_arr, g_arr, b_arr = img_arr[:, :, 0].astype(int), img_arr[:, :, 1].astype(int), img_arr[:, :, 2].astype(int)
	brightness = ((r_arr + g_arr + b_arr)/3).astype(int)
	mask = brightness > avg_threshold
	unmasked = brightness <= avg_threshold
	img_arr[mask] = [255, 255, 255]
	img_arr[unmasked] = [0, 0, 0]
	res_img = Image.fromarray(img_arr)
	return res_img
	
	













def make_bakcground_white(file_path, output_file_path, avg_threshold):
	doc = fitz.open(file_path)
	bg_color =  (1, 1, 1)

	for page in doc:
		# page.draw_rect(page.rect, color = bg_color, fill = bg_color, overlay = False)
		img_lst = page.get_images(full=True)
		for img in img_lst:
			xref = img[0]
			base_image = doc.extract_image(xref)
			img_bytes = base_image["image"]
			pil_img = Image.open(io.BytesIO(img_bytes))
			res_img = make_image_background_white(pil_img, avg_threshold)
			res_img.save(output_file_path, "PDF", resolution = 300)


	# doc.ez_save(output_file_path)
	# doc.close()
	# print("file '%s': background color is changes to white"%file_path)








if __name__ == "__main__":
	

	print("tested")











