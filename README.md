# Self Replicating Repository

To see a demo, click the following link: https://sheltered-escarpment-34153.herokuapp.com/

## Installation documentation:

Requirements:
Python
Git
Heroku CLI

Create accounts on:
Github
Heroku

### Install locally:
1. Clone this repo or download the zip file here: https://github.com/bmcniff/self-rep-repo/archive/master.zip
2. In CMD/terminal, cd 'path/to/self-rep-repo-master'
3. Enter the following commands:
  'python -m venv venv'
  'venv\Scritps\activate' (for PC) 'source venv/bin/activate' (for Linux/OSX)
  'python -m pip install -r requirements.txt'
  'flask run'
4. Create Oauth app on Github:
  a. Navigate to: https://github.com/settings/developers
  b. Select 'OAuth Apps"
  c. 'New OAuth App'
  d. Create application:
    Application name can be anything you'd like
    Homepage URL - http://127.0.0.1:5000/
    Application description can be anything you'd like
    Authorization callback URL - http://127.0.0.1:5000/github_login/github/authorized
    Register application
5. Navigate to http://127.0.0.1:5000/

### Install on Heroku:


