class DocumentTaskError(Exception):
    code = "DOCUMENT_TASK_ERROR"

    def __init__(self, message: str = ""):
        super().__init__(message or self.code)


class FileNotFoundErrorDT(DocumentTaskError):
    code = "FILE_NOT_FOUND"


class FileAmbiguousError(DocumentTaskError):
    code = "FILE_AMBIGUOUS"


class UnsupportedFormatError(DocumentTaskError):
    code = "UNSUPPORTED_FORMAT"


class PdfExtractionFailedError(DocumentTaskError):
    code = "PDF_EXTRACTION_FAILED"


class IndexFailedError(DocumentTaskError):
    code = "INDEX_FAILED"


class ReadFailedError(DocumentTaskError):
    code = "READ_FAILED"


class WriteFailedError(DocumentTaskError):
    code = "WRITE_FAILED"


class ValidationFailedError(DocumentTaskError):
    code = "VALIDATION_FAILED"


class StateCorruptedError(DocumentTaskError):
    code = "STATE_CORRUPTED"
