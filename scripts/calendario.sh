#!/bin/sh
# Amplía el calendario hasta 21 días por delante con preguntas ya aprobadas, en el orden correcto.
cd "$(dirname "$0")/.." && python3 scripts/plan.py "$@" && python3 scripts/intervencion.py && python3 scripts/examen.py && python3 scripts/dibujos.py && python3 scripts/sin_repetir.py
