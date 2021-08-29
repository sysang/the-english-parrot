import logging
from rasa.shared.core.slots import Slot

logger = logging.getLogger(__name__)


class OnehotVector99(Slot):

    def feature_dimensionality(self):
        return 100

    def as_feature(self):
        dim = self.feature_dimensionality()
        r = [0.0] * dim

        if not self.value:
            return r

        selfval = int(self.value)

        if selfval < 0 or selfval >= dim:
            raise Exception(f"Invalid index for one-hot vector; vector dimension: {dim}, index: {selfval} ")

        r[selfval] = 1.0

        return r


class Binary127Bit3(Slot):
    encoding_bit_quantity = 3

    def feature_dimensionality(self):
        return 21

    def _get_max_encoded_value(self):
        dim = self.feature_dimensionality()
        if dim % self.encoding_bit_quantity:
            raise Exception(f"Inappropriate feature dimensionality size: {dim}")

        binary_size = int(dim / self.encoding_bit_quantity)
        max_binary_value = [1] * binary_size

        digit_str = ''.join([str(d) for d in max_binary_value])

        return int(digit_str, 2)

    def _generate_vector(self, selfval):
        dim = self.feature_dimensionality()
        r = [0.0] * dim

        binary_number_str = "{0:b}".format(selfval)

        order = 0
        for idx, val in enumerate(reversed(binary_number_str)):
            for i in range(self.encoding_bit_quantity):
                r[order] = float(val)
                order += 1

        return list(reversed(r))

    def as_feature(self):
        dim = self.feature_dimensionality()
        r = [0.0] * dim

        if not self.value:
            return r

        selfval = int(self.value)
        max_encoded = self._get_max_encoded_value()

        if selfval < 0 or selfval > max_encoded:
            raise Exception(f"Invalid value: {selfval}, max encoded value: {max_encoded}")

        r = self._generate_vector(selfval)

        return r
