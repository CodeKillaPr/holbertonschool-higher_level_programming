import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be in a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        attendee = attendee.copy()
        missing_keys = [key for key in ['event_date', 'event_location', 'event_title'] if key not in attendee]
        for key in missing_keys:
            print(f"Warning: Replacing missing data '{key}' with 'N/A'.")
            attendee[key] = "N/A"
        try:
            invitation = template.format(**attendee)
        except KeyError as e:
            print(f"Warning: Unexpected missing data {e}")
            attendee[str(e)] = "N/A"
            invitation = template.format(**attendee)
        with open(f"output_{index}.txt", "w") as file:
            file.write(invitation)