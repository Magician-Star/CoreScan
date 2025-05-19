#!/bin/bash

# Nome e versão do pacote
PKG_NAME="core-scan"
VERSION="1.0.0"
EXECUTAVEL="CoreScan"
MAINTAINER="Gabriel Fernando <bielcreatina@gmail.com>"

# Caminhos
BUILD_DIR="${PKG_NAME}_${VERSION}"
BIN_DIR="${BUILD_DIR}/usr/bin"
DESKTOP_DIR="${BUILD_DIR}/usr/share/applications"
ICON_DIR="${BUILD_DIR}/usr/share/icons/hicolor/64x64/apps"
DEBIAN_DIR="${BUILD_DIR}/DEBIAN"

# Limpa estrutura antiga
rm -rf "$BUILD_DIR"

# Cria estrutura de diretórios
mkdir -p "$BIN_DIR" "$DESKTOP_DIR" "$ICON_DIR" "$DEBIAN_DIR"

# Copia o executável
cp "$EXECUTAVEL" "$BIN_DIR/"
chmod 755 "$BIN_DIR/$EXECUTAVEL"

# Cria o arquivo .desktop
cat <<EOF > "$DESKTOP_DIR/${PKG_NAME}.desktop"
[Desktop Entry]
Name=CoreScan
Exec=${EXECUTAVEL}
Icon=corescan-logo
Type=Application
Categories=Utility;
EOF

# Copia o ícone
cp "icons/corescan-logo.png" "$ICON_DIR/"

# Cria o arquivo control
cat <<EOF > "$DEBIAN_DIR/control"
Package: ${PKG_NAME}
Version: ${VERSION}
Section: utils
Priority: optional
Architecture: amd64
Depends: libc6 (>= 2.27)
Maintainer: ${MAINTAINER}
Description: Visualizador de informações do sistema (CoreScan)
EOF

# Gera o .deb
dpkg-deb --build "$BUILD_DIR"

echo "✅ Pacote .deb gerado: ${BUILD_DIR}.deb"
