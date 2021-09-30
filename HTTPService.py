from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse
import requests, os, json, sys

# Class to define the HTTP endpoints
class helloworld(BaseHTTPRequestHandler):    
    # Method to check for camel-case in the url query string and to cut by spaces 
    def camel2token(self, str):
        return ''.join(' ' + c if c.isupper() else c for c in str)

    # Method to return JSON with git hash and name of the project
    def git_versionz(self):
        git_info = os.getenv('GITHUB_TOKEN', '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')
        owner = "RaghuKA"
        repo = "Challenge"
        query_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
        headers = {'Authorization': f'token {git_info}'}
        # Get request from url
        get_requesturl = requests.get(query_url, headers=headers)
        # Parse the content of get_requesturl into a list
        getrequest_jsondata=json.loads(get_requesturl.content)
        # Get hash key and project name as a dictionary
        versionz_dict={getrequest_jsondata[0]['sha']:repo}
        return versionz_dict

    # Methods to define the HTTP endpoints
    def do_GET(self):
        # HTTP endpoint /helloworld
        if self.path.endswith('helloworld'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write('"Hello Stranger"\n'.encode())
    
        # HTTP endpoint /helloworld?name=filteredvalue -> Example. /helloworld?name=AlfredENeumann (any filtered value)
        if self.path.__contains__('helloworld?name='):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            # split the string into 2 parts if possible where = is encountered
            split_str = self.path.split('=', 1)
            # choose the latter part of the string after the =
            name_str = split_str[1]

            # check for empty strings, if so, print Hello Anonymous
            if (len(name_str)==0):
                self.wfile.write('Hello Anonymous\n'.encode())
            # else, de-camel the provided argument
            else:
                cmd_str = self.camel2token(name_str)
                # using f-string
                # parse.unquote -> https://docs.python.org/3/library/urllib.parse.html#urllib.parse.unquote
                f_cmd_str = f'"Hello{parse.unquote(cmd_str)}"\n'
                self.wfile.write((f_cmd_str).encode())

        if self.path.endswith('versionz'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.json_string= json.dumps(self.git_versionz(),indent = 4)
            self.wfile.write(self.json_string.encode())            

def main():
    PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server = HTTPServer(('', PORT), helloworld)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()