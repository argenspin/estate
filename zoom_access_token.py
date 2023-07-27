import requests
ACCOUNT_ID = 'I5G9MgEDSNyLnL_bR-WNHA'
ZOOM_CLIENT_ID = 'a1D7SdoMQW6_ONtSAOk8A'
ZOOM_CLIENT_SECRET = 'PjuJiMKKIA3m9VehX9UwgOs3YEE0Iq2U'
token_url = 'https://zoom.us/oauth/token'
ZOOM_CREATE_MEETING_URL = 'https://api.zoom.us/v2/users/me/meetings'

data = {
'grant_type': 'account_credentials',
'account_id': ACCOUNT_ID,
'client_id': ZOOM_CLIENT_ID,
'client_secret': ZOOM_CLIENT_SECRET,
#'redirect_uri': REDIRECT_URI,
}
response = requests.post(token_url,data=data)
print(response.json())
access_token = response.json().get('access_token')

def create_zoom_meeting(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    data = {
        'topic': 'My Zoom Meeting',
        'type': 1,  # 2 for scheduled meeting, 3 for recurring meeting
        #'start_time': '2023-07-29T12:20:00',  # Replace with the desired start time
        'duration': 30,  # Meeting duration in minutes
        'timezone': 'UTC',  # Replace with the desired timezone
        'agenda': 'Agenda for the meeting',
        'use_pmi':True
    }

    response = requests.post(ZOOM_CREATE_MEETING_URL, headers=headers, json=data)
    print(response.json())
    print(response.status_code)
create_zoom_meeting(access_token)

