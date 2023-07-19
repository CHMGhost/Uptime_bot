#!/usr/bin/env python3

import os
import json
import time
import requests
from ping3 import ping, verbose_ping

# Config file that will store the devices information
config_file = 'config.json'


def load_devices(file):
    try:
        if os.path.isfile(file):
            with open(file, 'r') as f:
                return json.load(f)
        else:
            return []
    except Exception as e:
        print(f"Failed to load devices from {file}: {e}")
        return []


def save_devices(file, devices):
    try:
        with open(file, 'w') as f:
            json.dump(devices, f)
    except Exception as e:
        print(f"Failed to save devices to {file}: {e}")


def prompt_devices():
    devices = []
    while True:
        device = input("Enter device IP (or 'done' when finish): ")
        if device.lower() == 'done':
            break
        else:
            devices.append(device)
    return devices


def ping_devices(devices):
    offline_devices = []
    for device in devices:
        delay = ping(device)
        if delay is None:
            print(f'{device} is offline')
            offline_devices.append(device)
            send_notice(device)
        else:
            print(f'{device} is online, ping in {delay} seconds')
    return offline_devices


def send_notice(device):
    event_name = 'device_offline'
    url = f"https://maker.ifttt.com/trigger/{event_name}/with/key/REPLACE_KEY"
    payload = {'value1': device}
    requests.post(url, data=payload)


def main():
    devices = load_devices(config_file)
    if not devices:
        devices = prompt_devices()
        save_devices(config_file, devices)

    while True:
        try:
            offline_devices = ping_devices(devices)
            if offline_devices:
                print("These devices are offline:")
                for device in offline_devices:
                    print(device)
            else:
                print("All devices are online.")
            time.sleep(60)
        except KeyboardInterrupt:
            print("\nExiting program.")
            break


if __name__ == '__main__':
    main()
