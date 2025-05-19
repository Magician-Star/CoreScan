#!/bin/bash

APP_NAME="CoreScan"
APPDIR="${APP_NAME}.AppDir"
ICON_NAME="corescan-logo.png"

# Limpar build anterior
rm -rf "$APPDIR" "${APP_NAME}.AppImage"

# Criar estrutura
mkdir -p "$APPDIR/icons"
cp -r dist/${APP_NAME}/* "$APPDIR/"
cp icons/${ICON_NAME} "$APPDIR/icons/"

# Criar AppRun
cat <<EOF > "$APPDIR/AppRun"
#!/bin/bash
HERE="\$(dirname "\$(readlink -f "\$0")")"
exec "\$HERE/${APP_NAME}" "\$@"
EOF
chmod +x "$APPDIR/AppRun"

# Criar .desktop
cat <<EOF > "$APPDIR/core-scan.desktop"
[Desktop Entry]
Name=CoreScan
Exec=${APP_NAME}
Icon=icons/corescan-logo
Type=Application
Categories=Utility;
Comment=Visualizador de informações do sistema
EOF

# Gerar AppImage
echo "🛠️ Gerando AppImage..."
appimagetool "$APPDIR"

echo "✅ AppImage gerado: ${APP_NAME}-x86_64.AppImage"

