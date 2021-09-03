import logging
from rasa.shared.core.slots import Slot

class Influential(Slot):

    def as_feature(self):
        dim = self.feature_dimensionality()

        if not self.value:
            return [0.0] * dim

        return [1.0] * dim


class Influentialx10(Influential):

    def feature_dimensionality(self):
        return 10


class Influentialx4(Influential):

    def feature_dimensionality(self):
        return 4


class Influentialx8(Influential):

    def feature_dimensionality(self):
        return 8


class Influentialx16(Influential):

    def feature_dimensionality(self):
        return 16


class Influentialx32(Influential):

    def feature_dimensionality(self):
        return 32
