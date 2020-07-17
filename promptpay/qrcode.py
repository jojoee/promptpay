import re
import crc16
import qrcode

ID_PAYLOAD_FORMAT = '00'
ID_POI_METHOD = '01'
ID_MERCHANT_INFORMATION_BOT = '29'
ID_TRANSACTION_CURRENCY = '53'
ID_TRANSACTION_AMOUNT = '54'
ID_COUNTRY_CODE = '58'
ID_CRC = '63'

PAYLOAD_FORMAT_EMV_QRCPS_MERCHANT_PRESENTED_MODE = '01'
POI_METHOD_STATIC = '11'
POI_METHOD_DYNAMIC = '12'
MERCHANT_INFORMATION_TEMPLATE_ID_GUID = '00'
BOT_ID_MERCHANT_PHONE_NUMBER = '01'
BOT_ID_MERCHANT_TAX_ID = '02'
BOT_ID_MERCHANT_EWALLET_ID = '03'
GUID_PROMPTPAY = 'A000000677010111'
TRANSACTION_CURRENCY_THB = '764'
COUNTRY_CODE_TH = 'TH'


def sanitize_target(target=""):
    result = re.sub(r'\D', '', target)

    return result


def format_target(target=""):
    result = sanitize_target(target)

    if len(result) < 13:
        result = re.sub('^0', '66', result)
        result = ('0000000000000' + result)[-13:]  # last 13 digits

    return result


def format_amount(amount=0):
    result = '{0:.2f}'.format(amount)

    return result


def checksum(target=""):
    byte_str = target.encode('ascii')  # convert to bytes
    hex_str = hex(crc16.crc16xmodem(byte_str, 0xffff))
    code = hex_str.replace('0x', '').upper()
    result = ('0000' + code)[-4:]  # only last 4 digits

    return result


def format(id="", value=""):
    last2digits = ('00' + str(len(value)))[-2:]
    result = id + last2digits + value

    return result


def generate_payload(id="", amount=0):
    # sanitize id
    target = sanitize_target(id)

    # id type
    n_target_chars = len(target)
    target_type = BOT_ID_MERCHANT_PHONE_NUMBER
    if n_target_chars >= 15:
        target_type = BOT_ID_MERCHANT_EWALLET_ID
    elif n_target_chars >= 13:
        target_type = BOT_ID_MERCHANT_TAX_ID

    data = [
        format(ID_PAYLOAD_FORMAT, PAYLOAD_FORMAT_EMV_QRCPS_MERCHANT_PRESENTED_MODE),
        format(ID_POI_METHOD, POI_METHOD_DYNAMIC if amount else POI_METHOD_STATIC),
        format(ID_MERCHANT_INFORMATION_BOT, ''.join([
            format(MERCHANT_INFORMATION_TEMPLATE_ID_GUID, GUID_PROMPTPAY),
            format(target_type, format_target(target))
        ])),
        format(ID_COUNTRY_CODE, COUNTRY_CODE_TH),
        format(ID_TRANSACTION_CURRENCY, TRANSACTION_CURRENCY_THB)
        # amount & &
    ]
    if amount:
        data.append(format(ID_TRANSACTION_AMOUNT, format_amount(amount)))

    data2crc = ''.join(data) + ID_CRC + '04'
    data.append(format(ID_CRC, checksum(data2crc)))

    return ''.join(data)


def to_image(payload=""):
    img = qrcode.make(payload)
    return img


def to_file(payload="", filepath=""):
    imgfile = open(filepath, 'wb')
    img = to_image(payload)
    img.save(imgfile, 'PNG')
    imgfile.close()
