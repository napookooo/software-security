"""Student task: complete the two bounded injection defenses. Sandbox only."""

import ipaddress
import re

def authenticate(connection, username: str, password: str):
    return connection.execute(
        "SELECT id, username FROM users WHERE username = ? AND password = ?",
        (username, password),
    ).fetchone()


_IPV4_SHAPE = re.compile(r"[0-9]{1,3}(?:\.[0-9]{1,3}){3}", re.ASCII)
def ping_argv(host: str) -> list[str]:
    """Return ['ping', '-c', '1', host] for a single IPv4 address."""
    if not isinstance(host, str) or not _IPV4_SHAPE.fullmatch(host):
        raise ValueError("host must be a single dotted-decimal IPv4 address")
    try:
        ipaddress.IPv4Address(host)
    except ValueError as exc:
        raise ValueError("host must be a valid IPv4 address") from exc
    return ["ping", "-c", "1", host]
