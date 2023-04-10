import json
import requests
import urllib3
from flask import Flask, Response

# Ignore ssl errors because of self-signed certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

@app.route('/metrics')
def index():
    with open('config.json') as f:
        sites = json.load(f)['sites']
    results = []

    # Loop through each site and check the latency
    for site in sites:
        try:
            # Send a GET request to the site and measure the response time
            response = requests.get(site, timeout=5, verify=False)
            latency = response.elapsed.total_seconds() * 1000
            results.append((site, latency))
        except requests.exceptions.RequestException as e:
            results.append((site, str(e)))

    # Format the results in a format that Prometheus can parse
    output = ''
    for site, latency in results:
        if isinstance(latency, str):
            output += f'site_latency{{site="{site}"}} NaN\n'
        else:
            output += f'site_latency{{site="{site}"}} {latency:.2f}\n'

    # Return the results as a response to the HTTP request
    return Response(output, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=False)