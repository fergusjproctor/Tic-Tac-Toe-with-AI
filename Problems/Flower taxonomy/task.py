iris = {}


def add_iris(id_n, species_, petal_length_, petal_width_, **kwargs):
    iris[id_n] = {'species': species_, 'petal_length': petal_length_, 'petal_width': petal_width_}
    iris[id_n].update(kwargs)
