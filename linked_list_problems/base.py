class BaseLinkedList:
    """Declares base LinkedList class with mandatory methods."""
    def insert(self, *args, **kwargs):
        raise NotImplementedError('Insert method not defined in extended class.')

    def update(self, *args, **kwargs):
        raise NotImplementedError('Update method not defined in extended class.')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('Delete method not defined in extended class.')
