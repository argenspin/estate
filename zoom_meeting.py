import requests

# Replace these with your Zoom OAuth App credentials
ZOOM_CLIENT_ID = 'y97TeksySHa_r3eIDCWjZg'
ZOOM_CLIENT_SECRET = 'PjuJiMKKIA3m9VehX9UwgOs3YEE0Iq2U'
REDIRECT_URI = 'https://01ff-49-37-225-3.ngrok-free.app'

# Zoom API endpoint to create a meeting
ZOOM_CREATE_MEETING_URL = 'https://api.zoom.us/v2/users/me/meetings'

def get_oauth_access_token(code):
    # Exchange the authorization code for an OAuth access token
    token_url = 'https://zoom.us/oauth/token'
    data = {
        'grant_type': 'accoun',
        'account_id': code,
        'client_id': ZOOM_CLIENT_ID,
        'client_secret': ZOOM_CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
    }
    response = requests.post(token_url, data=data)

    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(f'Failed to get access token. Error: {response.text}')
        return None

def create_zoom_meeting(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    data = {
        'topic': 'My Zoom Meeting',
        'type': 2,  # 2 for scheduled meeting, 3 for recurring meeting
        'start_time': '2023-07-29T14:30:00',  # Replace with the desired start time
        'duration': 30,  # Meeting duration in minutes
        'timezone': 'IST',  # Replace with the desired timezone
        'agenda': 'Agenda for the meeting',
    }

    response = requests.post(ZOOM_CREATE_MEETING_URL, headers=headers, json=data)

    if response.status_code == 201:
        print('Meeting created successfully.')
        return response.json()
    else:
        print(f'Failed to create meeting. Error: {response.text}')
        return None

if __name__ == '__main__':
    # Assuming you have obtained the OAuth access token from the OAuth flow
    # and stored it in the 'access_token' variable
    access_token = 'your_oauth_access_token'
    create_zoom_meeting(access_token)
