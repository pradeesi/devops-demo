from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_arab_bank_blue():
    return "<h1 style='color: Yellow;'>Hello Arab Bank.    Ver:6</h1>" # Renamed function for clarity, but not strictly necessary for the fix

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) # Get PORT from environment, default to 5000 for local dev
    app.run(debug=True, host='0.0.0.0', port=port)