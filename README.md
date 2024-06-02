# BUM Tester
This is a repo that contains the source code of a website, that helps FME BUT students to walk through some of the possible questions.
Project as such works with django backend, gunicorn, and nginx for static files(eg. images, css and js) serving.
## Requirements
Project depends to have docker installed, what it will download into container is up to him.

## How to launch it
This project utilizes docker for running, so for a quick combo copy this snippet and paste it into terminal.
```
git clone https://github.com/lotricekCZ/BUM-tester.git \
&& cd BUM-tester \
&& docker compose up --build
```
In case nothing was using port 80, you can access this site on http://127.0.0.1/BUM-tester/
## Contributions
If you have any ideas on what to improve on this project, hit me up in github issues