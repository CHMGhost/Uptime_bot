from ping3 import ping
import time
import json
import os
import requests

# Config file that will store the devices information
config_file = 'config.json'


def load_devices(file):
    devices = []
    try:
        if os.path.isfile(config_file):
            with open(config_file) as f:
                devices = json.load(f)
    except Exception as e:
        print(f"Failed to load devices from {config_file}: {e}")
    return devices


def save_devices(file, devices):
    with open(file, 'w') as f:
        json.dump(devices, f)


def prompt_devices():
    devices = []
    while True:
        device = input("Enter device hostname (type 'done' when finish): ")
        if device.lower() == 'done':
            break
        else:
            devices.append(device)
    return devices


def ping_devices(devices):
    offline_devices = []
    for device in devices:
        try:
            delay = ping(device)
            if delay is None:
                print(f'{device} is offline')
                offline_devices.append(device)
            else:
                print(f'{device} is online, ping in {delay} seconds')
        except Exception as e:
            print(f'An error has occurred: {e}')
    return offline_devices


def send_notice(event, hostname, api_key):
    url = f"https://maker.ifttt.com/trigger/{event}/with/key/{api_key}"
    data = {"value1": hostname}
    requests.post(url, data=data)


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
                    send_notice("device_offline", device, api)
            else:
                print("All devices are online.")
            time.sleep(60)
        except KeyboardInterrupt:
            print("\nExiting program.")
            break


if __name__ == '__main__':
    main()
