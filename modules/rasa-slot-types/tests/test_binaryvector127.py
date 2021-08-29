from RasaSlotTypes import Binary127Bit3

v = Binary127Bit3('test_slot')
v.value = 7

print("value: %s" % v.value)
print("as_feature(): %s" % v.as_feature())
