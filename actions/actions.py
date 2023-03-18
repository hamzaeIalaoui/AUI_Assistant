from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionVan(Action):
    def name(self):
        return "action_van"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        # Your logic to fetch the van schedule and send it as a response to the user
        # ...
        
        latest_message = tracker.latest_message.get('text')
        print(latest_message)

        dispatcher.utter_message(text=f"The van schedule is from 8:00 am to 5:00 pm on weekdays.")

        return []

class ActionOfficeHours(Action):
    def name(self):
        return "action_office_hours"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        # Your logic to fetch the office hours and send it as a response to the user
        # ...
        latest_message = tracker.latest_message.get('text')
        
        dispatcher.utter_message(text=f"The office hours of professors vary. Please check with the professor or department directly for their office hours.")

        return []

class ActionEvent(Action):
    def name(self):
        return "action_event"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        # Your logic to fetch the events happening and send it as a response to the user
        # ...
        latest_message = tracker.latest_message.get('text')
        
        dispatcher.utter_message(text="There are many events happening on campus. Please check the university calendar for more information.")

        return []

class ActionOpeningHours(Action):
    def name(self):
        return "action_opening_hours"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        # Your logic to fetch the opening hours and send it as a response to the user
        # ...
        latest_message = tracker.latest_message.get('text')
        
        dispatcher.utter_message(text="The opening hours of different services at the university vary. Please check with the specific service or department for their opening hours.")

        return []
