import requests

# Replace with your actual API key and secret
GODADDY_API_KEY = 'your_api_key'
GODADDY_API_SECRET = 'your_api_secret'

def check_api_key(api_key, api_secret):
    url = "https://api.godaddy.com/v1/domains/available?domain=example.com"
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}"
    }
    
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

# Call the function to test the credentials
check_api_key(GODADDY_API_KEY, GODADDY_API_SECRET)
