from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError("tipo inválido para key")):
        encrypt_message("testmesssage", "1")

    with pytest.raises(TypeError("tipo inválido para message")):
        encrypt_message(55, 1)

    key_out_of_range_return = encrypt_message("test message", 22)
    assert key_out_of_range_return == "egassem tset"

    odd_key_return = encrypt_message("test message", 3)
    assert odd_key_return == "set_egassem t"

    even_key_return = encrypt_message("test message", 4)
    assert even_key_return == "egassem_tset"
