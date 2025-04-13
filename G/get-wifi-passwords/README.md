# get_wifi_passwords

The "get_wifi_passwords" project is a Python script that allows you to extract saved Wi-Fi profiles and their associated passwords from both Windows and Linux machines. It uses different methods for each operating system to retrieve this information.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3.x installed on your machine.
- The required Python packages installed. You can install them using pip:

  ```bash
  pip install configparser
  ```

## Usage

1. Download the script to your local machine.

2. Open your command prompt or terminal.

3. Navigate to the directory where the script is located.

4. Run the script by executing the following command:

   ```bash
   python get_wifi_passwords.py
   ```

   This will display a list of saved Wi-Fi profiles and their associated passwords.

## Supported Operating Systems

The script can extract Wi-Fi profiles from the following operating systems:

- Windows
- Linux

The appropriate method is automatically selected based on your operating system.

## Windows Usage

For Windows users, the script uses the `netsh` command to extract saved Wi-Fi profiles. It lists the SSID (network name), encryption ciphers, and Wi-Fi password (key).

## Linux Usage

For Linux users, the script extracts information from configuration files stored in the `/etc/NetworkManager/system-connections/` directory. It displays the SSID, authentication algorithm, key management type, and pre-shared key (PSK) for each profile.

## Customizing Output

You can customize the output verbosity by modifying the `verbose` parameter in the `print_profiles` function. The default value is set to `1`, which displays information for each profile. You can set it to `0` to suppress real-time output.

## License

There's no license details available about this project.

## Note

This code is provided as-is and may require modifications to work on different system configurations. Please use it responsibly and respect privacy and security considerations.

---

Feel free to further customize and expand upon this README as needed. Make sure to include a license file (`LICENSE`) with the appropriate license text if you plan to distribute or share the code
