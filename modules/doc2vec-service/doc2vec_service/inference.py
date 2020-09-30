from numpy import dot
from numpy.linalg import norm


def project_vector_to(query, target):
    return target * dot(query, target) / dot(target, target)


def query_semantic_distance(model, query, target, theme, epochs=5):
    """
    Compute the distance between word vectors via their projection
    onto theme vector. We can use the distance as a inference way to
    query semantic similarity

    Parameters:
        query (ndarray): vector represents embedded word
        target (ndarray): vector represents embedded word
        theme (ndarray): vector represents embedded word, respected to the
            meaning under comparison
        epochs (int): epochs for Doc2vec.infer_vector method

    Returns:
        distance (float)
    """

    query_vector = model.infer_vector(query.split(' '), epochs=epochs)
    target_vector = model.infer_vector(target.split(' '), epochs=epochs)
    theme_vector = model.infer_vector([theme], epochs=epochs)
    query_projection_on_theme = project_vector_to(query_vector, theme_vector)
    target_projection_on_theme = project_vector_to(target_vector, theme_vector)

    distance_vector = query_projection_on_theme - target_projection_on_theme

    return norm(distance_vector) / norm(theme_vector)
