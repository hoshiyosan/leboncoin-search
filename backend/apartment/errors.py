class ApartmentError:
    """
    Most generic type of error related to this application.
    """


class SearchError(ApartmentError):
    """
    Error raised in case of failure when searching new apartments.
    """


class AuthorizationError(SearchError):
    """
    Raise when content provider refused to return content due to wrong authorizations.
    """
