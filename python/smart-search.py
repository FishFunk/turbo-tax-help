"""
search.py
A simple web server to serve AnswerXChange search results.
Uses:
  Flask==1.1.1
  requests==2.22.0
Install dependencies:
  pip3 install Flask requests
Run with:
  python3 search.py
"""
__author__ = "Tyler Krupicka"

import json
import requests
from flask import Flask, redirect, request, jsonify, abort
app = Flask(__name__)


@app.route('/')
def index():
    return redirect("/search")


@app.route('/search', methods=['GET'])
def search():
    """
    A simple search endpoint, which takes a query and a page number.
    Example: http://localhost:5000/search?query=test&page=1
    """
    query = request.args.get('query')
    page = request.args.get('page')

    if page == None or query == None:
        abort(400, 'The "page" and "query" parameters are both required.')

    cookies = {
        'qbn.authid': 'demo',
        'qbn.agentid': 'demo',
        'qbn.parentid': 'demo',
    }

    headers = {
        'Authorization': 'Intuit_APIKey intuit_apikey=prdakyres2BEwmOvDMtoKGiMruAOBfRhCZq0GAap, intuit_apikey_version=1.0',
    }

    params = (
        ('q', query),
        ('page', page),
        ('tax_year[]', '2019'),
    )

    response = requests.get('https://cetsmartsearch.api.intuit.com/v1/search',
                            headers=headers, params=params, cookies=cookies)

    return jsonify(response.json())


if __name__ == "__main__":
    app.run()
