#!/bin/bash

# Nome e versão
PKG_NAME="core-scan"
VERSION="1.0.0"
APP_NAME="CoreScan"
MAINTAINER="Gabriel Fernando <bielcreatina@gmail.com>"

# Estrutura de pastas
BUILD_DIR="${PKG_NAME}_${VERSION}"
OPT_APP_DIR="${BUILD_DIR}/opt/${APP_NAME}"
BIN_LINK_DIR="${BUILD_DIR}/usr/bin"
DESKTOP_DIR="${BUILD_DIR}/usr/share/applications"
ICON_DIR="${BUILD_DIR}/usr/share/icons/hicolor/64x64/apps"
DEBIAN_DIR="${BUILD_DIR}/DEBIAN"

# Limpar build anterior
rm -rf "$BUILD_DIR"

# Criar estrutura
mkdir -p "$OPT_APP_DIR" "$BIN_LINK_DIR" "$DESKTOP_DIR" "$ICON_DIR" "$DEBIAN_DIR"

# Copiar executável e assets para /opt/CoreScan/
cp -r dist/${APP_NAME}/* "$OPT_APP_DIR/"
chmod +x "$OPT_APP_DIR/${APP_NAME}"

# Criar script de atalho em /usr/bin/
cat <<EOF > "${BIN_LINK_DIR}/${APP_NAME}"
#!/bin/bash
/opt/${APP_NAME}/${APP_NAME} "\$@"
EOF
chmod 755 "${BIN_LINK_DIR}/${APP_NAME}"


# Criar .desktop com descrição
cat <<EOF > "${DESKTOP_DIR}/${PKG_NAME}.desktop"
[Desktop Entry]
Name=CoreScan
Exec=${APP_NAME}
Icon=corescan-logo
Type=Application
Categories=Utility;
Comment=Visualizador de informações do sistema
EOF


# Copiar ícone
cp "/home/gabriel/Área de trabalho/Ambiente SPYDER/CoreScan/dist/CoreScan/assets/icons/corescan-logo.png" "$ICON_DIR/"

# Criar control
cat <<EOF > "${DEBIAN_DIR}/control"
Package: ${PKG_NAME}
Version: ${VERSION}
Section: utils
Priority: optional
Architecture: amd64
Depends: libc6 (>= 2.27)
Maintainer: ${MAINTAINER}
Description: Visualizador de informações do sistema (CoreScan)
EOF

# Empacotar
dpkg-deb --build "$BUILD_DIR"

echo "✅ Pacote .deb criado: ${BUILD_DIR}.deb"

