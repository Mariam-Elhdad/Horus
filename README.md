# horus

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy horus

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd horus
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Deployment

The following details how to deploy this application.

### Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).


### path for APIs
```
horus
├── blog
│   ├── api
│   └── migrations
├── contrib
│   └── sites
│       └── migrations
├── events
│   ├── api
│   └── migrations
├── media
│   ├── events_images
│   └── images
│       └── historical_places
├── museums
│   ├── api
│   └── migrations
├── reviews
│   ├── api
│   └── migrations
├── search
│   ├── api
│   └── migrations
├── service
│   ├── api
│   ├── management
│   │   ├── __pycache__
│   │   └── commands
│   │       └── __pycache__
│   └── migrations
├── static
│   ├── css
│   ├── fonts
│   ├── images
│   │   └── favicons
│   └── js
├── templates
│   ├── account
│   ├── pages
│   └── users
├── user_profile
│   ├── api
│   └── migrations
├── users
│   ├── api
│   ├── migrations
│   └── tests
└── utils

```

### database design
   - <a href="https://lucid.app/lucidchart/6c102840-beb6-40cc-8986-41c6915913f5/edit?viewport_loc=-106%2C999%2C2200%2C1147%2C0_0&invitationId=inv_19e5cb20-d9a8-4ca6-8395-696b88aa7366"> <h3> erd digram</h3> </a>
   - <a href="https://lucid.app/lucidchart/1552b69b-b77d-4715-9dc9-4ea2a7fb2715/edit?view_items=3~_6PkoQaWxn&invitationId=inv_022baf83-6e72-4b75-aa5e-7352775529f8"> <h3> model design diagram</h3> </a>

### technologies:
   - Django & djangorestframework
   - PostgreSQL
   - Elasticsearch
   - Docker
   - makefile

### Steps:
   1. Database design
   2. Build the initial project using cookie cutter
   3. make a custome user
   4. using djsore for authorization and using JWT token
   5. make the default permission is Authenticated
   6. building user profile for CRUD operations
   7. building the services(restaurant, bank and hotel) app and add search by location
   8. building blogs where the user can make CRUDs on blog and (upvote, downvote, comment, reply on comment, ..etc)
   9. building events and only admin can make CRUD on it, but normal user can view all events or the current and the future also user can mention that he will go to the event
   10. building museums which type of services but have relation with different items.
   11. building search that uses elasticsearch to get the match with high speed and high quality results, we do search on the all services and get the list of results
   12. reviews the user can add reviews on the services to give feedback about the place
   13. adding favorite to save favorite items
