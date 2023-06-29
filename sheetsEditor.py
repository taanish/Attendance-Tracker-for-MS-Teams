import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import joinStatus


load_dotenv()
creds = {
    "type": os.getenv("TYPE"),
    "project_id": os.getenv("PROJECT_ID"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    "private_key": os.getenv("PRIVATE_KEY"),
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": os.getenv("AUTH_URI"),
    "token_uri": os.getenv("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
}


def googleSheetsUpdater():

    scope = ['https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        creds, scope)
    client = gspread.authorize(credentials)

    sheet = client.open('Demo Attendance').sheet1
    sheet.clear()
    headers = ["Name", "Presence"]
    sheet.append_row(headers)
    sheet.append_row([])

    attendanceReport = joinStatus.attendanceReportGenerator()
    for i in attendanceReport:
        sheet.append_row(i)


googleSheetsUpdater()
