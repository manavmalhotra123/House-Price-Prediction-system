#Import Libraries
from flask import Flask, request, render_template,send_from_directory
import model

 
app = Flask(__name__,template_folder="templates",static_folder="static")
 
@app.route('/',methods = ['GET'])
@app.route('/index')
def home_page():
    return render_template('index.html')


 
# render htmp page 
@app.route('/a')
def about_page():
    return render_template('about.html')

@app.route('/c')
def contact_page():
    return render_template('contact.html')


@app.route('/g')
def gallery_page():
    return render_template('gallery.html')

@app.route('/predict',methods=['POST'])
def predict():
     
    #take data from form and store in each feature    
    input_features = [x for x in request.form.values()]
    bath = input_features[0]
    balcony = input_features[1]
    total_sqft_int = input_features[2]
    bhk = input_features[3]
    price_per_sqft = input_features[4]
    area_type = input_features[5]
    availability = input_features[6]
    location = input_features[7]
     
    # predict the price of house by calling model.py
    predicted_price = model.predict_house_price(bath,balcony,total_sqft_int,bhk,price_per_sqft,area_type,availability,location)       
 
 
    # render the html page and show the output
    return render_template('index.html', prediction_text='Predicted Price of Bangalore House is {}'.format(predicted_price))





 

 
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="8080")



@app.route("/base/<path:filename>")
def base_static(filename):
    return send_from_directory(app.root_path + "../templates/static",filename)
     
if __name__ == "__main__":
    app.run(debug=True)
    
    