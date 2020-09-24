# SoccerAPI

SoccerAPI is an app containing data about soccer matches, teams and players.

### Endpoints

* match/<int:id>/ - match details
* match/ - match list
* match/<int:id>/passes - match pass list
* match/<int:id>/shots - match shot list
* team/<int:id>/ - team details
* team/ - team list
* player/<int:id>/ - player details
* player/ - player list

### Tech

SoccerAPI uses:

* [Django] - web app framework for Python
* [Django Rest Framework] - REST API framework for Django
* [Django-CORS-Headers] - CORS headers for Django projects


### Installation

SoccerAPI requires Python 3.6.7 to run.

Install the dependencies and devDependencies and start the server.

```sh
$ pip install -r requirements.txt
$ python soccer/manage.py runserver
```

