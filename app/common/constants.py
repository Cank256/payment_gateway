# Constants for the gateway

# HTTP status codes for API responses.
class STATUS_CODES:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    BAD_REQUEST = 400
    NOT_FOUND = 404
    UNAUTHORIZED = 401
    UNPROCESSABLE_ENTITY = 422
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503
    HTTP_GATEWAY_TIMEOUT = 504


# Log levels for logging purposes.
class LOG_LEVELS:
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'


# Common error messages for API responses.
class ERROR_MESSAGES:
    NON_UNIQUE_TRANSACTION = 'Please provide a unique py_ref.'
    MISSING_API_REF = 'Missing api reference (py_ref).'
    MISSING_PROVIDER_HEADER = 'Missing provider header.'
    UNKNOWN_SERVICE_PROVIDER = 'Unknown service provider.'
    UNAUTHORIZED_ACCESS = 'Unauthorized API access.'
    RESPONSE_TIMEOUT = 'Timeout response took so long.'
    ROUTE_NOT_FOUND = 'Route not found.'
    UNKNOWN_CONTENT_TYPE = 'Unrecognized Request Content Type',


# Status codes for SMS delivery statuses.
class SMS_CODES:
    DELIVERED= 1
    SUBMITTED= 4
    QUEUED= 8


# Transaction types for categorizing payment transactions.
class TRANS_TYPES:
    COLLECTION= 'collection'
    PAYOUT= 'payout'
    PURCHASE= 'purchase'
    VALIDATION= 'validation'


# Statuses for categorizing the state of payment transactions.
class TRANS_STATUS:
    CANCELLED= 'CANCELLED'
    COMPLETED= 'COMPLETED'
    FAILED= 'FAILED'
    PENDING= 'PENDING'
    LOGGED= 'LOGGED'
    SUCCESSFUL= 'SUCCESS'

