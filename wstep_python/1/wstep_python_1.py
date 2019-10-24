##########################1############################
 string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sit amet mi viverra, viverra diam nec, " \
            "Praesent tempor urna ligula, blandit scelerisque risus vulputate id. Nam in lorem felis. Vestibulum sit amet urna blandit, " \
            "ultrices ligula sit amet, dignissim libero. Curabitur pulvinar nunc sit amet pretium facilisis. Orci varius natoque penatibus et magnis  " \
            "dis parturient montes, nascetur ridiculus mus. Aliquam nec lectus placerat, mattis neque at, pe" \
            "llentesque lectus. Aliquam efficitur sapien elit, et blandit erat iaculis ut. " \
            "Sit amet, dignissim libero."
            
##########################2############################
n = list("rafal")
s = list("sarbiewski")
n_number = s_number = 0

for i in string:
    if i == n[2]:
        n_number += 1
    if i == s[3]:
        s_number += 1

print(f"W tekście jest {n_number} liter {n[2]}... oraz {s_number} liter {s[3]}...")

##########################4############################
print(dir("rafal"))
help("rafal".split())

##########################5############################
name = "Rafał Sarbiewski"
print(name[::-1])

##########################6############################
list = [i for i in range(1, 11)]
list2 = [i for i in range(1, 11) if i > 5]
list = [i for i in range(1, 11) if i <= 5]
print(list, list2)

##########################7############################
list3 = [0, *list, *list2]
print(list3)
print(sorted(list3, reverse=True))

##########################8############################
krotka = [(111111, "Rafał Wita"), (222222, "Rafał Kosi"), (333333, "Rafał Wspina")]
print(krotka)

##########################9############################
slownik = dict(krotka)

##########################10############################
telefony = [123456789, 485405321, 857643213, 123456789, 485405321, 654321321, 123456789]
numbers = set(telefony)
print(telefony)

##########################11############################
l = []
for i in range(1, 11):
    l.append(i)
print(l)

##########################12############################
l2 = []
for i in reversed(range(20, 101, 5)):
    print(i)
    l2.append(i)
print(l2)

##########################13############################
slowniki = [{"ID": 1, "Imie": "Rafal"}, {"Number": 5, "Nazwisko": "Sarbiewski"}, {"Liczba": 1, 2: "dodaj"}]
napis = ""
for i in list_dicts:
    for j in x.keys():
        napis += str(i[j]) + " "
print(napis)