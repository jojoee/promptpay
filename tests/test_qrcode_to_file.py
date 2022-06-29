from promptpay import qrcode
import os.path


class TestToFile:
    def test_normal(self):
        payload = qrcode.generate_payload("0841234567")
        filepath = "./exported-qrcode-file.png"
        qrcode.to_file(payload, filepath)
        assert os.path.exists(filepath)
