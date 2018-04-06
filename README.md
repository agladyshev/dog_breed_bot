# [@dogbreeder](https://t.me/dogbreeder_bot)
This is a bot for telegram which can receive a photo input from user and provide multiple feedback:
- if the photo contains a dog, which breed is it
- if the photo depicts a human, which dog breed does he/she look like
- if there is neither a dog or a person in the photo, the error message is sent

## To run the bot locally
- Ask [BotFather](https://t.me/BotFather) to create new bot
- Get TOKEN to access Telegram API
- Clone this project
- Create conda environment from file `conda env create -f requirements-local.yml`
- Set TOKEN as an environment variable or edit set TOKEN directly in webapp/main.py
- Start bot with `python webapp/main.py`
- Send a photo to you bot in telegram

## To deploy to Heroku
- Have Docker and Heroku installed on your machine
- Clone the project and run terminal from project directory
```
     $ heroku plugins:install heroku-container-registry
     $ heroku container:login
     $ heroku create
     $ heroku container:push web
```
- Set TOKEN as an environment variable in the project settings in Heroku dashboard