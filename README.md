
# Services

<!-- All badges get added here. -->

![CI](https://github.com/Bellboy-Capstone/Services/workflows/CI/badge.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8fb53c0f016b46889a92c8bc37d26bbe)](https://www.codacy.com/gh/Bellboy-Capstone/Services/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Bellboy-Capstone/Services&amp;utm_campaign=Badge_Grade)
[![Updates](https://pyup.io/repos/github/Bellboy-Capstone/Services/shield.svg)](https://pyup.io/repos/github/Bellboy-Capstone/Services/)
[![Python 3](https://pyup.io/repos/github/Bellboy-Capstone/Services/python-3-shield.svg)](https://pyup.io/repos/github/Bellboy-Capstone/Services/)



Django Application for monitoring Bellboy devices, also provides a frontend for staff to monitor devices and interact with device users.

## Development Instructions

To work on this repository, you'll need to download and install _Pycharm_ and _Docker Desktop_.

Thanks to a convo with Sein, I've now included a collection of instructions for getting started and troubleshooting.

Generally, to **run the development environment**, type `docker-compose -f development.yml up`

Services API docs are hosted at <https://bellboy-services.herokuapp.com/swagger/>

### Setup

**These instructions are for Windows 10, which the majority of our team uses. If running on a better OS it is assumed that you are skilled enough to figure all this out by yourself.**

1. Install Docker Desktop from [this link](https://www.docker.com/products/docker-desktop). Ensure that you install the WSL2 binaries.
2. Ensure the WSL integrations are enabled, as seen in the screenshot below:
    ![WSL integrations should be enabled in the docker dashboard](/readme/wsl-integrations.png)
    You **do not need to use the Windows Subsystem for Linux (WSL) on GNU/Linux or OSX.**
1. If you have problems with speed or stability in WSL, it's fine to use the Hyper-V backend.
3. Ensure that everything works by running the following command:
    ```sh
    docker-compose -f development.yml run django pytest
    ```
    If all the unit tests pass, you're good to go! Your system should now be ready to do basic development. Any changes you make will be hot-reloaded after running this:
    ```sh
    docker-compose -f development.yml up
    ```


### Creating a New Branch

```sh
git checkout -b <new branch name>
git push --set-upstream origin <new branch name>
```

### Developing with the Bellboy Services Docker Environment

The database containers can also be accessed externally, allowing you to run `manage.py` commands from outside the container, but on Windows 10, it may be difficult to successfully install all of the django dependencies, especially `psycopg2`, and you should probably stick to running commands in the container like so:

```sh
docker-compose -f development.yml run django <your cmd here>
```


### Starting a New Django Application

Within the Services project, functionality is organized into apps.
For example, there could be an app to manage users, an app to run an
endpoint to manage camera data, and an endpoint to continuously process
incoming data from successful ultrasonic activations.

The filesystem is organized like so:

```
Services (root folder)
  - services (application folder)
    - users
    - utils
    - <your app here>
```

To add a new app, you'll need to do these things:

1. Know what you want to name your new app.
1. Right-click the 'services' folder and add a new python package.
1. Inside the folder, there should exist a file called `__init__.py`, just make sure it's there.
1. Create a new python file in the folder called `apps.py`, and add the following:
   ```py
   from django.apps import AppConfig
   from django.utils.translation import gettext_lazy as _

   class <AppName>Config(AppConfig):
       name = "services.<appname>"
       verbose_name = _("<App Name>")
   ```
1. Now the app needs to be added to the `LOCAL_APPS` list in config > settings > `base.py`:
   ```py
   LOCAL_APPS = [
     "services.users.apps.UsersConfig",
     # Your stuff: custom apps go here
     "services.<appname>.apps.<AppName>Config"
   ]
   ```
1. That's it, your new app will be loaded and run when Django starts.
1. Enjoy a scoop of ice cream.

<br />

## Old Instructions

```sh
# Install requirements:
# (In admin console on windows)
pip install -r requirements.txt
# (Or on linux/OSX)
python3 -m pip install -r requirements.txt

# Set up pre-commit
pre-commit install

# Launch the Services component with docker
docker-compose -f development.yml up

# Run the unit tests
docker-compose -f development.yml run django pytest

# Branch and start hacking!
git checkout -b my-new-branch-name
```
