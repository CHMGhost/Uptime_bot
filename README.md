# Uptime Bot

Uptime Bot is a Python-based application that continuously monitors the online status of devices on your home network. If a device goes offline, it triggers a notification via IFTTT.

## Installation

1. Clone this repository

```
git clone https://github.com/CHMGhost/Uptime_bot
```

1. Navigate to the project directory

```
cd Uptime_bot
```

1. Create a virtual environment and activate it

```
python3 -m venv venv
source venv/bin/activate
```

1. Install the required packages

```
pip install -r requirements.txt
```

## Configuration

1. Run the script once to create the `config.json` file:

```
python3 ping_devices.py
```

1. You will be prompted to enter the hostname of each device you want to monitor. Enter 'done' when you have added all your devices.
2. Set up an IFTTT applet that triggers when the "device_offline" event is received via a webhook, and sends you an email notification.
3. Replace the IFTTT key in the `main()` function with your actual IFTTT key.

## Usage

To start monitoring devices, run:

```
python3 ping_devices.py
```

The script will ping each device every 60 seconds, and if any device is offline, it will trigger the IFTTT event to send you an email.

Press Ctrl+C to stop the script.

## Running in the Background

You can use `nohup` to run this script as a background process:

```
nohup python3 /path/to/ping_devices.py &
```

This will keep the script running even after you log out or close the terminal.

