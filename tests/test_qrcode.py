from promptpay import qrcode


def test_qrcode():
    assert qrcode.generate_payload(3) == "eee"
