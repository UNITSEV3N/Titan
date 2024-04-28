# T.I.T.A.N - Total Information Tactical Awareness Nexus

# SETUP

1. Install python 3.12.3 - https://www.python.org/downloads/
2. Clone the repository `git clone https://github.com/UNITSEV3N/Titan.git`
3. Rename example.env to .env
4. Add your discord bot token and openai key in the .env file
5. Configure config.yml
```
ROLES = all the roles u want to be able to use AI commands
TEMPERATURE = accuracy of the bots generated prompts 0.0 - 1.0 (default 0.3)
MAX_TOKENS = 0 -> 4096
DEFAULT_MODEL = Default -> gpt-3.5-turbo
DEFAULT_GUILD = your guild/server ID
PRESENCE = Custom Status
```
6. Add or remove rules/templates in rules.yml
7. Install the required packages run ``pip install -r .\requirements.txt``
8. Run bot ``python start.py``
