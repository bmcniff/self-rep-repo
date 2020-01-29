# Self Replicating Repository

## Installation documentation:

To see a demo, click the following link: https://sheltered-escarpment-34153.herokuapp.com/

**Requirements:**  
Python - https://www.python.org/downloads/  
Git - https://git-scm.com/book/en/v2/Getting-Started-Installing-Git  
Heroku CLI - https://devcenter.heroku.com/articles/heroku-cli  

**Create accounts on:**  
Github - https://github.com/login  
Heroku - https://id.heroku.com/  

### Install locally:

1. Clone this repo or download the zip file here: https://github.com/bmcniff/self-rep-repo/archive/master.zip

2. In CMD/terminal, cd 'path/to/self-rep-repo-master'

3. Enter the following commands:  
  'python -m venv venv'  
  'venv\Scripts\activate' (for PC) 'source venv/bin/activate' (for Linux/OSX)  
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

1. Clone this repo or download the zip file here: https://github.com/bmcniff/self-rep-repo/archive/master.zip

2. In CMD/terminal, cd 'path/to/self-rep-repo-master'

3. Enter the following commands:  
  'virtualenv env'  
  'venv\Scripts\activate' (for PC) 'source venv/bin/activate' (for Linux/OSX)  
  'pip install flask'  
  'pip install gunicorn'  
  'git init'  
  'git add .'  
  'git commit -m "first commit"'  
  'heroku create' - Take note of the http://your-app.herokuapp.com link, it is needed in the next step  
  
4. Create Oauth app on Github:  
  a. Navigate to: https://github.com/settings/developers  
  b. Select 'OAuth Apps"  
  c. 'New OAuth App'  
  d. Create application:  
    Application name can be anything you'd like  
    Homepage URL - http://your-app.herokuapp.com  
    Application description can be anything you'd like  
    Authorization callback URL - http://your-app.herokuapp.com/github_login/github/authorized  
    Register application  
    
5. Navigate to http://your-app.herokuapp.com
