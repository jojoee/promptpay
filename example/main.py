from promptpay import qrcode

print("phone format")
print(qrcode.generate_payload(id="0000000000"))
print(qrcode.generate_payload(id="0801234567"))
print(qrcode.generate_payload(id="0819837638"))
print(qrcode.generate_payload(id="0849488172"))
print(qrcode.generate_payload(id="0871255555"))
print(qrcode.generate_payload(id="0891234567"))
print(qrcode.generate_payload(id="0899999999"))

print("phone format with amount")
print(qrcode.generate_payload(id="0000000000", amount=100))
print(qrcode.generate_payload(id="0801234567", amount=456.25))
print(qrcode.generate_payload(id="0819837638", amount=5476521.50))
print(qrcode.generate_payload(id="0849488172", amount=81545415.75))
print(qrcode.generate_payload(id="0871255555", amount=4864688.23))
print(qrcode.generate_payload(id="0891234567", amount=445465.654878))
print(qrcode.generate_payload(id="0899999999", amount=484848.4645))

print("dashed phone format")
print(qrcode.generate_payload(id="000-000-0000"))
print(qrcode.generate_payload(id="080-123-4567"))
print(qrcode.generate_payload(id="081-983-7638"))
print(qrcode.generate_payload(id="084-948-8172"))
print(qrcode.generate_payload(id="087-125-5555"))
print(qrcode.generate_payload(id="089-123-4567"))
print(qrcode.generate_payload(id="089-999-9999"))

print("international phone format")
print(qrcode.generate_payload(id="+66-00-000-0000"))
print(qrcode.generate_payload(id="+66-80-123-4567"))
print(qrcode.generate_payload(id="+66-81-983-7638"))
print(qrcode.generate_payload(id="+66-84-948-8172"))
print(qrcode.generate_payload(id="+66-87-125-5555"))
print(qrcode.generate_payload(id="+66-89-123-4567"))
print(qrcode.generate_payload(id="+66-89-999-9999"))

print("national id")
print(qrcode.generate_payload(id="1111111111111"))
print(qrcode.generate_payload(id="1234567890123"))
print(qrcode.generate_payload(id="0123456789012"))
print(qrcode.generate_payload(id="8512819188690"))
print(qrcode.generate_payload(id="4912419510270"))
print(qrcode.generate_payload(id="0023637209811"))

print("national id with amount")
print(qrcode.generate_payload(id="1111111111111", amount=878748))
print(qrcode.generate_payload(id="1234567890123", amount=23))
print(qrcode.generate_payload(id="0123456789012", amount=4848.50))
print(qrcode.generate_payload(id="8512819188690", amount=541.23))
print(qrcode.generate_payload(id="4912419510270", amount=4585485.5415))
print(qrcode.generate_payload(id="0023637209811", amount=72.985))

print("dashed national id format")
print(qrcode.generate_payload(id="1-1111-11111-11-1"))
print(qrcode.generate_payload(id="1-2345-67890-12-3"))
print(qrcode.generate_payload(id="0-1234-56789-01-2"))
print(qrcode.generate_payload(id="8-5128-19188-69-0"))
print(qrcode.generate_payload(id="4-9124-19510-27-0"))
print(qrcode.generate_payload(id="0-0236-37209-81-1"))

print("ewallet format")
print(qrcode.generate_payload(id="012345678901234"))
print(qrcode.generate_payload(id="004999000288505"))
print(qrcode.generate_payload(id="004000006579718"))

print("ewallet format with amount")
print(qrcode.generate_payload(id="012345678901234", amount=9874887))
print(qrcode.generate_payload(id="004999000288505", amount=1515.75))
print(qrcode.generate_payload(id="004000006579718", amount=4848.458545))
