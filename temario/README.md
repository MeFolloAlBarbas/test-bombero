# Temario (cifrado)

Manuales del temario de Bombero/a Especialista, con el nombre de cada tema según el Anexo III de las bases
(ver `tandas/TEMARIO_BASES.md`). **Están cifrados (AES-256): sin la clave no se pueden abrir.**

- `pdf/` — los PDF originales, cifrados.
- `texto/` — el texto de cada manual, con marcas `=== Página N del PDF ===`, cifrado.
- `indice.json` — nombre y número de páginas de cada manual (sin contenido).

Para descifrar (en una carpeta fuera del repo): `TEMARIO_CLAVE='…' sh scripts/temario.sh [texto|pdf|todo] /tmp/temario`.
Nunca subas al repo los archivos descifrados.
