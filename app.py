from flask import Flask, request, render_template, redirect
import requests
import fsq
app = Flask(__name__)

@app.route("/post", methods=['POST',])
def post():
    #post message to page
    venueId = request.form['venueId'] 
    text = request.form['text']
    payload = {'venueId': venueId, 'text': text }
    response = requests.post('https://api.foursquare.com/v2/tips/add?oauth_token=0Q235XWN4ACGAPLRUTRUGBQFV1HWN4RVXCMHVE0EAETX2DMC&v=20140607', data=payload) 
    print(response.text)
    if response.status_code != 200:
        return response.json()['meta']['errorDetail']
    url = response.json()['response']['tip']['canonicalUrl']
    return redirect(url+'/')

@app.route("/")
def index():
    stores = fsq.search(40.7, -74)
    return render_template('index.html', stores=stores)

if __name__ == "__main__":
    app.run(debug=True)
