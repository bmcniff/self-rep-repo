# Self Replicating Repository
## Technical Specification Documentation

### What is this app doing?

This app requests access to a user's profile and then creates a copy of it's own code on the user's profile. It then provides a link to this new repo.

### How is this app doing this?

This app makes use of Flask-dance, a Python library which incorporates Flask and OAuth authentication to allow access to user accounts without requesting login credentials.

The app can then be run locally, or on Heroku.
