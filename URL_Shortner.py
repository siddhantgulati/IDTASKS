from flask import Flask, request, redirect
import string
import random

app = Flask(__name__)

# Dictionary to store short URLs and their corresponding long URLs
url_store = {}

# Function to generate a random short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))  # You can adjust the length as needed
    return short_url

@app.route('/')
def index():
    return 'Welcome to the URL Shortener'

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    short_url = generate_short_url()
    
    # Store the mapping between short and long URLs
    url_store[short_url] = long_url
    
    return f'Short URL: {request.host_url}{short_url}'

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    if short_url in url_store:
        long_url = url_store[short_url]
        return redirect(long_url)
    else:
        return 'Short URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)
