# Domain Availability Checker

A Python script to check the availability of domain names across various TLDs using the GoDaddy API.

## Features

- Checks domain availability using the GoDaddy API
- Supports multiple TLDs from a provided text file
- Saves available domains to a results file

## Requirements

- Python 3.x
- `requests` library

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/1337codes/check_tld_availability_GoDaddy.py.git
    cd check_tld_availability_GoDaddy.py
    ```

2. **Install the required Python packages:**
    ```bash
    pip install requests
    ```

3. **Set up GoDaddy API credentials:**

    Ensure you have your GoDaddy API key and secret. You can set them as environment variables:

    ```bash
    export GODADDY_API_KEY='your_api_key'
    export GODADDY_API_SECRET='your_api_secret'
    ```

    Or replace the `os.getenv` calls in the script with your actual API key and secret.

4. **Prepare your TLD file:**

    Ensure you have a file named `tlds.txt` in the same directory as the script, or provide a different file when running the script. The file should contain a list of TLDs, one per line.

## Usage

Run the script and follow the prompts:

```bash
python check_tld_availability.py

Example:
Enter base domain name: example
Enter TLD file name (or press Enter to use tlds.txt):

Created by
1337 Company
