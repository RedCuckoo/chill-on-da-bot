# Chill-On-Da Bot

## Requirements
1. Running
   * [python ^3.9](https://www.python.org/)

2. Linting
   * flake8
   * black

3. Tests
   * pytest

# Local development

1. Create or use existing testing bot
2. Put token in TELEGRAM_TOKEN env.
3. Running
3.1. run main.py
```shell
python main.py
```
3.2. run docker-compose.yaml
```shell
TELEGRAM_TOKEN=<token> docker-compose up [-d]
```
if token is in PATH, just start command with _docker-compose_

when introduced changes, don't forget to rebuild
```shell
docker-compose up --build [-d]
```
_**-d** - optional flag to run in detached mode_

**OR** any variation with building docker image from Dockerfile and running it

# Deployment

Github actions automatically builds, tags and deploys

# Contributions

Repo maintainers may push to main

Open pull request for developers from outside of organization