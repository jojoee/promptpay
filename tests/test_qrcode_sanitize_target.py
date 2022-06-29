from promptpay import qrcode


class TestSanitizeTarget:
    def test_phone_format(self):
        assert qrcode.sanitize_target(target="0801234567") == "0801234567"
        assert qrcode.sanitize_target(target="0849488172") == "0849488172"
        assert qrcode.sanitize_target(target="0819837638") == "0819837638"
        assert qrcode.sanitize_target(target="0871255555") == "0871255555"

    def test_dashed_phone_format(self):
        assert qrcode.sanitize_target(target="080-123-4567") == "0801234567"
        assert qrcode.sanitize_target(target="084-948-8172") == "0849488172"
        assert qrcode.sanitize_target(target="081-983-7638") == "0819837638"
        assert qrcode.sanitize_target(target="087-125-5555") == "0871255555"

    def test_international_phone_format(self):
        assert qrcode.sanitize_target(target="+66-89-123-4567") == "66891234567"
        assert qrcode.sanitize_target(target="+66-84-948-8172") == "66849488172"
        assert qrcode.sanitize_target(target="+66-81-983-7638") == "66819837638"
        assert qrcode.sanitize_target(target="+66-87-125-5555") == "66871255555"

    def test_national_id_format(self):
        assert qrcode.sanitize_target(target="1111111111111") == "1111111111111"
        assert qrcode.sanitize_target(target="1234567890123") == "1234567890123"
        assert qrcode.sanitize_target(target="0123456789012") == "0123456789012"
        assert qrcode.sanitize_target(target="8512819188690") == "8512819188690"
        assert qrcode.sanitize_target(target="4912419510270") == "4912419510270"
        assert qrcode.sanitize_target(target="0023637209811") == "0023637209811"

    def test_dashed_national_id_format(self):
        assert qrcode.sanitize_target(target="1-1111-11111-11-1") == "1111111111111"
        assert qrcode.sanitize_target(target="1-2345-67890-12-3") == "1234567890123"
        assert qrcode.sanitize_target(target="0-1234-56789-01-2") == "0123456789012"
        assert qrcode.sanitize_target(target="8-5128-19188-69-0") == "8512819188690"
        assert qrcode.sanitize_target(target="4-9124-19510-27-0") == "4912419510270"
        assert qrcode.sanitize_target(target="0-0236-37209-81-1") == "0023637209811"

    def test_ewallet_format(self):
        assert qrcode.sanitize_target(target="012345678901234") == "012345678901234"
        assert qrcode.sanitize_target(target="004999000288505") == "004999000288505"
        assert qrcode.sanitize_target(target="004000006579718") == "004000006579718"
