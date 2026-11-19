import pytest

from protocol.handshake import (
    nonce_fresh,
    sequence_valid,
    session_alive,
    transition_allowed,
    credential_isolated,
    build_handshake,
)


def test_replay_nonce_rejected():
    seen = {}
    nonce_fresh("n1", seen)
    assert nonce_fresh("n1", seen) is False


def test_fresh_nonce_allowed():
    assert nonce_fresh("n1", {}) is True


def test_sequence_rewind_rejected():
    assert sequence_valid(2, 5) is False


def test_sequence_increment_ok():
    assert sequence_valid(6, 5) is True


def test_expired_session_rejected():
    assert session_alive(1000, 2000) is False


def test_active_session_alive():
    assert session_alive(9999999999, 2000) is True


def test_skip_auth_to_business_rejected():
    assert transition_allowed("init", "enter_business") is False


def test_legal_transition_allowed():
    assert transition_allowed("init", "authenticate") is True


def test_cross_layer_credential_rejected():
    assert credential_isolated({"layer": "web"}, "db") is False


def test_same_layer_credential_ok():
    assert credential_isolated({"layer": "db"}, "db") is True


def test_handshake_binds_nonces():
    hs = build_handshake("c1", "s1")
    assert hs["client_nonce"] == "c1" and hs["server_nonce"] == "s1"


def test_missing_nonce_rejected():
    import pytest
    with pytest.raises(ValueError):
        build_handshake("", "s1")


def test_repeated_nonce_pair_rejected():
    import pytest
    with pytest.raises(ValueError):
        build_handshake("c1", "c1")


def test_state_reset_after_logout():
    assert transition_allowed("authenticated", "logout") is True


def test_timeout_event_rejects():
    assert session_alive(0, 2000) is False
