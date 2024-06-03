# BUM Tester
This is a repo that contains the source code of a website, that helps FME BUT students to walk through some of the possible questions in [BUM](https://www.fme.vutbr.cz/studenti/predmety/266488).
Project as such works with django backend, gunicorn, and nginx for static files(eg. images, css and js) serving.
## Requirements
Project depends on docker, what it will download into container is up to him.

## How to launch it
Paste this snippet into terminal and wait.
```
git clone https://github.com/lotricekCZ/BUM-tester.git \
&& cd BUM-tester \
&& docker compose up --build
```
In case nothing was using port 80, you can access this site on http://127.0.0.1/BUM-tester/
## Contributions
If you have any ideas on what to improve on this project, hit me up in github issues.
## Known issues
 - README.md -README might be a little more verbose