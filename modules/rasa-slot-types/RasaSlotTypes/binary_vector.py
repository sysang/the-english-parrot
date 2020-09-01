import logging
from rasa.core.slots import Slot

logger = logging.getLogger(__name__)

class OnehotVector99(Slot):

    def feature_dimensionality(self):
        return 10

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

class BinaryVector7(Slot):

    def feature_dimensionality(self):
        dim = self._encoding_bit()
        max_encoded = self._get_max_encoded_value(dim)

        return dim*max_encoded

    def _encoding_bit(self):
        return 3

    def _get_max_encoded_value(self, dim):
        array_of_binary_digits = [1]*dim
        digit_str = ''.join([str(d) for d in array_of_binary_digits])

        return int(digit_str, 2)

    def _convert_decimal_to_binary_digits(self, val, dim):
        array_of_binary_digits = [int(d) for d in format(val, 'b')]
        extended_length = dim - len(array_of_binary_digits)

        return [0]*extended_length + array_of_binary_digits

    def _generate_vector(self, val, dim):
        max_encoded = self._get_max_encoded_value(dim)
        r = []
        for num in range(max_encoded + 1):
            encoded = self._convert_decimal_to_binary_digits(num, dim)
            if num <= val:
                r = r + encoded
            else:
                r = r + [0]*dim

        return r

    def as_feature(self):
        dim = self._encoding_bit()
        r = [0.0] * dim

        if not self.value:
            return r

        selfval = int(self.value)
        max_encoded = self._get_max_encoded_value(dim)

        if selfval < 0 or selfval > max_encoded:
            raise Exception(f"Invalid value: {selfval}, max encoded value: {max_encoded}")

        r = self._generate_vector(selfval, dim)

        #logger.debug(f"Encoded vector for slot value {selfval}: {r}")

        return r

class BinaryVector127(BinaryVector7):

    def _encoding_bit(self):
        return 7
