from person import Person
test = [Person("bob", 123),
        Person("Alice", 234),
        Person("Smith", 1632),
        Person("John", 1765),
        Person("Zangeef", 697)]
test[0].coordinates = (39.192511, -96.581802)
test[1].coordinates = (39.192511, -96.58180)
test[2].coordinates = (39.19251, -96.581802)
test[3].coordinates = (39.192511, -96.581302)
test[4].coordinates = (39.122511, -96.581802)
group = {}
for i in test:
    group[i.phone_number] = i
lost_people = set(group.values())
for i in group.values():
    for j in group.values():
        if i @ j > 100:
            lost_people &= {i, j}
for i in lost_people:
    print(i)