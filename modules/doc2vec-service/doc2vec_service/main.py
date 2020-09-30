from doc2vec_service import load_model
from doc2vec_service import query_semantic_distance

EPOCHS = 200

model = load_model()


def infer_if_words_similar(query, target, theme):
    return query_semantic_distance(model, query, target, theme, EPOCHS)
