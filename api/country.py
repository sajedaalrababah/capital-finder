from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        
        path = self.path
        url_components = parse.urlsplit(path)
        dic = dict(parse.parse_qsl(url_components.query))
        countryName = dic.get("name")


        if countryName:
            try:
                url = f"https://restcountries.com/v3.1/name/{countryName}?fullText=true"
                res = requests.get(url)
                data = res.json()
                capitalName = data[0]["capital"][0]
                result = f'The capital city of {countryName} is {capitalName}.'  

            except: 
                result = "Invalid country name! OR there is a connection issue."


        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))
        return