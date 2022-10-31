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


# Get downloadurl
fileInfo = repo.get_contents('test_text_assignment04.txt')
urlOfFile = fileInfo.download_url
#print(urlOfFile)

# Making a http request from the downloadurl 
response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)


# Replacing instances of 'Andrew' with 'Katie'
newContents = contentOfFile.replace('Andrew', 'Katie')
#print(newContents)

        
# Updating the file on git
gitHubResponse=repo.update_file(fileInfo.path,'updatedtest_text_assignment04.txt',newContents,fileInfo.sha)
#print(gitHubResponse)