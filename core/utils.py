
class FullPartialSerializerMixin(object):
    """
    Overrides get_serializer_class to choose the full serializer
    for GET/POST requests and the partial serializer for PATCH requests.

    Set full_serializer_class and partial_serializer_class attributes on a
    viewset. 
    """

    full_serializer_class = None
    partial_serializer_class = None

    def get_serializer_class(self):        
        if self.partial is True:
            return self.get_partial_serializer_class()
        return self.get_full_serializer_class()

    def get_full_serializer_class(self):
        assert self.full_serializer_class is not None, (
            "'%s' should either include a `full_serializer_class` attribute,"
            "or override the `get_full_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.full_serializer_class

    def get_partial_serializer_class(self):
        assert self.partial_serializer_class is not None, (
            "'%s' should either include a `write_serializer_class` attribute,"
            "or override the `partial_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.partial_serializer_class
