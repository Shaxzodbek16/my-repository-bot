import base64
from PIL import Image
from io import BytesIO


def save_image_from_base64(photo_code, output_file_path):
	try:
		if "," in photo_code:
			photo_code = photo_code.split(",")[1]
		image_data = base64.b64decode(photo_code)
		img = Image.open(BytesIO(image_data))
		img.save(output_file_path)
		return f"Image saved successfully as {output_file_path}"
	except Exception as e:
		return f"Error decoding or saving image: {e}"
