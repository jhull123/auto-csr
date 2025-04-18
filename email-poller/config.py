from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_credentials():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    return flow.run_local_server(port=0)

