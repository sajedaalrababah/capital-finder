from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        
        path = self.path
        url_components = parse.urlsplit(path)
        dic = dict(parse.parse_qsl(url_components.query))
        capitalName = dic.get("capital")


        if capitalName:
            try:
                url = f"https://restcountries.com/v3.1/capital/{capitalName}"
                res = requests.get(url)
                data = res.json()
                countryName = data[0]["name"]['common']
                result = f'{capitalName} is the capital city of {countryName}.'  

            except:
                result = "Invalid capital name! OR there is a connection issue."    


        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))
        return