
# Moratab Pdf Server

## Heroku Config

    heroku buildpacks:set heroku/python
    heroku buildpacks:add --index 2 heroku/nodejs
    heroku buildpacks:add --index 3 https://github.com/heroku/heroku-buildpack-google-chrome
