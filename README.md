# Django Rest Framework API Project Reference
## Overview
This a simple sample app repo for the purposes of experimentation and sharing of examples.
## Requirements
* Python (3.7)
## Running
`python manage.py runserver`
## Tests
`python manage.py test`
`python manage.py test --no-skip`

* Tests produce coverage results that you can view by opening the generated `./cover/index.html` file.
* You can ignore a specific line from coverage by adding a `# pragma: no cover` 
comment to the end of the line
* The minimum coverage allowed setting can be set via `NOSE_COVER_MIN_PERCENTAGE`
* If you need a wait for coverage to finish reporting set `NOSE_COVER_WAIT`
* Other [Coverage Docs](https://coverage.readthedocs.io/en/latest/index.html)
