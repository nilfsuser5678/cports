pkgname = "vulkan-utility-libraries"
pkgver = "1.3.302"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "gtest-devel",
    "magic_enum",
    "vulkan-headers",
]
depends = ["vulkan-headers"]
pkgdesc = "Utility libraries for Vulkan"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/Vulkan-Utility-Libraries"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d9e0903e3a2916e2be8ca49f7ee750a1364e33fa021f5bbc02e032c4d54a8bbd"
# broken cmake files
tool_flags = {"CXXFLAGS": ["-I/usr/include/magic_enum"]}
# static-only library, so just keep it as one package
options = ["!lintstatic"]
