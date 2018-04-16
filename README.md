# gtf-bot
A Telegram bot for GTFS running at aws lambda using GTFS from [gla-tmb-fda](https://github.com/hugosenari/gla-tmb-fda)

Requirements
------------

This project uses [pipenv](https://docs.pipenv.org/) to manage its dependencies, it can be installed
on macOS using [Homebrew](https://brew.sh) by typing `$ brew install pipenv`.

Installation
------------

This project uses [Zappa](https://github.com/Miserlou/Zappa) to deploy to AWS
lambda. Zappa is installed in an isolated environment by running:

    ```sh
    pipenv install
    ```

Deployment
----------

See [Zappa documentation](https://github.com/Miserlou/Zappa),
you will need to have your AWS credentials setup, and then you can run Zappa inside of your
virtualenv:

    ```sh
    pipenv run zappa deploy
    ```

Then set two env vars at AWS Lambda Function:

- BOT_WEBHOOK_URL: url of this api (provided by zappa after deploy)
- BOT_TOKEN: token of your bot (provided by [BotFather](https://telegram.me/BotFather))

And set your webhook on your bot:

    ```sh
    pipenv run zappa invoke 'gtf_bot.bot.set_webhook'
    ```
