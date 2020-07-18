from promptpay import qrcode
import os.path


class TestSanitizeTarget:
    def test_normal(self):
        # phone
        assert qrcode.sanitize_target(target="0801234567") == "0801234567"
        # national id
        assert qrcode.sanitize_target(target="1111111111111") == "1111111111111"
        # tax id
        assert qrcode.sanitize_target(target="0123456789012") == "0123456789012"
        # ewallet
        assert qrcode.sanitize_target(target="012345678901234") == "012345678901234"

    def test_with_dash(self):
        # phone
        assert qrcode.sanitize_target(target="080-123-4567") == "0801234567"
        # national id
        assert qrcode.sanitize_target(target="1-1111-11111-11-1") == "1111111111111"

    def test_with_international_format(self):
        assert qrcode.sanitize_target(target="+66-89-123-4567") == "66891234567"


class TestFormatTarget:
    def test_normal(self):
        # phone
        assert qrcode.format_target("0899999999") == "0066899999999"

        # national id
        assert qrcode.format_target("1234567890123") == "1234567890123"

    def test_with_dash(self):
        assert qrcode.format_target("089-999-9999") == "0066899999999"

    def test_with_zero_leading(self):
        # tax id which is start with 0
        assert qrcode.format_target("0123456789012") == "0123456789012"


class TestFormatAmount:
    def test_normal(self):
        assert qrcode.format_amount(10.23) == "10.23"

    def test_number_without_decimal(self):
        assert qrcode.format_amount(10) == "10.00"

    def test_number_with_more_than_two_decimal_number(self):
        assert qrcode.format_amount(1337.1337) == "1337.13"
        assert qrcode.format_amount(1337.1387) == "1337.14"


class TestChecksum:
    def test_normal(self):
        assert qrcode.checksum("00020101021129370016A000000677010111011300660000000005802TH53037646304") == "8956"
        assert qrcode.checksum("00020101021129370016A000000677010111011300668999999995802TH53037646304") == "FE29"


class TestFormat:
    def test_normal(self):
        assert qrcode.format("00", "01") == "000201"
        assert qrcode.format("05", "420") == "0503420"


class TestGeneratePayload:
    def test_local_phone_number(self):
        assert qrcode.generate_payload(
            id="0801234567") == "00020101021129370016A000000677010111011300668012345675802TH530376463046197"
        assert qrcode.generate_payload(
            id="0899999999") == "00020101021129370016A000000677010111011300668999999995802TH53037646304FE29"
        assert qrcode.generate_payload(
            id="0891234567") == "00020101021129370016A000000677010111011300668912345675802TH5303764630429C1"
        assert qrcode.generate_payload(
            id="0000000000") == "00020101021129370016A000000677010111011300660000000005802TH530376463048956"

    def test_local_phone_number_with_dash(self):
        assert qrcode.generate_payload(
            id="080-123-4567") == "00020101021129370016A000000677010111011300668012345675802TH530376463046197"

    def test_local_phone_number_with_international_format(self):
        assert qrcode.generate_payload(
            id="+66-89-123-4567") == "00020101021129370016A000000677010111011300668912345675802TH5303764630429C1"

    def test_national_id_number(self):
        assert qrcode.generate_payload(
            id="1111111111111") == "00020101021129370016A000000677010111021311111111111115802TH530376463047B5A"
        assert qrcode.generate_payload(
            id="1234567890123") == "00020101021129370016A000000677010111021312345678901235802TH53037646304EC40"

    def test_national_id_number_with_dash(self):
        assert qrcode.generate_payload(
            id="1-1111-11111-11-1") == "00020101021129370016A000000677010111021311111111111115802TH530376463047B5A"

    def test_tax_id(self):
        assert qrcode.generate_payload(
            id="0123456789012") == "00020101021129370016A000000677010111021301234567890125802TH530376463040CBD"

        def test_ewallet_id(self):
            # eWallet ID, KPlus ID
            assert qrcode.generate_payload(
                id="012345678901234") == "00020101021129390016A00000067701011103150123456789012345802TH530376463049781"
            assert qrcode.generate_payload(
                id="004999000288505") == "00020101021129390016A00000067701011103150049990002885055802TH530376463041521"

            # KPlus shop ID
            assert qrcode.generate_payload(
                id="004000006579718") == "00020101021129390016A00000067701011103150040000065797185802TH53037646304FBB5"

    def test_amount_setting(self):
        # phone number
        assert qrcode.generate_payload(
            id="000-000-0000",
            amount=4.22) == "00020101021229370016A000000677010111011300660000000005802TH530376454044.226304E469"
        assert qrcode.generate_payload(
            id="089-123-4567",
            amount=13371337.75) == "00020101021229370016A000000677010111011300668912345675802TH5303764541113371337.756304B7D7"

        # national id
        assert qrcode.generate_payload(
            id="1234567890123",
            amount=420) == "00020101021229370016A000000677010111021312345678901235802TH53037645406420.006304BF7B"

        # eWallet ID, KPlus ID
        assert qrcode.generate_payload(
            id="004999000288505",
            amount=100.25) == "00020101021229390016A00000067701011103150049990002885055802TH53037645406100.256304369A"

        # KPlus shop ID
        assert qrcode.generate_payload(
            id="004000006579718",
            amount=200.50) == "00020101021229390016A00000067701011103150040000065797185802TH53037645406200.5063048A37"


class TestToImage:
    def test_normal(self):
        payload = qrcode.generate_payload("0841234567")
        img = qrcode.to_image(payload)
        assert type(img).__name__ == "PilImage"


class TestToFile:
    def test_normal(self):
        payload = qrcode.generate_payload("0841234567")
        filepath = "./exported-qrcode-file.png"
        qrcode.to_file(payload, filepath)
        assert os.path.exists(filepath)
