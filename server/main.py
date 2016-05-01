from person import Person


def group_center(group: set) -> tuple:
    center = [0, 0]
    for i in group:
        center[0] += i.coordinates[0]
        center[1] += i.coordinates[1]
    center[0] /= len(group)
    center[1] /= len(group)
    return tuple(center)

test = [Person("bob", 123),
        Person("Alice", 234),
        Person("Smith", 1632),
        Person("John", 1765),
        Person("Zangeef", 697),
        Person("Zanleef", 697)]
test[0].coordinates = (39.192511, -96.581802)
test[1].coordinates = (39.192511, -96.58180)
test[2].coordinates = (39.19251, -96.581802)
test[3].coordinates = (39.192511, -96.581302)
test[4].coordinates = (38.122511, -96.581802)
test[5].coordinates = (38.122511, -96.571802)
group = test
lost_people = set()

for i in group:
    i_am_lost = True
    for j in (set(group) - {i}):
        if i @ group_center(set(group) - {j}) < 100:
            i_am_lost = False
            if i.name == "Zangeef":
                print("Distance = {}".format(i @ group_center(set(group) - {i})))
                print("Person" + str(i))
    if i_am_lost:
        lost_people.add(i)
for i in lost_people:
    print(i)

