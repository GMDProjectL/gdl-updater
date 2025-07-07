pkgname=gdl-updater
pkgver=1.0
pkgrel=1
pkgdesc="Project GDL Installer Updater"
arch=('any')
url="https://github.com/GMDProjectL/gdl-updater"
license=('GPL')
depends=('python-requests' 'pyside6')
makedepends=()
checkdepends=()
optdepends=()
backup=()
options=()
install=
source=("git+file://${srcdir}")

export UPDATER_DIST="${pkgdir}/opt/gdl-updater"

package() {
    cd "$srcdir"
    mkdir -p "${UPDATER_DIST}"

    install -Dm0644 $srcdir/github.py -t ${UPDATER_DIST}
    install -Dm0644 $srcdir/main_window.py -t ${UPDATER_DIST}
    install -Dm0644 $srcdir/main.py -t ${UPDATER_DIST}
    install -Dm0644 $srcdir/update_threads.py -t ${UPDATER_DIST}
    install -Dm0644 $srcdir/update.py -t ${UPDATER_DIST}
    
    install -Dm0644 $srcdir/assets/gdl-updater.desktop -t "${pkgdir}/usr/share/applications"
}