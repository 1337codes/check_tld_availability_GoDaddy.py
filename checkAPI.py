import requests

# Replace with your actual API key and secret
GODADDY_API_KEY = 'your_api_key'
GODADDY_API_SECRET = 'your_api_secret'

def check_api_key(api_key, api_secret):
    url = "https://api.godaddy.com/v1/domains/available?domain=example.com"
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        
        if response.status_code == 403:
            print("Access denied. Please check your API key permissions.")
        elif response.status_code == 401:
            print("Authentication failed. Please check your API key and secret.")
        elif response.status_code == 200:
            print("Authentication succeeded.")
        else:
            print(f"Unexpected status code: {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to test the credentials
check_api_key(GODADDY_API_KEY, GODADDY_API_SECRET)
