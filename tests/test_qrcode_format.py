from promptpay import qrcode


class TestFormat:
    def test_normal(self):
        assert qrcode.format("00", "01") == "000201"
        assert qrcode.format("00", "950") == "0003950"
        assert qrcode.format("05", "420") == "0503420"
        assert qrcode.format("07", "01") == "070201"
        assert qrcode.format("123", "456") == "12303456"
        assert qrcode.format("0987", "91823") == "09870591823"
        assert qrcode.format("494", "98973") == "4940598973"
        assert qrcode.format("09744", "080") == "0974403080"
        assert qrcode.format("00981", "000") == "0098103000"
