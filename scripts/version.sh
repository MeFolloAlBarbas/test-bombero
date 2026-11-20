#!/bin/sh
# Ejecutar antes de cada commit que cambie la web: fuerza a los navegadores a recargar
cd "$(dirname "$0")/.." && V=$(date +%s) && echo $V > version.txt && sed -i "s/const APPV='[0-9]*'/const APPV='$V'/" index.html
