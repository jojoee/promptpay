from promptpay import qrcode
import os.path


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


class TestChecksum:
    def test_normal(self):
        # phone
        assert qrcode.checksum("00020101021129370016A000000677010111011300660000000005802TH53037646304") == "8956"
        assert qrcode.checksum("00020101021129370016A000000677010111011300668012345675802TH53037646304") == "6197"
        assert qrcode.checksum("00020101021129370016A000000677010111011300668198376385802TH53037646304") == "F963"
        assert qrcode.checksum("00020101021129370016A000000677010111011300668494881725802TH53037646304") == "C907"
        assert qrcode.checksum("00020101021129370016A000000677010111011300668712555555802TH53037646304") == "82FE"
        assert qrcode.checksum("00020101021129370016A000000677010111011300668912345675802TH53037646304") == "29C1"
        assert qrcode.checksum("00020101021129370016A000000677010111011300668999999995802TH53037646304") == "FE29"

        # national id

        assert qrcode.checksum("00020101021129370016A000000677010111021311111111111115802TH53037646304") == "7B5A"
        assert qrcode.checksum("00020101021129370016A000000677010111021312345678901235802TH53037646304") == "EC40"
        assert qrcode.checksum("00020101021129370016A000000677010111021301234567890125802TH53037646304") == "0CBD"
        assert qrcode.checksum("00020101021129370016A000000677010111021385128191886905802TH53037646304") == "00F4"
        assert qrcode.checksum("00020101021129370016A000000677010111021349124195102705802TH53037646304") == "10C5"
        assert qrcode.checksum("00020101021129370016A000000677010111021300236372098115802TH53037646304") == "0C4C"


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


