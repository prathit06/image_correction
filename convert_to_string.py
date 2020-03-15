import requests
import base64

def convert_to_base(image):

	URL = "http://localhost:5000/image"
	with open(image, "rb") as imageFile:
	    img = base64.b64encode(imageFile.read())
	response = requests.post(URL, data={"img":str(img)})
	print(response.text)
convert_to_base("new.jpg")