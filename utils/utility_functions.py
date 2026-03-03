def update_keys(data, **kwargs):
    for key in kwargs:
        data[key] = kwargs[key]
    return data