#/usr/bin/bash

echo --------------------Run Tests--------------------
echo "🔬  Running pytest tests…" &&
. venv/bin/activate
pytest -v --cov=api --exitfirst
echo "👌  OK!"
echo --------------------Finished Test Run--------------------