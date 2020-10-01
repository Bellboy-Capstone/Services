
# Services

<!-- All badges get added here. -->

![CI](https://github.com/Bellboy-Capstone/Services/workflows/CI/badge.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8fb53c0f016b46889a92c8bc37d26bbe)](https://www.codacy.com/gh/Bellboy-Capstone/Services/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Bellboy-Capstone/Services&amp;utm_campaign=Badge_Grade)


Django Application for monitoring Bellboy devices, also provides a frontend for staff to monitor devices and interact with device users.



## Development Instructions

To work on this repository, you'll need to download and install _Pycharm_ and _Docker Desktop_.

To run the development environment, type `docker-compose -f local.yml up`

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
