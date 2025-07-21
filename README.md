# Let's Learn MCP

This project is for learning MCP (Model Context Protocol).

## Setup

1. Install uv if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create and activate virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   uv pip install -e .
   ```

## Development

Install development dependencies:
```bash
uv pip install -e ".[dev]"
```

## Usage

```python
python main.py
```