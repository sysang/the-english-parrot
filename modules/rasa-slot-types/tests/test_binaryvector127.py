from RasaSlotTypes import BinaryVector127

import logging

logger = logging.getLogger(__name__)

v = BinaryVector127('test_slot')
v.value = 126

logger.warning("feature_dimensionality(): %s", v.feature_dimensionality())
logger.warning("as_feature(): %s", v.as_feature())
