########################################################
######image to be encoded in base64 first###############
########################################################

from flask import Flask, render_template, request,jsonify
import cv2
import numpy as np
import base64
import math
from scipy import ndimage
import json

app = Flask(__name__)

@app.route('/image', methods=['GET', 'POST'])
def add_face():
    if request.method == 'POST':
        #  read encoded image
        imageString = base64.b64decode(request.form['img'])

        #  convert binary data to numpy array
        nparr = np.fromstring(imageString, np.uint8)

        #  let opencv decode image to correct format
        image= cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR);

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.bitwise_not(gray)

        thresh = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        coords = np.column_stack(np.where(thresh > 0))

        angle = cv2.minAreaRect(coords)[-1]

        if angle < -45:
            angle = -(90+angle)
        else:
            angle = -angle
        print(angle)

        message={
                    #status':200
                    'Angle':angle
        }

        return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)