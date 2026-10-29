"""Control a Dyson device on your local network.

Usage:
    python control.py status
    python control.py on
    python control.py off
    python control.py speed <1-10>
"""
import json
import sys

from libdyson import get_device


def load_config(path="config.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cfg = load_config()
    device = get_device(cfg["serial"], cfg["credential"], cfg["device_type"])
    if device is None:
        print("Unsupported device type:", cfg["device_type"])
        sys.exit(1)

    device.connect(cfg["host"])
    try:
        command = sys.argv[1].lower()
        if command == "on":
            device.turn_on()
            print("Turned on")
        elif command == "off":
            device.turn_off()
            print("Turned off")
        elif command == "speed" and len(sys.argv) == 3:
            device.set_speed(int(sys.argv[2]))
            print("Speed set to", sys.argv[2])
        elif command == "status":
            print("On:   ", device.is_on)
            print("Speed:", device.speed)
        else:
            print(__doc__)
    finally:
        device.disconnect()


if __name__ == "__main__":
    main()
