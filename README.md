# Black-Scholes Option Pricing (Streamlit App)

Interactive Streamlit app to price European call and put options using the Black–Scholes model. Provides instant pricing for given inputs and visualizes how prices change across ranges of current price and volatility via heatmaps.

## Features
- Real‑time Black–Scholes pricing for call and put options
- Adjustable inputs: current price (S), strike (K), time to maturity (t, years), risk‑free rate (r), volatility (σ)
- Dual heatmaps showing call/put values across S and σ (±20% around inputs)
- In‑app reference table explaining each variable

## Quick Start

Option A — using uv (recommended):
```bash
# 1) Install uv if needed: https://docs.astral.sh/uv/
# macOS/Linux: curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows (PowerShell): iwr https://astral.sh/uv/install.ps1 -UseBasicParsing | iex

# 2) Create venv and sync deps
uv venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\activate
uv sync

# 3) Run the app
uv run streamlit run src/app.py
```

Option B — using pip:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\activate
pip install --upgrade pip
pip install .
streamlit run src/app.py
```

Then open the URL printed by Streamlit (defaults to http://localhost:8501).

## Requirements
- Python ≥ 3.13 (as specified in `pyproject.toml`)
- Dependencies are managed via `pyproject.toml`/`uv.lock`:
  - numpy, scipy, pandas, matplotlib, seaborn, streamlit

If your local Python is older, upgrade Python or adjust `requires-python` in `pyproject.toml` to a compatible version for your environment and dependencies.

## Usage
1. Enter inputs in the sidebar grid:
   - Current Asset Price (S)
   - Strike Price (K)
   - Time to Maturity in years (t)
   - Volatility as a decimal (σ), e.g., 0.2 for 20%
   - Risk‑Free Rate as a decimal (r), e.g., 0.05 for 5%
2. View computed Call and Put prices.
3. Explore heatmaps to see sensitivity to S and σ around your inputs.

Conventions:
- Rates and volatility are decimals (not percentages).
- Time is in years (e.g., 0.5 = 6 months).
- Model assumes European options and no dividends.

## How It Works
Given S, K, t, r, σ:

```
d1 = (ln(S/K) + (r + σ²/2) t) / (σ √t)
d2 = d1 − σ √t

Call C = S·N(d1) − K·e^(−rt)·N(d2)
Put  P = K·e^(−rt)·N(−d2) − S·N(−d1)
```

`N(·)` is the standard normal CDF (from SciPy). Heatmaps vary S and σ by ±20% (by default) to visualize pricing sensitivity.

## Usage
You can import and use the pricing class without Streamlit:

```python
from BlackScholes import BlackScholes

model = BlackScholes(current_price=100.0, strike_price=100.0,
                     time=1.0, interest_rate=0.05, volatility=0.2)
call, put = model.calculate_prices()
print(f"Call: {call:.2f}, Put: {put:.2f}")

# Create a matplotlib Figure with call/put heatmaps
fig = model.heatmap()
```

Key APIs:
- `BlackScholes.calculate_prices() -> tuple[float, float]`
- `BlackScholes.heatmap() -> matplotlib.figure.Figure`

## Project Structure
```
src/
  app.py             # Streamlit UI and layout
  BlackScholes.py    # Pricing logic and heatmap generation
pyproject.toml       # Project metadata and dependencies
uv.lock              # Locked dependency resolution for uv
```

## Troubleshooting
- Python version errors: ensure Python ≥ 3.13, or adjust `requires-python` if you intend to run on an earlier version that supports these dependency ranges.
- SciPy/NumPy install issues: upgrade pip and wheel (`pip install -U pip wheel`) and try again.
- Port in use: run `streamlit run src/app.py --server.port 8502`.

## Contributing
Issues and PRs are welcome. For larger changes, please open an issue to discuss first.

## License
you can use this code and critique it idc
