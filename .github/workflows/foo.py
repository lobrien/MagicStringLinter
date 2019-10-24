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
print(json.dumps(event['head_commit'], indent=2))
url = event['head_commit']['url']
print('HEAD is at %s' % url)
sha = event['head_commit']['id']
print(f"SHA is {sha}")
#TODO Dynamic path to current repo
url = f'https://api.github.com/repos/lobrien/MagicStringLinter/commits/{sha}'
print('Commit is at %s' % url)
tree_response = requests.get(url)
tree_json = json.loads(tree_response.content)
fs = tree_json["files"]
to_check = (f["filename"] for f in fs if f["status"] in ["added", "modified"])
print(json.dumps(fs, indent=2))
print("-----------------------")
print("File to check:")
for f in to_check : 
    print(f)