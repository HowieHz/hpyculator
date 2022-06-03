# i18n
from . import tags
from . import version
from . import docs
import gettext
import os

langs = ["en"]
for lang in langs:
    gettext.install(lang, localedir=os.path.join(".", "utils", "locale"))


START_SHOW = docs.START_SHOW
CHANGELOG = docs.CHANGELOG
VERSION = version.VERSION
ABOUT = docs.ABOUT
