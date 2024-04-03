<p align="center">
    <img src="https://i.imgur.com/FIHv9aS.png" alt="ClipIt-Banner">
</p>

#  Telescrape 
Telescrape is a tool designed to extract member information from public Telegram groups and channels.

## Features
- Scrape group or channel members.
- Scrape multiple groups or channels at once.
- Scrape members based on their activity and other customizable parameters.
- Save scraped data to .csv files.
- Easy to use GUI.

## Limitations
- Only public groups or channels.
- Only up to 10.000 members per group or channel.

## Demo

## Installation
- Download and install **Python 3.12**.
- Open a **Git Bash** or **PowerShell** terminal.
- Clone the repository: `git clone [repository URL]`
- Navigate to the cloned directory via the terminal: `cd "[directory path]"`
- Create a virtual environment: `py -3.12 -m venv venv`
- Activate the virtual environment:
  - bash: `source venv/Scripts/activate`
  - pwsh: `.\venv\Scripts\activate`
- Install project's dependencies: `pip install .`
- Start the application: `python src`

## How to get the API ID & API Hash?
1. [Login to your Telegram account](https://my.telegram.org/auth) with the phone number you're going to be using.
2. Click **API development tools**.
3. Fill in the **App title** and **Short name** fields with any values you prefer. The remaining fields can be left blank.
4. Click **Create application**.
5. **App configuration** page will open where you will find your API ID and API Hash.

## License
[MIT](LICENSE)