class TestGeneratePayload:
    def test_phone_format(self):
        assert qrcode.generate_payload(
            id="0000000000") == "00020101021129370016A000000677010111011300660000000005802TH530376463048956"
        assert qrcode.generate_payload(
            id="0801234567") == "00020101021129370016A000000677010111011300668012345675802TH530376463046197"
        assert qrcode.generate_payload(
            id="0819837638") == "00020101021129370016A000000677010111011300668198376385802TH53037646304F963"
        assert qrcode.generate_payload(
            id="0849488172") == "00020101021129370016A000000677010111011300668494881725802TH53037646304C907"
        assert qrcode.generate_payload(
            id="0871255555") == "00020101021129370016A000000677010111011300668712555555802TH5303764630482FE"
        assert qrcode.generate_payload(
            id="0891234567") == "00020101021129370016A000000677010111011300668912345675802TH5303764630429C1"
        assert qrcode.generate_payload(
            id="0899999999") == "00020101021129370016A000000677010111011300668999999995802TH53037646304FE29"

    def test_phone_format_with_amount(self):
        # no decimal points
        assert qrcode.generate_payload(
            id="0000000000",
            amount=100) == "00020101021229370016A000000677010111011300660000000005802TH53037645406100.0063043B7D"

        # 2 decimal points
        assert qrcode.generate_payload(
            id="0801234567",
            amount=456.25) == "00020101021229370016A000000677010111011300668012345675802TH53037645406456.256304483D"
        assert qrcode.generate_payload(
            id="0819837638",
            amount=5476521.50) == "00020101021229370016A000000677010111011300668198376385802TH530376454105476521.506304EA3B"
        assert qrcode.generate_payload(
            id="0849488172",
            amount=81545415.75) == "00020101021229370016A000000677010111011300668494881725802TH5303764541181545415.756304D28D"
        assert qrcode.generate_payload(
            id="0871255555",
            amount=4864688.23) == "00020101021229370016A000000677010111011300668712555555802TH530376454104864688.236304E369"

        # more than 2 decimal points
        assert qrcode.generate_payload(
            id="0891234567",
            amount=445465.654878) == "00020101021229370016A000000677010111011300668912345675802TH53037645409445465.656304CD64"
        assert qrcode.generate_payload(
            id="0899999999",
            amount=484848.4645) == "00020101021229370016A000000677010111011300668999999995802TH53037645409484848.466304209B"

    def test_dashed_phone_format(self):
        assert qrcode.generate_payload(
            id="000-000-0000") == "00020101021129370016A000000677010111011300660000000005802TH530376463048956"
        assert qrcode.generate_payload(
            id="080-123-4567") == "00020101021129370016A000000677010111011300668012345675802TH530376463046197"
        assert qrcode.generate_payload(
            id="081-983-7638") == "00020101021129370016A000000677010111011300668198376385802TH53037646304F963"
        assert qrcode.generate_payload(
            id="084-948-8172") == "00020101021129370016A000000677010111011300668494881725802TH53037646304C907"
        assert qrcode.generate_payload(
            id="087-125-5555") == "00020101021129370016A000000677010111011300668712555555802TH5303764630482FE"
        assert qrcode.generate_payload(
            id="089-123-4567") == "00020101021129370016A000000677010111011300668912345675802TH5303764630429C1"
        assert qrcode.generate_payload(
            id="089-999-9999") == "00020101021129370016A000000677010111011300668999999995802TH53037646304FE29"

    def test_international_phone_number_format(self):
        assert qrcode.generate_payload(
            id="+66-00-000-0000") == "00020101021129370016A000000677010111011300660000000005802TH530376463048956"
        assert qrcode.generate_payload(
            id="+66-80-123-4567") == "00020101021129370016A000000677010111011300668012345675802TH530376463046197"
        assert qrcode.generate_payload(
            id="+66-81-983-7638") == "00020101021129370016A000000677010111011300668198376385802TH53037646304F963"
        assert qrcode.generate_payload(
            id="+66-84-948-8172") == "00020101021129370016A000000677010111011300668494881725802TH53037646304C907"
        assert qrcode.generate_payload(
            id="+66-87-125-5555") == "00020101021129370016A000000677010111011300668712555555802TH5303764630482FE"
        assert qrcode.generate_payload(
            id="+66-89-123-4567") == "00020101021129370016A000000677010111011300668912345675802TH5303764630429C1"
        assert qrcode.generate_payload(
            id="+66-89-999-9999") == "00020101021129370016A000000677010111011300668999999995802TH53037646304FE29"

    def test_national_id_format(self):
        assert qrcode.generate_payload(
            id="1111111111111") == "00020101021129370016A000000677010111021311111111111115802TH530376463047B5A"
        assert qrcode.generate_payload(
            id="1234567890123") == "00020101021129370016A000000677010111021312345678901235802TH53037646304EC40"
        assert qrcode.generate_payload(
            id="0123456789012") == "00020101021129370016A000000677010111021301234567890125802TH530376463040CBD"
        assert qrcode.generate_payload(
            id="8512819188690") == "00020101021129370016A000000677010111021385128191886905802TH5303764630400F4"
        assert qrcode.generate_payload(
            id="4912419510270") == "00020101021129370016A000000677010111021349124195102705802TH5303764630410C5"
        assert qrcode.generate_payload(
            id="0023637209811") == "00020101021129370016A000000677010111021300236372098115802TH530376463040C4C"

    def test_national_id_format_with_amount(self):
        # no decimal points
        assert qrcode.generate_payload(id="1111111111111",
                                       amount=878748) == "00020101021229370016A000000677010111021311111111111115802TH53037645409878748.0063042792"
        assert qrcode.generate_payload(id="1234567890123",
                                       amount=23) == "00020101021229370016A000000677010111021312345678901235802TH5303764540523.006304C4F2"

        # 2 decimal points
        assert qrcode.generate_payload(id="0123456789012",
                                       amount=4848.50) == "00020101021229370016A000000677010111021301234567890125802TH530376454074848.5063049BEA"
        assert qrcode.generate_payload(id="8512819188690",
                                       amount=541.23) == "00020101021229370016A000000677010111021385128191886905802TH53037645406541.23630437F5"

        # more than 2 decimal points
        assert qrcode.generate_payload(id="4912419510270",
                                       amount=4585485.5415) == "00020101021229370016A000000677010111021349124195102705802TH530376454104585485.546304DF31"
        assert qrcode.generate_payload(id="0023637209811",
                                       amount=72.985) == "00020101021229370016A000000677010111021300236372098115802TH5303764540572.986304E802"

    def test_dashed_national_id_format(self):
        assert qrcode.generate_payload(
            id="1-1111-11111-11-1") == "00020101021129370016A000000677010111021311111111111115802TH530376463047B5A"
        assert qrcode.generate_payload(
            id="1-2345-67890-12-3") == "00020101021129370016A000000677010111021312345678901235802TH53037646304EC40"
        assert qrcode.generate_payload(
            id="0-1234-56789-01-2") == "00020101021129370016A000000677010111021301234567890125802TH530376463040CBD"
        assert qrcode.generate_payload(
            id="8-5128-19188-69-0") == "00020101021129370016A000000677010111021385128191886905802TH5303764630400F4"
        assert qrcode.generate_payload(
            id="4-9124-19510-27-0") == "00020101021129370016A000000677010111021349124195102705802TH5303764630410C5"
        assert qrcode.generate_payload(
            id="0-0236-37209-81-1") == "00020101021129370016A000000677010111021300236372098115802TH530376463040C4C"

    def test_ewallet_id(self):
        # eWallet ID, KPlus ID
        assert qrcode.generate_payload(
            id="012345678901234") == "00020101021129390016A00000067701011103150123456789012345802TH530376463049781"
        assert qrcode.generate_payload(
            id="004999000288505") == "00020101021129390016A00000067701011103150049990002885055802TH530376463041521"

        # KPlus shop ID
        assert qrcode.generate_payload(
            id="004000006579718") == "00020101021129390016A00000067701011103150040000065797185802TH53037646304FBB5"

    def test_ewallet_id_with_amount(self):
        # no decimal points
        assert qrcode.generate_payload(
            id="012345678901234",
            amount=9874887) == "00020101021229390016A00000067701011103150123456789012345802TH530376454109874887.0063047158"

        # 2 decimal points
        assert qrcode.generate_payload(
            id="004999000288505",
            amount=1515.75) == "00020101021229390016A00000067701011103150049990002885055802TH530376454071515.756304522C"

        # more than 2 decimal points
        assert qrcode.generate_payload(
            id="004000006579718",
            amount=4848.458545) == "00020101021229390016A00000067701011103150040000065797185802TH530376454074848.466304BB6B"


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
