import os
from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_automation.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = 'https://www.googleapis.com/auth/drive'

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def export_file(file, parents):
    if not os.path.exists(file):
        print('File path not found')
        return
    try:
        file_metadata = {'name': os.path.basename(file).replace('.csv', ''),
                         'mimeType': 'application/vnd.google-apps.spreadsheet', 'parents': parents}
        media = MediaFileUpload(filename=file, mimetype='text/csv')
        response = service.files().create(mediabody=media, body=file_metadata).execute()
        print(response)
        return response
    except Exception as e:
        print(e)
        return

