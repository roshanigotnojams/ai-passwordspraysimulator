def detect_password_spray(logs):
    """
    Analyze synthetic authentication events.

    A password-spray pattern is indicated when:
    - Multiple users are targeted
    - Multiple failed attempts occur
    - The activity is distributed across users
    """

    if not logs:
        return {
            "detected": False,
            "confidence": 0,
            "message": "No activity detected."
        }

    failed_logs = [
        log for log in logs
        if log["result"] == "FAILED"
    ]

    unique_users = len(
        set(log["username"] for log in failed_logs)
    )

    unique_passwords = len(
        set(log.get("password", "") for log in failed_logs)
    )

    failed_attempts = len(failed_logs)

    if (
        unique_users >= 3
        and unique_passwords >= 2
        and failed_attempts >= 5
    ):

        return {
            "detected": True,
            "confidence": 95,
            "message": "PASSWORD SPRAY DETECTED"
        }

    return {
        "detected": False,
        "confidence": 20,
        "message": "No password-spray pattern detected."
    }