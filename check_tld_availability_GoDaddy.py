import requests
import time
import json

GODADDY_API_KEY = 'your_api_key'  # Replace with your actual API key
GODADDY_API_SECRET = 'your_api_secret'  # Replace with your actual API secret

def check_domain_availability(base_name, tld_file="tlds.txt"):
    """Checks availability of a given base name across TLDs from a file using GoDaddy API."""

    available_tlds = []
    checked = 0

    with open(tld_file, "r") as file:
        for tld in file:
            tld = tld.strip()
            domain = base_name + tld
            print(f"Checking: {domain}")
            
            try:
                response = requests.get(
                    f"https://api.godaddy.com/v1/domains/available?domain={domain}",
                    headers={
                        "Authorization": f"sso-key {GODADDY_API_KEY}:{GODADDY_API_SECRET}"
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"Response for {domain}: {json.dumps(data, indent=2)}")  # Debugging line

                    if data.get('available', False):
                        available_tlds.append(domain)
                        print(f"\033[92mAvailable: {domain}\033[0m")  # Green color
                    else:
                        print(f"\033[91mTaken: {domain}\033[0m")  # Red color
                else:
                    print(f"\033[91mError {response.status_code} for {domain}: {response.text}\033[0m")

            except Exception as e:
                print(f"\033[91mError checking {domain}: {e}\033[0m")
            
            checked += 1
            if checked % 10 == 0:
                time.sleep(1)

    return available_tlds

if __name__ == "__main__":
    base_name = input("Enter base domain name: ")
    tld_file = input("Enter TLD file name (or press Enter to use tlds.txt): ")
    if not tld_file:
        tld_file = "tlds.txt"

    available_domains = check_domain_availability(base_name, tld_file)

    if available_domains:
        with open("results.txt", "w") as outfile:
            outfile.write("Available domains:\n")
            for domain in available_domains:
                outfile.write(domain + "\n")
        print("\nResults also saved to results.txt")
    else:
        print("No available domains found for the given base name.")
