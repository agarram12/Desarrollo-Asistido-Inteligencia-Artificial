temperaturas = [18, 22, 19, 25, 30, 17, 28, 24]
# 1
mayores = []
for temperatura in temperaturas:
    if temperatura > 20:
        mayores.append(temperatura)
# 2
tmp_dict = {}
for i in range(len(temperatura)):
    tmp_dict[i] = temperatura [i]
print(tmp_dict)
tmp_3 = tmp[:3]