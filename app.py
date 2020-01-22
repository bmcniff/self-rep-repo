from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
import os


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissupposedtobeasecret'

github_blueprint = make_github_blueprint(client_id = '033b6cc3d24fbf5c354e', client_secret = '42b93a8dbe30ce9b373b505cbd2c212a880c490d')

app.register_blueprint(github_blueprint, url_prefix='/github_login')

get_username = os.environ.get('GITHUB_USERNAME','bmcniff')
get_repo_name = os.environ.get('REPOSITORY NAME','self-rep-repo')

@app.route('/')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))

    account_info = github.get('/user')
    if not account_info.ok:
        return "Something has gone wrong! Please try refreshing the page."

    fork_repo = github.post(f'/repos/{get_username}/{get_repo_name}/forks')

    if not fork_repo.ok:
        return "Something has gone wrong! Please try refreshing the page..."

        return '<h1>Your Github name is {}'.format(account_info_json['login'])

    return f'Success!'

if __name__ == "__main__":
    app.run()