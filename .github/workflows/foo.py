import requests
import os 
import json

def readJson(path) :
    with open(path) as json_file:
        data = json.load(json_file)
        return data

print(os.environ['PATH'])
for f in os.listdir("."):
    print(f)
path = os.environ['GITHUB_EVENT_PATH']
print('Event path is %s' % path)
event = readJson(path)
url = event['head_commit']['url']
print('HEAD is at %s' % url)
url = 'https://api.github.com/repos/lobrien/MagicStringLinter/commits/1445bb6f501df462f2480eba3bf924782198a05a'
print('HARDCODE is at %s' % url)
tree_response = requests.get(url)
tree_json = json.loads(tree_response.content)
print(json.dumps(tree_json, indent=2))

print("Hello, actions")