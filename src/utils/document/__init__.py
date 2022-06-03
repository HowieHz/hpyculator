# i18n
import gettext
import os
langs = ["en"]
for lang in langs:
    gettext.install(lang, localedir=os.path.join(".", "utils", "locale"))

from . import docs
from . import version
from . import tags

START_SHOW = docs.START_SHOW
CHANGELOG = docs.CHANGELOG
VERSION = version.VERSION
ABOUT = docs.ABOUT
