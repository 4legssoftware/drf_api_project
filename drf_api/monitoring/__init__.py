class Health(object):
    def __init__(self, **kwargs):
        for field in 'status':
            setattr(self, field, kwargs.get(field, None))
