Kagojer Nouka Backend
======================

Run the Project Locally
-----------------------
1. Make `run_backend.sh` script executable if it is not by running `chmod +x run_backend.sh`
1. Run the server locally on port 8000 with command `./run_backend.sh`
 
Git Workflow
------------
1. Create a feature bran4ch with name styled `backend-feature-name`
1. Make your code change in the feature branch
1. Merge your code to the development branch (not master branch)
1. If everything works in development, merge the change in master
1. Delete the feature branch

Heroku Setup
------------
If you are not maintaining heroku integration or not experienced with it, don't push to heroku.
Contact with [ZunaedSifat](https://github.com/zunaedsifat) instead.
1. Run the project with heroku desktop client `heroku local web`
1. Add Heroku repository `heroku git:remote -a kagojer-nouka`
1. Rename the Heroku repository to `heroku-backend` by executing the command
`git remote rename heroku heroku-backend`
1. Push code to Heroku by executing from the project root `git subtree push --prefix backend heroku-backend master`
