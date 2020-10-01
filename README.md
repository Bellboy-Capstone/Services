
# Services

<!-- All badges get added here. -->

![CI](https://github.com/Bellboy-Capstone/Services/workflows/CI/badge.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8fb53c0f016b46889a92c8bc37d26bbe)](https://www.codacy.com/gh/Bellboy-Capstone/Services/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Bellboy-Capstone/Services&amp;utm_campaign=Badge_Grade)


Django Application for monitoring Bellboy devices, also provides a frontend for staff to monitor devices and interact with device users.



## Development Instructions

To work on this repository, you'll need to download and install _Pycharm_ and _Docker Desktop_.

Thanks to a convo with Sein, I've now included a collection of instructions for getting started and troubleshooting.

Generally, to run the development environment, type `docker-compose -f local.yml up`

### Setup

These instructions are for Windows 10, which the majority of our team uses. If running on a better OS it is assumed that you are skilled enough to figure all this out by yourself.

1. Install Docker Desktop from [this link](https://www.docker.com/products/docker-desktop). Ensure that you install the WSL2 binaries.
2. Ensure the WSL integrations are enabled, as seen in the screenshot below:
    ![WSL integrations should be enabled in the docker dashboard](/readme/wsl-integrations.png)
3. Ensure that everything works by running the following command:
    ```sh
    # Can be run in powershell or in WSL, but preferably WSL:
    docker-compose -f local.yml run django pytest
    ```

Your system should now be ready to do basic development. Any changes you make will be hot-reloaded.



```sh
# Install requirements:
# (In admin console on windows)
pip install -r requirements.txt
# (Or on linux/OSX)
python3 -m pip install -r requirements.txt

# Set up pre-commit
pre-commit install

# Launch the Services component with docker
docker-compose -f local.yml up

# Run the unit tests
docker-compose -f local.yml run django pytest

# Branch and start hacking!
git checkout -b my-new-branch-name
```

### Using the Services Docker Environment

TBC
