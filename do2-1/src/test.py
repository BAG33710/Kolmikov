text = "Билирубин прямой - 3.4\nАЛТ - 0.52\nАСТ - 0.43\nСахар крови - 4.1\nХолестерин - 5.2\n"
t = text.lower()
num = t[t.find("алт")+6: t.find("алт") + 10]
print(f' ALT - {num}')
print(type(num))