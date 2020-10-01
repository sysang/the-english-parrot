from doc2vec_service import load_model
from doc2vec_service import query_semantic_distance

EPOCHS = 200
THRESOLD = 0.35

model = load_model()


def infer_if_words_similar(query, target, theme):
    distance = query_semantic_distance(model, query, target, theme, EPOCHS)
    return distance < THRESOLD


def infer_vector(doc_words):
    return model.infer_vector(doc_words, epochs=EPOCHS)
