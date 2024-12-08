import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
plt.style.use('dark_background')
sns.set_palette("husl")

# Create sample data
np.random.seed(42)
n_companies = 100

# Generate market cap data
market_caps = np.exp(np.random.normal(10, 2, n_companies))
prices = market_caps * np.random.uniform(0.01, 0.05, n_companies)
sectors = np.random.choice(['Technology', 'Healthcare', 'Finance', 'Energy', 'Consumer'], n_companies)

df = pd.DataFrame({
    'market_cap': market_caps,
    'price': prices,
    'sector': sectors
})

# Price Distribution Plot
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='market_cap', y='price', hue='sector', alpha=0.7, s=100)
plt.title('Stock Price vs Market Cap by Sector', fontsize=14, pad=20)
plt.xlabel('Market Cap (Billions)', fontsize=12)
plt.ylabel('Stock Price ($)', fontsize=12)
plt.yscale('log')
plt.xscale('log')
plt.grid(True, alpha=0.2)
plt.legend(title='Sector', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('images/price_dist.png', dpi=300, bbox_inches='tight', facecolor='#0f172a')
plt.close()

# Sector Performance Plot
sector_perf = pd.DataFrame({
    'sector': ['Technology', 'Healthcare', 'Finance', 'Energy', 'Consumer'],
    'returns': np.random.normal(0.15, 0.05, 5),
    'volatility': np.random.uniform(0.2, 0.4, 5)
})

plt.figure(figsize=(12, 8))
sns.barplot(data=sector_perf, x='sector', y='returns', alpha=0.7)
plt.title('Average Returns by Sector', fontsize=14, pad=20)
plt.xlabel('Sector', fontsize=12)
plt.ylabel('Annual Returns (%)', fontsize=12)
plt.grid(True, alpha=0.2)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/sector_performance.png', dpi=300, bbox_inches='tight', facecolor='#0f172a')
plt.close()
