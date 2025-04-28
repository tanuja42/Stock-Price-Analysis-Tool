# Stock-Price-Analysis-Tool
This implementation combines three key components:

1. Data Structures:

Linked List: Stores historical stock prices using StockNode class

Stack: Efficiently calculates stock spans using a decreasing monotonic stack

2. Core Functionality:

Dynamic price updates with timestamp tracking

Span calculation (consecutive days with ≤ current price)

Real-time maximum span tracking

Data constraints (price limits between $50-$200)

3. Visualization:

Dual-axis line plot showing both price and span

Auto-updating display using matplotlib animation

Clear labeling and color coding for different metrics

To use:

Save as stock_analyzer.py

Install dependencies: pip install matplotlib

Run: python stock_analyzer.py

The simulation will show:

Blue line: Stock price movement

Red dashed line: Current span values

Console output with timestamped updates

Automatic y-axis scaling for both price and span

Real-time maximum span display in title

For real-world data integration, replace the simulation loop with API calls to financial data services (like Yahoo Finance using yfinance).


