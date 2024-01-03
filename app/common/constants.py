# app/common/constants.py

# Constants for the gateway

# STATUS_CODES
# Defines standard HTTP status codes used in API responses.
# These codes indicate the result of the API request, such as success or error.
class STATUS_CODES:
    OK = 200  # Successful request.
    CREATED = 201  # Resource created successfully.
    ACCEPTED = 202  # Request accepted for processing.
    BAD_REQUEST = 400  # Invalid request syntax or bad query.
    NOT_FOUND = 404  # Requested resource not found.
    UNAUTHORIZED = 401  # Authentication is required and has failed or not yet been provided.
    METHOD_NOT_ALLOWED = 405  # HTTP method used is not supported for this route.
    UNPROCESSABLE_ENTITY = 422  # Request well-formed but unable to process due to semantic errors.
    INTERNAL_SERVER_ERROR = 500  # Generic server error.
    SERVICE_UNAVAILABLE = 503  # Service is currently unavailable.
    HTTP_GATEWAY_TIMEOUT = 504  # Gateway did not receive a response in time.

# LOG_LEVELS
# Defines log levels for categorizing the severity or importance of log messages.
class LOG_LEVELS:
    DEBUG = 'DEBUG'  # Detailed information, typically of interest only when diagnosing problems.
    INFO = 'INFO'  # Confirmation that things are working as expected.
    WARNING = 'WARNING'  # An indication that something unexpected happened.
    ERROR = 'ERROR'  # Due to a more serious problem, the software has not been able to perform some function.
    CRITICAL = 'CRITICAL'  # A serious error, indicating that the program itself may be unable to continue running.

# ERROR_MESSAGES
# Provides common error messages that can be used in API responses.
# These messages are standardized for consistency in API error handling.
class ERROR_MESSAGES:
    NON_UNIQUE_TRANSACTION = 'Please provide a unique py_ref.'
    MISSING_API_REF = 'Missing api reference (py_ref).'
    MISSING_PROVIDER_HEADER = 'Missing provider header.'
    UNKNOWN_SERVICE_PROVIDER = 'Unknown service provider.'
    UNAUTHORIZED_ACCESS = 'Unauthorized API access.'
    RESPONSE_TIMEOUT = 'Timeout response took so long.'
    ROUTE_NOT_FOUND = 'Route not found.'
    UNKNOWN_CONTENT_TYPE = 'Unrecognized Request Content Type',

# TRANS_TYPES
# Transaction types for categorizing different types of payment transactions.
# Useful for distinguishing the nature of each transaction.
class TRANS_TYPES:
    COLLECTION = 'collection'  # Collection transaction type.
    PAYOUT = 'payout'  # Payout transaction type.
    PURCHASE = 'purchase'  # Purchase transaction type.
    VALIDATION = 'validation'  # Validation transaction type.

# TRANS_STATUS
# Statuses for categorizing the state of payment transactions.
# Each status represents a different stage in the transaction lifecycle.
class TRANS_STATUS:
    CANCELLED = 'CANCELLED'  # Transaction has been cancelled.
    COMPLETED = 'COMPLETED'  # Transaction has been completed successfully.
    FAILED = 'FAILED'  # Transaction has failed.
    PENDING = 'PENDING'  # Transaction is pending and not yet finalized.
    LOGGED = 'LOGGED'  # Transaction has been logged.
    SUCCESSFUL = 'SUCCESS'  # Transaction has been successful.
