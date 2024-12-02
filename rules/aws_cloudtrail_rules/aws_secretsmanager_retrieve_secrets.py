from panther_aws_helpers import aws_rule_context


def rule(event):
    if event.get("eventName") == "GetSecretValue" and event.get("errorCode") == "AccessDenied":
        return True
    return False


def dedup(event):
    return event.deep_get("additionalEventData", "UserName", default="<NO_USER>")


def title(event):
    user = event.deep_get("additionalEventData", "UserName", default="<NO_USER>")
    return f"[{user}] attempted to retrieve secrets from AWS Secrets Manager"


def alert_context(event):
    return aws_rule_context(event)
