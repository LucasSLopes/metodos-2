# metodos-2

## Setup

### Com uv

Requer [uv](https://docs.astral.sh/uv/) instalado.

```bash
# instalar dependências
uv sync

# ativar o ambiente virtual
source .venv/bin/activate

# executar um notebook
uv run main.py
```

### Sem uv

```bash
python -m venv .venv
source .venv/bin/activate
pip install matplotlib pandas sympy
python main.py
```
