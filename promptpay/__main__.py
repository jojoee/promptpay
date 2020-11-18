import sys
from promptpay import qrcode

USAGE = """promptpay
Usage:
------
    $ promptpay qrcode --id="0841234567"
    $ promptpay qrcode --id="0841234567" --file="./qrcode-cli.png"
    $ promptpay qrcode --id="0841234567" --show=true
    $ promptpay qrcode --id="0841234567" --amount=2.34 --file="/Users/joe/Downloads/qrcode-cli-with-amount.png"

Available options are:
    -h, --help         Show this help
"""


def main():
    if sys.argv[1] == "qrcode" and len(sys.argv) > 2:
        args = sys.argv[2:]

        id_or_phone_number = None
        filepath = None
        amount = 0
        is_show = False

        # parsing
        for arg in args:
            if arg.startswith("--id"):
                id_or_phone_number = str(arg.split("=", 1)[1])
            elif arg.startswith("--amount"):
                amount = float(arg.split("=", 1)[1])
            elif arg.startswith("--file"):
                filepath = str(arg.split("=", 1)[1])
            elif arg.startswith("--show"):
                is_show = str(arg.split("=", 1)[1]).lower() == 'true'
            else:
                print("you are passing invalid argument", arg)
                sys.exit(0)

        if id_or_phone_number:
            payload = qrcode.generate_payload(id_or_phone_number, amount)
            print("payload of %s: %s" % (id_or_phone_number, payload))
            if filepath:
                qrcode.to_file(payload, filepath)
            if is_show:
                if sys.stdout.isatty():
                    qrcode.print_tty(payload)
                else:
                    img = qrcode.to_image(payload)
                    img.show()

    else:
        print(USAGE)
        sys.exit(0)


if __name__ == "__main__":
    main()
