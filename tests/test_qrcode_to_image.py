from promptpay import qrcode


class TestToImage:
    def test_normal(self):
        payload = qrcode.generate_payload("0841234567")
        img = qrcode.to_image(payload)
        assert type(img).__name__ == "PilImage"
