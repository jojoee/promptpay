from promptpay import qrcode


class TestFormatTarget:
    def test_phone_format(self):
        assert qrcode.format_target("0899999999") == "0066899999999"
        assert qrcode.format_target("0849488172") == "0066849488172"
        assert qrcode.format_target("0819837638") == "0066819837638"
        assert qrcode.format_target("0871255555") == "0066871255555"

    def test_dashed_phone_format(self):
        assert qrcode.format_target("089-999-9999") == "0066899999999"
        assert qrcode.format_target("084-948-8172") == "0066849488172"
        assert qrcode.format_target("081-983-7638") == "0066819837638"
        assert qrcode.format_target("087-125-5555") == "0066871255555"

    def test_national_id_format(self):
        assert qrcode.format_target("1234567890123") == "1234567890123"
        assert qrcode.format_target("8512819188690") == "8512819188690"
        assert qrcode.format_target("4912419510270") == "4912419510270"
        assert qrcode.format_target("0023637209811") == "0023637209811"

    def test_zero_leading_national_id_format(self):
        # tax id which is start with 0
        assert qrcode.format_target("0123456789012") == "0123456789012"
        assert qrcode.format_target("0023637209811") == "0023637209811"

    def test_ewallet_format(self):
        assert qrcode.format_target("012345678901234") == "012345678901234"
        assert qrcode.format_target("004999000288505") == "004999000288505"
        assert qrcode.format_target("004000006579718") == "004000006579718"
