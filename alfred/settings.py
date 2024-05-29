import os

# CACHE SETTINGS
ALFRED_REDIS_HOST = os.environ.get("ALFRED_REDIS_HOST", "")

# SENTRY SETTINGS
SENTRY_DSN = os.environ.get("SENTRY_DSN", "")

# AWS SETTINGS
AWS_ACCESS_KEY_ID = os.environ.get("ALFRED_AWS_ACCESS_KEY_ID") or os.environ.get(
    "AWS_ACCESS_KEY_ID"
)
AWS_SECRET_ACCESS_KEY = os.environ.get(
    "ALFRED_AWS_SECRET_ACCESS_KEY"
) or os.environ.get("AWS_SECRET_ACCESS_KEY")
SQS_QUEUE_URL = os.environ.get("SQS_QUEUE_URL", "")

DYNAMODB_HOST = os.environ.get("DYNAMODB_HOST")
DYNAMODB_PREFIX = os.environ.get("DYNAMODB_PREFIX")

SQS_TASK_EAGER = os.environ.get("SQS_TASK_EAGER", False)
