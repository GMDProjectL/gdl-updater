pkgname=gdl-updater
pkgver=1.1
pkgrel=1
pkgdesc="Project GDL Installer Updater"
arch=('any')
url="https://github.com/GMDProjectL/gdl-updater"
license=('GPL')
depends=('python-requests' 'python-systemd' 'pyside6')
makedepends=()
checkdepends=()
optdepends=()
backup=()
options=()
install=
source=(${pkgname}::"git+file://${PWD}")

export UPDATER_DIST="${pkgdir}/opt/gdl-updater"

package() {
    cd "$srcdir"
    mkdir -p "${UPDATER_DIST}"

    install -Dm0644 $srcdir/${pkgname}/github.py -t ${UPDATER_DIST}
    install -Dm0644 $srcdir/${pkgname}/main_window.py -t ${UPDATER_DIST}
    install -Dm0644 $srcdir/${pkgname}/main.py -t ${UPDATER_DIST}
    install -Dm0644 $srcdir/${pkgname}/update_threads.py -t ${UPDATER_DIST}
    install -Dm0644 $srcdir/${pkgname}/update.py -t ${UPDATER_DIST}
    
    install -Dm0644 $srcdir/${pkgname}/assets/gdl-updater.desktop -t "${pkgdir}/usr/share/applications"
}
