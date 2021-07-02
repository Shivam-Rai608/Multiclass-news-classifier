from flask import Flask, render_template, request
#import tensorflow
from keras.preprocessing.sequence import pad_sequences
import h5py
import numpy as np
import pickle
import preprocess



app = Flask(__name__) # initializing a flask app
@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("base11.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            with open('tokenizer.pickle', 'rb') as handle:
                tokenizer = pickle.load(handle)
            X=str(request.form['crim'])
            X=preprocess.all_func(X)
            maxlen=102
            X= pad_sequences(tokenizer.texts_to_sequences([X]), maxlen=maxlen)

            filename = "my_model111.h5"
            loaded_model = h5py.File(filename, 'r') # loading the model file from the storage
            # predictions using the loaded model file
            loaded_model = keras.models.load_model('my_model111.h5')
            prediction = loaded_model.predict(X)
            print(prediction)
            prediction=np.argmax(prediction) + 1
            print(prediction)
            y='s'
            if (prediction==1):
                y='World News'
            elif(prediction==2):
                y='Sports News'
            elif(prediction==3):
                y='Business News'
            elif(prediction==4):
                y='Science-Technology News'
            # showing the prediction results in a UI
            print(y)
            return render_template('prediction11.html', value=y)

        except:
            return ('Something Went Wrong')
    else:
        return render_template('base11.html')


if __name__ == "__main__":
    app.run()