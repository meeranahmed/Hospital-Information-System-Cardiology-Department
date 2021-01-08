from db import db
from datetime import datetime,timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event

class AppointmentModel(db.Model):
    __tablename__ = "Appointments"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)

    doctor_id = db.Column(db.Integer, db.ForeignKey("Doctors.id"), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("Patients.id"), nullable=False)

    doctor = db.relationship("DoctorModel")
    patient = db.relationship("PatientModel")

    def __init__(self, date, doctor_id, patient_id, created_at):
        self.date = date
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.created_at = created_at

    def json(self):
        return {
            "_id": self.id,
            "date": str(self.date),
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date_of_reservation": str(self.created_at),
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_date(cls,date):
        return cls.query.filter_by(date=date).all()    

    # def main(start_time):
    #  SCOPES = ['https://www.googleapis.com/auth/calendar']
    #  creds = None

    #  if os.path.exists('token.pickle'):
    #     with open('token.pickle', 'rb') as token:
    #         creds = pickle.load(token)

    #  if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'client_secret2.json', SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     with open('token.pickle', 'wb') as token:
    #         pickle.dump(creds, token)

    #  service = build('calendar', 'v3', credentials=creds)
    #  end_time = start_time + timedelta(hours = 4 ) 
    #  event = {
    #   'summary': 'Doctor Appointment',
    #   'location': 'Cairo',
    #   'description': '',
    #   'start': {
    #   'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
    #   'timeZone': 'Africa/Cairo',
    #    },
    #   'end': {
    #   'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
    #   'timeZone': 'Africa/Cairo',
    #   },
    #   'reminders': {
    #   'useDefault': False,
    #  #'overrides': [
    #   #{'method': 'email', 'minutes': 24 * 60},
    #   #{'method': 'popup', 'minutes': 10},
    #   #],
    #   },
    #  }

    #  service.events().insert(calendarId='primary', body=event).execute()

    def calendar (start_time,email):

        calendar = GoogleCalendar('ehab.wahba98@eng-st.cu.edu.eg')

        event = Event(
         'The Glass Menagerie',
          start=start_time,
          location='Africa/Cairo',
          minutes_before_popup_reminder=15
         )

        calendar.add_event(event)




