#!/bin/sh
# Descifra el temario (carpeta temario/, cifrado con AES-256) en una carpeta local que NO se sube al repo.
# Uso: TEMARIO_CLAVE='la clave' sh scripts/temario.sh [texto|pdf|todo] [destino]
#   texto (por defecto): un .txt por manual con marcas «=== Página N del PDF ===» (para buscar con grep).
#   Destino por defecto: /tmp/temario  (NUNCA dentro del repo: el repo es público).
# Para cifrar un manual nuevo: TEMARIO_CLAVE=... sh scripts/temario.sh cifrar "Bloque II - Tema NN - Título.pdf"
set -e
cd "$(dirname "$0")/.."
[ -n "$TEMARIO_CLAVE" ] || { echo "Falta TEMARIO_CLAVE"; exit 1; }
QUE=${1:-texto}; DEST=${2:-/tmp/temario}
if [ "$QUE" = cifrar ]; then
  f="$2"; n=$(basename "$f" .pdf)
  openssl enc -aes-256-cbc -pbkdf2 -iter 200000 -salt -pass env:TEMARIO_CLAVE -in "$f" -out "temario/pdf/$n.pdf.enc"
  pdftotext -enc UTF-8 "$f" - | python3 -c "import sys;p=sys.stdin.read().split('\f');p=p[:-1] if p and not p[-1].strip() else p;sys.stdout.write(''.join(f'\n=== Página {i} del PDF ===\n{x}' for i,x in enumerate(p,1)))" > "/tmp/$n.txt"
  openssl enc -aes-256-cbc -pbkdf2 -iter 200000 -salt -pass env:TEMARIO_CLAVE -in "/tmp/$n.txt" -out "temario/texto/$n.txt.enc"
  rm -f "/tmp/$n.txt"; echo "Cifrado: $n (añádelo a temario/indice.json y a tandas/TEMARIO_BASES.md)"; exit 0
fi
case "$DEST" in "$(pwd)"*) echo "El destino no puede estar dentro del repo"; exit 1;; esac
mkdir -p "$DEST"
for sub in texto pdf; do
  [ "$QUE" = todo ] || [ "$QUE" = "$sub" ] || continue
  for f in temario/$sub/*.enc; do
    n=$(basename "$f" .enc)
    openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -pass env:TEMARIO_CLAVE -in "$f" -out "$DEST/$n"
  done
done
echo "Temario descifrado en $DEST ($(ls "$DEST" | wc -l) archivos)"
