import pathlib
from setuptools import setup, find_packages

requirements = ["qrcode", "libscrc", "Pillow"]

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="promptpay",
    version="1.1.8",
    description="Python library to generate PromptPay QR Code",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jojoee/promptpay",
    author="Nathachai Thongniran",
    author_email="inid3a@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=requirements,
    keywords=["promptpay", "qrcode"],
    entry_points={"console_scripts": ["promptpay=promptpay.__main__:main"]},
)
