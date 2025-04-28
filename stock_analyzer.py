import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

class StockNode:
    def __init__(self, timestamp, price):
        self.timestamp = timestamp
        self.price = price
        self.next = None

class StockAnalyzer:
    def __init__(self):
        self.head = None
        self.price_stack = []
        self.time_data = []
        self.price_data = []
        self.span_data = []
        
    def add_price(self, timestamp, price):
        new_node = StockNode(timestamp, price)
        new_node.next = self.head
        self.head = new_node
        
        span = 1
        while self.price_stack and self.price_stack[-1][0] <= price:
            span += self.price_stack.pop()[1]
        self.price_stack.append((price, span))
        
        self.time_data.append(timestamp)
        self.price_data.append(price)
        self.span_data.append(span)
        return span

    def get_max_span(self):
        return max(self.span_data) if self.span_data else 0

class StockVisualizer:
    def __init__(self):
        self.analyzer = StockAnalyzer()
        self.fig, self.ax = plt.subplots()
        plt.show(block=False)
        
    def update_plot(self):
        self.ax.clear()
        self.ax.plot(self.analyzer.time_data, self.analyzer.price_data, 'b-')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Price', color='b')
        self.ax.tick_params(axis='y', labelcolor='b')
        
        self.ax2 = self.ax.twinx()
        self.ax2.plot(self.analyzer.time_data, self.analyzer.span_data, 'r--')
        self.ax2.set_ylabel('Span', color='r')
        self.ax2.tick_params(axis='y', labelcolor='r')
        
        plt.title(f'Stock Price Analysis (Max Span: {self.analyzer.get_max_span()})')
        plt.draw()
        plt.pause(0.1)

def simulate_stock_data():
    visualizer = StockVisualizer()
    start_time = datetime.now()
    price = 100 + random.random() * 50
    
    for _ in range(100):
        timestamp = start_time + timedelta(minutes=5*_)
        price += (random.random() - 0.5) * 10
        price = round(max(50, min(200, price)), 2)
        
        visualizer.analyzer.add_price(timestamp, price)
        visualizer.update_plot()
        
        print(f"Time: {timestamp.strftime('%H:%M')} | Price: ${price} | Current Span: {visualizer.analyzer.span_data[-1]}")

simulate_stock_data()
