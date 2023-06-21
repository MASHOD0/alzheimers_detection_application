from flask import Flask, request, render_template
import os
from model import predict_image

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'UPLOADS')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file_input = request.files['file']
    if file_input.filename == '':
        return 'No file selected', 400

    
    file_input.save(os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg'))
    prediction = predict_image('UPLOADS/image.jpg')
    return f'File uploaded successfully \n Prediction: {prediction}', 200

if __name__ == '__main__':
    app.run(debug=True)