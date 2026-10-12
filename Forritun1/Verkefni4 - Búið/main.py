aldur = int(input("Hvað verður þú gamall/gömul á þessu ári? "))
if aldur < 12:
    print ("Þú ert barn")
elif aldur > 12 and aldur < 20:
    print ("Þú ert unglingur")
else:
    print ("Þú ert fullorðin")
print ("Þú ert fædd(ur) árið", 2026-aldur,)