class CatalogError(Exception):
    pass
class InvalidBookError(CatalogError):
    pass
class DuplicateIdError(CatalogError):
    pass
class BookNotFounderError(CatalogError):
    pass
class UnsupportedVersionFileError(CatalogError):
    pass
class CorruptedFileError(CatalogError):
    pass
