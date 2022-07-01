from pathlib import Path

from setuptools import find_packages, setup

description = "这是一个基于python的高拓展性计算器"

# with open(r"..\README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

THIS_DIR = Path(__file__).resolve().parent
# try:
#     long_description = (THIS_DIR / 'README.md').read_text()
# except FileNotFoundError:
#     long_description = description
long_description = (THIS_DIR / "README.md").read_text(encoding="utf-8")

VERSION = "1.0.0"

setup(
    # 以下为必需参数
    name="hpyc_core",
    version=VERSION,
    description=description,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HowieHz/hpyculator",
    author="HowieHz",  # 作者名
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=["hpyculator"],
    project_urls={
        "Bug Reports": "https://github.com/HowieHz/hpyculator/issues",
    },
)
