from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import openai
import gspread
from oauth2client.service_account import ServiceAccountCredentials

model = "gpt-3.5-turbo"
sheet_id = '1bhCpAd0v0cN9DQe_OOaG8sGm8VlH5pNhgpGowR9vVkU'
openAI_API_key = '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'


class ActionVan(Action):
    def name(self):
        return "action_van"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        # Your logic to fetch the van schedule and send it as a response to the user
        # ...

        latest_message = tracker.latest_message.get('text')

        dispatcher.utter_message(
            text=f"The van schedule is from 8:00 am to 5:00 pm on weekdays.")

        return []


class ActionOfficeHours(Action):
    def name(self):
        return "action_office_hours"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        # Your logic to fetch the office hours and send it as a response to the user
        # ...
        latest_message = tracker.latest_message.get('text')
        
        worksheet_name = "office_hours"
        rows = read_google_spreadsheet(sheet_id, worksheet_name)
        
        system = "You are Al Akhawayn university assistant for students. you help them find office hours for their professors:" + str(rows)

        dispatcher.utter_message(
            text=chat_response(system, latest_message))
        return []


class ActionEvent(Action):
    def name(self):
        return "action_event"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        # Your logic to fetch the events happening and send it as a response to the user
        # ...
        latest_message = tracker.latest_message.get('text')

        worksheet_name = "events"
        rows = read_google_spreadsheet(sheet_id, worksheet_name)
        
        print(rows)

        system = "You are Al Akhawayn university assistant for students. you help them find events on campus:" + str(rows)

        dispatcher.utter_message(
            text=chat_response(system, latest_message))

        return []


class ActionOpeningHours(Action):
    def name(self):
        return "action_opening_hours"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        # Your logic to fetch the opening hours and send it as a response to the user
        # ...
        latest_message = tracker.latest_message.get('text')

        worksheet_name = "opening_hours"
        rows = read_google_spreadsheet(sheet_id, worksheet_name)
        
        print(rows)
        
        system = "You are Al Akhawayn university assistant for students. you help them find opening hours of services at the university:" + str(rows)

        dispatcher.utter_message(
            text=chat_response(system, latest_message))
        return []


def read_google_spreadsheet(sheet_id, worksheet_name):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        '/Users/ahmedjaafari/AuiAssistant/actions/custom-name-381012-da941d5e5107.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id).worksheet(worksheet_name)
    data = sheet.get_all_values()
    headers = data.pop(0)
    rows = []
    for row in data:
        row_dict = {}
        for i in range(len(headers)):
            row_dict[headers[i]] = row[i]
        rows.append(row_dict)
    return rows


def chat_response(system, latest_message):
    openai.api_key = openAI_API_key 
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": latest_message},
        ]
    )
    return response['choices'][0]['message']['content'].strip()
