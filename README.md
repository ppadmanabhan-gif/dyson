# dyson_API

Control your Dyson fan / purifier from your computer using Python.

## What you need
- Python 3.9 or newer
- A Dyson account (the one you use in the MyDyson app)
- Your Dyson device connected to the same Wi-Fi as your computer

## Setup
```bash
pip install -r requirements.txt
```

## Step 1: Get your device details
```bash
python get_devices.py
```
Enter your email, country code (for example `SG`), password and the code Dyson emails you.
It prints the **Serial**, **Device Type** and **Credential** for each device.

Copy `config.example.json` to `config.json` and fill in those values,
plus your device's IP address (find it in your Wi-Fi router's device list).

> If login fails, log out of the MyDyson app, log back in, then try again.

## Step 2: Control your device
```bash
python control.py status
python control.py on
python control.py off
python control.py speed 5
```

## Warning
Never upload `config.json` to GitHub. It contains your device password.
It is already listed in `.gitignore` so Git will skip it.
