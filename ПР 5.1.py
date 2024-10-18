ws = "Окно емае как дела ехать"
ct = 0
for word in ws.split(" "):
    if word.strip()[0] == 'е':
        ct +=1
print(ct)