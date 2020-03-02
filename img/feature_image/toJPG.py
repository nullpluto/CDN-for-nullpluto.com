import os
import cv2

EXPANDED_NAME = [".png"]


def get_images(file_dir):
	image_files = []

	for file in os.listdir(file_dir):
		if os.path.splitext(file)[1] in EXPANDED_NAME:
			image_files.append(file)

	return image_files


def convert_to_jpg(file_dir, image_file, keep_source):
	raw_image_path = os.path.join(file_dir, image_file)
	new_image_file = os.path.splitext(image_file)[0] + ".jpg"
	new_image_path = os.path.join(file_dir, new_image_file)

	image = cv2.imread(raw_image_path)
	cv2.imwrite(new_image_path, image)

	if keep_source == False:
		os.remove(raw_image_path)


if __name__ == "__main__":
	file_dir = os.getcwd()
	image_list = get_images(file_dir)

	for image in image_list:
		convert_to_jpg(file_dir, image, False)
