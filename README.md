# T.I.T.A.N - Total Information Tactical Awareness Nexus

# FEATURES

/create_patrol
/create_mission
/create_frago

# SETUP - SELF HOSTING

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

# Hosting

I use https://cybrancee.com/ to host my bots (cheap too)

#### SETUP HOST - This is for those who want to use cybrancee


1. Go to the file tab

![Alt text](https://i.ibb.co/t4fgQLk/files.png "hosting")

2. Create a directory with 3 subdirectories (dragging folders won't work)
    - source
      - cogs
      - config
      - core

![Alt text](https://i.ibb.co/C5swKCB/source.png "hosting")

3. Drag and drop the files from the repository u have downloaded from setup
    - cogs - gpt_module.py
    - config - config.yml and rules.yml
    - core - loader.py

4. now go back to the root
    - drag the .env, start.py, requirements.txt files 
    - insure it looks like the image in step one (ignore the discord.log file the bot will create this when required)

5. Go to the startup tab

![Alt text](https://i.ibb.co/GxH1RSv/startup.png "hosting")

- set the REQUIREMENTS FILE to requirements.txt
- set the BOT PY FILE to start.py
- add discord.py to ADDITIONAL PYTHON PACKAGES

6. Go to the console tab

![Alt text](https://i.ibb.co/M2RKt1j/cmd.png "hosting")

- Press Start
- It will run the requirements.txt and install all the required packages
- 

If everything has been set up correctly, the bot should be running

![Alt text](https://i.ibb.co/JqcnD4Y/running.png "hosting")