"""Log in to your Dyson account and print the details of your devices."""
from getpass import getpass

from libdyson.cloud import DysonAccount


def main():
    country = input("Country code (e.g. SG, US, GB): ").strip().upper()
    email = input("Email: ").strip()

    account = DysonAccount()
    verify = account.login_email_otp(email, country)
    password = getpass("Password: ")
    otp = input("Verification code from your email: ").strip()
    verify(otp, password)

    for device in account.devices():
        print()
        print(f"Name:        {device.name}")
        print(f"Serial:      {device.serial}")
        print(f"Device Type: {device.product_type}")
        print(f"Credential:  {device.credential}")


if __name__ == "__main__":
    main()
