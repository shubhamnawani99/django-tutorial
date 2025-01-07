# Installation and initial steps to configure Django
- Install uv - alternative to pip with faster speed (similar to bun in js)
- Create a virtual environment - uv venv (creates a folder named .venv)
- Activate the venv using - .\\.venv\Scripts\activate
- Installation - uv pip [package-name]

### Running Django Server
- **django-admin** startproject [project-name] (django-admin is provided once Django is installed by default)
- cd [project-name]
- python .\manage.py runserver [port-number](command to run the server)

## Manage.py
- Starting point of Django Code

## Settings.py
- All the configurations are set here for project-level (extremely powerful)

## URL.py
- All the routing are set here