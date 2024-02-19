
virtualenv my_env

# change "my_env" to what name you want 

virtualenv brainenv

# make syre you change directory to the file that was just creatd "brainenv"

cd brainenv

# then type 

source bin/activate

# to activate the virutal environment 

# it should say (brianenv)in the terminal 

(brainenv) pc@pc-Lenovo-G500s:~/Desktop/parserproject5/brainenv$ 


also conda info --envs will list all the conda virtual environmemths going on

conda info --envs

# conda environments:
#
                         /home/pc/anaconda3
base                     /home/pc/miniconda3
h2ogpt                   /home/pc/miniconda3/envs/h2ogpt
new_env                  /home/pc/miniconda3/envs/new_env


to run a program 


Have to make sure beutful soup is installed 

pip install beautifulsoup4

after install is complete you can check that it installed correclty by 

pip list

# move the python code to the bin directory and hit run? 

import requests
from bs4 import BeautifulSoup

url = 'https://www.drudgereport.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the first <h1> tag on the page
h1_tag = soup.find('h1')

if h1_tag:
    print(f'The first <h1> tag is: {h1_tag.text}')
else:
    print('No <h1> tag found.')


https://www.drudgereport.com/
