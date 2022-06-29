from promptpay import qrcode


class TestFormatAmount:
    def test_normal(self):
        assert qrcode.format_amount(10.23) == "10.23"
        assert qrcode.format_amount(301928.50) == "301928.50"
        assert qrcode.format_amount(1820494.25) == "1820494.25"

    def test_number_without_decimal(self):
        assert qrcode.format_amount(10) == "10.00"
        assert qrcode.format_amount(300) == "300.00"
        assert qrcode.format_amount(461239) == "461239.00"

    def test_number_with_more_than_two_decimal_number_round_up(self):
        assert qrcode.format_amount(1337.1387) == "1337.14"
        assert qrcode.format_amount(8884994.996) == "8884995.00"

    def test_number_with_more_than_two_decimal_number_round_down(self):
        assert qrcode.format_amount(1337.1337) == "1337.13"
        assert qrcode.format_amount(1293123.254) == "1293123.25"
        assert qrcode.format_amount(3000.255) == "3000.26"

    def test_number_with_more_than_two_decimal_number_and_floating_point_issue(self):
        assert qrcode.format_amount(8884994.995) == "8884994.99"
