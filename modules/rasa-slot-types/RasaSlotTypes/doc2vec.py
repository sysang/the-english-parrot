import os

from rasa.shared.core.slots import Slot
from gensim.models.doc2vec import Doc2Vec

import logging
logger = logging.getLogger(__name__)


class Model():
    __instance = None

    @staticmethod
    def getInstance():
        if Model.__instance is None:
            Model()
        return Model.__instance

    def __init__(self):

        if Model.__instance is not None:
            raise Exception("This class is a singleton! Use Model.getInstance() instead.")
        else:
            logger.info('Loading doc2vec model...')
            model_file = os.path.join(os.path.dirname(__file__), 'models/dmc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin')
            logger.info(model_file)
            self.model = Doc2Vec.load(model_file)
            logger.info('...completed loading doc2vec model.')

            self.caches = dict()

            Model.__instance = self

    def infer_sentence_vector(self, sentence):
        if sentence not in self.caches:
            tokens = sentence.split(' ')
            result = self.model.infer_vector(tokens)
            self.caches[sentence] = result.tolist()

        return self.caches.get(sentence)


class WordVector(Slot):
    def __init__(self, *args, **kwargs):
        super(WordVector, self).__init__(*args, **kwargs)
        self.model = Model.getInstance()

    def feature_dimensionality(self):
        return 15

    def as_feature(self):
        dim = self.feature_dimensionality()
        r = [0.0] * dim

        if not self.value:
            return r

        r = self.model.infer_sentence_vector(self.value)

        return r
