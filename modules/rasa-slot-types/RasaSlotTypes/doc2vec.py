import os

import numpy as np
from rasa.core.slots import Slot
from gensim.models.doc2vec import Doc2Vec
from gensim.models.callbacks import CallbackAny2Vec

import logging
logger = logging.getLogger(__name__)


logger.info('Loading doc2vec model...')
model_file = os.path.join(os.path.dirname(__file__), 'models/dmc_d10_n3_w2_mc5_s001_ech50_imdb.bin')
logger.info(model_file)
model = Doc2Vec.load(model_file)
logger.info('...completed loading doc2vec model.')

caches = dict()


def transform_to_vector(sentence):
    if sentence not in caches:
        tokens = sentence.split(' ')
        result = model.infer_vector(tokens)
        # norm = np.linalg.norm(result)
        # result = result / norm
        caches[sentence] = result.tolist()

    return caches.get(sentence)


class WordVector(Slot):

    def feature_dimensionality(self):
        return 10

    def as_feature(self):
        dim = self.feature_dimensionality()
        r = [0.0] * dim

        if not self.value:
            return r

        r = transform_to_vector(self.value)

        return r
