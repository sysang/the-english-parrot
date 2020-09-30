from RasaSlotTypes import BinaryVector127

v = BinaryVector127('test_slot')
v.value = 126

print("feature_dimensionality(): %s", v.feature_dimensionality())
print("as_feature(): %s", v.as_feature())
