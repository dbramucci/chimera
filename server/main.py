from flask import Flask, request
from person import Person
from test import make_test_case
from twilio.rest import TwilioRestClient

account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)

app = Flask(__name__)

GROUP_RADIUS = 100
group = {}

def send_lost_message(phone_number, lost_person_name):
    message = client.messages.create(to=0, from_=0,
                                     body="{} is being left behind!".format(lost_person_name))

def group_center(group: set) -> tuple:
    center = [0, 0]
    for i in group:
        center[0] += i.coordinates[0]
        center[1] += i.coordinates[1]
    center[0] /= len(group)
    center[1] /= len(group)
    return tuple(center)


def find_lost_people(list_of_group_members: list) -> set:
    lost_people = set()
    for person_lost in list_of_group_members:
        i_am_lost = True
        for partner in (set(list_of_group_members) - {person_lost}):
            if person_lost @ group_center(set(list_of_group_members) - {partner}
                                          ) < GROUP_RADIUS:
                i_am_lost = False
        if i_am_lost:
            lost_people.add(person_lost)
    return lost_people


@app.route("/", methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        try:
            post_data = request.args
            name = request.args['name']
            phone_num = int(request.args['num'])
            lat = float(post_data['lat'])
            long = float(post_data['long'])
            print(name, phone_num, lat, long)
            group[phone_num] = Person(name, phone_num)
            group[phone_num].coordinates = lat, long
        except (ValueError, RuntimeError):
            return '404'
        main()
        return '200'


def main():
    # group = make_test_case()
    lost_people = find_lost_people(group.values())
    for i in lost_people:
        if len(group) > 1:
            print(i)
            send_lost_message(i.phone_number, i.name)


if __name__ == "__main__":
    app.run(debug=True)
