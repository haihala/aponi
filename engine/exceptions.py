class InvalidAssetTypeException(Exception):
    """
    For when the cache handler tries to load something but the type presented doesn't exist.
    """
    pass

class AssetNotFoundException(Exception):
    """
    For when the cache handler tries to load something but an asset with the specified name doesn't exist.
    """
    pass