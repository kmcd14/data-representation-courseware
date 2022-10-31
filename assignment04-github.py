# This program reads a file from a repository.
# Then replace all the instances of the text "Andrew" with your name (Katie).
# Then commit those changes and push the file back to the repository.

import requests 
from github import Github
from config import config as cfg

apikey = cfg['key']
g = Github(apikey)


# Get clone url
repo = g.get_repo('kmcd14/data-representation-courseware')
#print(repo.clone_url)

# Reading all repo names
#for repo in g.get_user().get_repos():
    #print(repo.name)


# Get downloadurl
fileInfo = repo.get_contents('test_text_assignment04-github.py')
urlOfFile = fileInfo.download_url
print(urlOfFile)

# Making a http request from the downloadurl 
response = requests.get(urlOfFile)
contentOfFile = response.text
print(contentOfFile)

# Adding new text
#with open(contentOfFile) as fp:
    #line = fp.readline()
    #for line in fp:
        #newContents = contentOfFile.replace('Andrew', 'Katie')
    #print(newContents)

# Updating the file on git
#gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
#print(gitHubResponse)