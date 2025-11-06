pkgname = "tomb"
pkgver = "2.13"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
depends = [
    "cmd:pinentry!pinentry-curses",
    "cryptsetup",
    "file",
    "gnupg",
    "opendoas",
    "zsh",
]
pkgdesc = (
    "Tomb facilitates managing secret data in volumes protected by encryption"
)
license = "GPL-3.0-or-later"
url = "https://dyne.org/tomb"
source = f"https://github.com/dyne/tomb/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0164b1e036c4cf608dd07553258b67d02b57a507b83d1b05872ea4076d142379"
# the tests do not work without sudo
options = ["!check"]
