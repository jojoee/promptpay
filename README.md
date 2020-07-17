# PromptPay

![Continuous Integration (pip)](https://github.com/jojoee/promptpay/workflows/Continuous%20Integration%20(pip)/badge.svg?branch=master)
![Continuous Deployment (pip)](https://github.com/jojoee/promptpay/workflows/Continuous%20Deployment%20(pip)/badge.svg)
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

## Reference
- [มีอะไรอยู่ใน PromptPay QR แกะสเปค QR ที่จะใช้จ่ายผ่าน mobile banking ได้ทุกธนาคารในอนาคต](https://www.blognone.com/node/95133)
