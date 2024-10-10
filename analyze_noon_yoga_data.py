import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('noon_yoga_products.csv')

df['Price'] = df['Price'].replace('[\AED,]', '', regex=True).astype(float)

most_expensive = df.loc[df['Price'].idxmax()]
print(f"Most Expensive Product: {most_expensive['Title']} - AED {most_expensive['Price']}")

cheapest_product = df.loc[df['Price'].idxmin()]
print(f"Cheapest Product: {cheapest_product['Title']} - AED {cheapest_product['Price']}")

brand_counts = df['Brand'].value_counts()
print("\nNumber of Products by Brand:")
print(brand_counts)

seller_counts = df['Seller'].value_counts()
print("\nNumber of Products by Seller:")
print(seller_counts)


plt.figure(figsize=(10, 6))
brand_counts.plot(kind='bar')
plt.title('Number of Products by Brand')
plt.xlabel('Brand')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
seller_counts.plot(kind='bar')
plt.title('Number of Products by Seller')
plt.xlabel('Seller')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
