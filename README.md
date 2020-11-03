# PromptPay

![flake8 + pytest](https://github.com/jojoee/promptpay/workflows/flake8%20+%20pytest/badge.svg?branch=master)
[![PyPI version fury.io](https://badge.fury.io/py/promptpay.svg)](https://pypi.python.org/pypi/promptpay/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/jojoee/promptpay/branch/master/graph/badge.svg)](https://codecov.io/gh/jojoee/promptpay)

Python library to generate PromptPay QR Code, inspired from [dtinth/promptpay-qr](https://github.com/dtinth/promptpay-qr)

## Installation
```
pip install promptpay

# or
git clone https://github.com/jojoee/promptpay
cd promptpay
python setup.py install
```

## Usage

### Library

```python
from promptpay import qrcode

# generate a payload
id_or_phone_number = "0841234567"
payload = qrcode.generate_payload(id_or_phone_number)
payload_with_amount = qrcode.generate_payload(id_or_phone_number, 1.23)

# export to PIL image
img = qrcode.to_image(payload)

# export to file
qrcode.to_file(payload, "./qrcode-0841234567.png")
qrcode.to_file(payload_with_amount, "/Users/joe/Downloads/qrcode-0841234567.png") 
```

### CLI

```bash
python -m promptpay qrcode --id="0841234567"
python -m promptpay qrcode --id="0841234567" --file="./qrcode-cli.png"
python -m promptpay qrcode --id="0841234567" --show=true
python -m promptpay qrcode \
  --id="0841234567" \
  --amount=2.34 \
  --file="/Users/joe/Downloads/qrcode-cli-with-amount.png"
```

## Reference
- [มีอะไรอยู่ใน PromptPay QR แกะสเปค QR ที่จะใช้จ่ายผ่าน mobile banking ได้ทุกธนาคารในอนาคต](https://www.blognone.com/node/95133)