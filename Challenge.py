#!/usr/bin/env python
# coding: utf-8

# In[202]:


import pandas as pd
file_path = r"C:\Users\ogunb\OneDrive\Desktop\Challenge\orders.json"
df_orders = pd.read_json(file_path, lines=True)


# In[201]:


file_path = r"C:\Users\ogunb\OneDrive\Desktop\Challenge\products.json"
df_products = pd.read_json(file_path, lines=True)


# # 1. Calculate the net sales amount.

# In[187]:


def calculate_net_sales_amount(df_orders):
    df_Sales = df_orders[['product_id','price','status']].copy()
    df_Sales = df_Sales.sort_values('product_id')
    df_Sales['Quantity'] = df_Sales.groupby(['product_id', 'status'])['product_id'].transform('count')
    df_Sales = df_Sales.drop_duplicates(subset = ['product_id'])
    df_Sales['Sales'] = df_Sales['Quantity'] * df_Sales['price']

    sales_created = df_Sales[df_Sales['status'] == 'Created']
    total_sales_created = sales_created['Sales'].sum().round()

    sales_Cancelled = df_Sales[df_Sales['status'] == 'Cancelled']
    total_sales_Cancelled = sales_Cancelled['Sales'].sum().round()

    sales_returned = df_Sales[df_Sales['status'] == 'Returned']
    total_sales_returned= sales_returned['Sales'].sum().round()

    Net_Sales_Amount = total_sales_created - (total_sales_Cancelled + total_sales_returned)
    
    return int(Net_Sales_Amount)
net_sales = calculate_net_sales_amount(df_orders)
print(f'The net sales amount is: {net_sales}')


# # 2.Calculate the average net sales price.

# In[188]:


def calculate_Average_Net_Salesprice(df_orders):
    df_Sales = df_orders[['product_id','price','status']].copy()
    df_Sales = df_Sales.sort_values('product_id')
    df_Sales['Quantity'] = df_Sales.groupby(['product_id', 'status'])['product_id'].transform('count')
    df_Sales = df_Sales.drop_duplicates(subset = ['product_id'])
    df_Sales['Sales'] = df_Sales['Quantity'] * df_Sales['price']

    sales_created = df_Sales[df_Sales['status'] == 'Created']
    total_sales_created = sales_created['Sales'].sum().round()

    sales_Cancelled = df_Sales[df_Sales['status'] == 'Cancelled']
    total_sales_Cancelled = sales_Cancelled['Sales'].sum().round()

    sales_returned = df_Sales[df_Sales['status'] == 'Returned']
    total_sales_returned= sales_returned['Sales'].sum().round()

    Net_Sales_Amount = total_sales_created - (total_sales_Cancelled + total_sales_returned)
    
    df_Qty = df_orders[['product_id','price','status']].copy()
    df_Qty = df_Qty.sort_values('product_id')
    df_Qty['Quantity'] = df_Qty.groupby(['product_id', 'status'])['product_id'].transform('count')
    df_Qty = df_Qty.drop_duplicates(subset = ['product_id'])

    Quantity_created = df_Qty[df_Qty['status'] == 'Created']
    Quantity_Cancelled = df_Qty[df_Qty['status'] == 'Cancelled']
    Quantity_returned = df_Qty[df_Qty['status'] == 'Returned']

    total_Quantity_created = Quantity_created['Quantity'].sum()
    total_Quantity_Cancelled = Quantity_Cancelled['Quantity'].sum()
    total_Quantity_returned= Quantity_returned['Quantity'].sum()

    Net_Quantity_Sold = total_Quantity_created - (total_Quantity_Cancelled + total_Quantity_returned)

    Average_Net_Salesprice = (Net_Sales_Amount / Net_Quantity_Sold).round(2)

    return Average_Net_Salesprice
Average_Net_Salesprice = calculate_Average_Net_Salesprice(df_orders)
print(f'The Average Net Salesprice is: {Average_Net_Salesprice}')


# # Calculate the gross (total) sales amount

# In[189]:


def calculate_Gross_sales_amount(df_orders):
    df_Sales = df_orders[['product_id','price','status']].copy()
    df_Sales = df_Sales.sort_values('product_id')
    df_Sales['Quantity'] = df_Sales.groupby(['product_id', 'status'])['product_id'].transform('count')
    df_Sales = df_Sales.drop_duplicates(subset = ['product_id'])
    df_Sales['Sales'] = df_Sales['Quantity'] * df_Sales['price']
    
    Gross_sales= df_Sales['Sales'].sum().round()
    
    return int( Gross_sales)
Gross_sales = calculate_Gross_sales_amount(df_orders)
print(f'The gross (total) sales amount is: {Gross_sales}')


# # Calculate the average gross (total) sales price.

# In[190]:


def calculate_Av_Gross_salesprice(df_orders):
    df_Sales = df_orders[['product_id','price','status']].copy()
    df_Sales = df_Sales.sort_values('product_id')
    df_Sales['Quantity'] = df_Sales.groupby(['product_id', 'status'])['product_id'].transform('count')
    df_Sales = df_Sales.drop_duplicates(subset = ['product_id'])
    df_Sales['Sales'] = df_Sales['Quantity'] * df_Sales['price']
    
    Gross_sales= df_Sales['Sales'].sum().round()
    
    df_Qty = df_orders[['product_id','price','status']].copy()
    df_Qty = df_Qty.sort_values('product_id')
    df_Qty['Quantity'] = df_Qty.groupby(['product_id', 'status'])['product_id'].transform('count')
    df_Qty = df_Qty.drop_duplicates(subset = ['product_id'])

    total_Quantity_sold = df_Qty['Quantity'].sum()
    
    Av_gross_total_sales_price = Gross_sales / total_Quantity_sold
    
    return int(Av_gross_total_sales_price)

Av_Gross_salesprice = calculate_Av_Gross_salesprice(df_orders)
print(f"The average gross (total) sales price is:", Last5days_Av_Sales_Amount)


# # Determine the average sales amount for the last 5 days of sales. Note that the sales do not have to be over 5 consecutive calendar days.

# In[191]:


from datetime import datetime

def calculate_sales(df_orders):
    df_Sales = df_orders[['product_id','price','order_date']].copy()

    df_Sales = df_Sales.sort_values('product_id')

    df_Sales['Quantity'] = df_Sales.groupby(['product_id', 'order_date'])['product_id'].transform('count')

    df_Sales = df_Sales.drop_duplicates(subset = ['product_id'])

    df_Sales['Sales Amount'] = df_Sales['Quantity'] * df_Sales['price']

    df_Sales['order_date'] = pd.to_datetime(df_Sales['order_date']).dt.date

    df_Sales = df_Sales.sort_values('order_date', ascending=True)

    max_date = df_Sales['order_date'].max()
    date_5_days_ago = max_date - pd.Timedelta(days=5)

    df_last_5_days = df_Sales[df_Sales['order_date'] > date_5_days_ago]

    Last5days_Av_Sales_Amount = ((df_last_5_days['Sales Amount'].sum())/5).round(2)

    return Last5days_Av_Sales_Amount
Last5days_Av_Sales_Amount = calculate_sales(df_orders)
print(f"The average sales amount for the last 5 days of sales is:", Last5days_Av_Sales_Amount)


# In[192]:


def calculate_location_sales(df_orders):
    df_Sales = df_orders[['product_id','price','location']].copy()

    df_Sales = df_Sales.sort_values('product_id')

    df_Sales['Quantity'] = df_Sales.groupby(['product_id', 'location'])['product_id'].transform('count')

    df_Sales = df_Sales.drop_duplicates(subset = ['product_id'])

    df_Sales['Sales Amount'] = df_Sales['Quantity'] * df_Sales['price']

    df_Location_Sales = df_Sales[['location','Sales Amount']]

    Sales_bylocation = df_Location_Sales.groupby('location')['Sales Amount'].sum()

    Highest_Sales_Location = Sales_bylocation.idxmax()

    return Highest_Sales_Location

Highest_Sales_Location = calculate_location_sales(df_orders)
print(f"Location with Highest Sales:", Highest_Sales_Location)


# # In the `orders` dataset, for each `product_id`, calculate the price change (i.e., if the price of the order is increased, you can write `rise`. If the price of the order is decreased, you can write `fall`).

# In[193]:


def calculate_price_change(df_orders):
    df_orders['order_date'] = pd.to_datetime(df_orders['order_date']) 
    df_orders.sort_values(by=['product_id', 'order_date'], inplace=True)
    df_input= df_orders[['product_id','price','order_date']].copy()

    df_input['previous_price'] = df_input.groupby('product_id')['price'].shift(1)
    def price_change(row):
        if pd.isna(row['previous_price']):
            return None
        if row['price'] > row['previous_price']:
            return 'rise'
        if row['price'] < row['previous_price']:
            return 'fall'
        elif row['price'] == row['previous_price']:
            return 'None'
        return None
    df_input['Change'] = df_input.apply(price_change, axis=1)
    df_Output = df_input[['product_id','price','order_date','Change']].copy()
    return df_Output
df_Output = calculate_price_change(df_orders)
df_Output.head()


# # Which products were ordered in the same year as their release date?

# In[194]:


def process_data(df_orders, df_products):
    df_orders = df_orders.rename(columns={'product_id':'productid'})
    df_merge = pd.merge(df_orders, df_products, on='productid', how='left')
    df_release = df_merge[['order_date','productid','brandname','releasedate']].copy()
    df_release = df_release.dropna(subset=['releasedate'])
    df_release['order_year'] = pd.to_datetime(df_release['order_date']).dt.year
    
    df_release_Samedate = df_release[df_release['order_year'] == df_release['releasedate']]
    df_release_Samedate = df_release_Samedate[['order_date','productid','brandname','releasedate']].copy()
    df_release_Samedate = df_release_Samedate.drop_duplicates(subset=['productid', 'releasedate'])
    return df_release_Samedate

df_release_Samedate = process_data(df_orders, df_products)
df_release_Samedate.head()


# # Visualize the average price per release year for each location using the most suitable chart

# In[195]:


import matplotlib.pyplot as plt
df_orders = df_orders.rename(columns={'product_id':'productid'})
def plot_average_price_perlocation(df_orders, df_products):
    df_merge = pd.merge(df_orders, df_products, on='productid', how='left')
    df_Price_perrelease_year = df_merge[['location','price','releasedate']].copy()
    average_price = df_Price_perrelease_year.groupby(['location', 'releasedate'])['price'].mean().reset_index()
    average_price['releasedate'] = average_price['releasedate'].astype(int)

    locations = average_price['location'].unique()

    for location in locations:
        plt.figure(figsize=(4,3))
        average_price[average_price['location'] == location].groupby('releasedate')['price'].mean().plot(kind='bar')
        plt.title(f'Bar Chart of Average Price by Release Year for {location}')
        plt.xlabel('Release Year')
        plt.ylabel('Average Price')
        plt.show()
plot_average_price_perlocation(df_orders, df_products)


# # Visualize the distribution of weekly gross (total) sales amount. Does the distribution resemble a normal distribution?

# In[203]:


file_path = r"C:\Users\ogunb\OneDrive\Desktop\Challenge\orders.json"
df_orders = pd.read_json(file_path, lines=True)


# In[197]:


import seaborn as sns
import matplotlib.pyplot as plt

def process_sales_data(df_orders):
    df_Sales = df_orders[['product_id','price','order_date']].copy()
    df_Sales = df_Sales.sort_values('product_id')
    df_Sales['Quantity'] = df_Sales.groupby('product_id')['product_id'].transform('count')
    df_Sales = df_Sales.drop_duplicates(subset = ['product_id'])
    df_Sales['Sales_Amount'] = df_Sales['Quantity'] * df_Sales['price']

    df_Sales['order_date'] = pd.to_datetime(df_Sales['order_date'])
    df_Sales['year'] = df_Sales['order_date'].dt.isocalendar().year
    df_Sales['week_number'] = df_Sales['order_date'].dt.isocalendar().week
    df_Sales['year_week'] = df_Sales['year'].astype(str) + ' ' + 'wk' + df_Sales['week_number'].astype(str)
    df_Sales = df_Sales.sort_values('year_week', ascending=False)

    return df_Sales

def plot_weekly_gross_sales(df_Sales):
    weekly_gross_sales = df_Sales[['year_week','Sales_Amount']]
    weekly_gross_sales = df_Sales.groupby('year_week')['Sales_Amount'].sum().reset_index()

    plt.figure(figsize=(10,6))
    sns.histplot(weekly_gross_sales['Sales_Amount'], kde=True)
    plt.title('Distribution of Weekly Gross Sales Amount')
    plt.xlabel('Weekly Gross Sales Amount')
    plt.ylabel('Frequency')
    plt.show()

df_Sales = process_sales_data(df_orders)
plot_weekly_gross_sales(df_Sales)


# Does the distribution resemble a normal distribution? YES

# # Visualize gross (total) sales amount per week and highlight anomalies on the chart.

# In[198]:


from scipy.stats import zscore

def plot_weekly_gross_sales(df_Sales, nth_week=4):
    weekly_gross_sales = df_Sales[['year_week','Sales_Amount']]
    weekly_gross_sales = df_Sales.groupby('year_week')['Sales_Amount'].sum().reset_index()
    weekly_gross_sales['z_score'] = zscore(weekly_gross_sales['Sales_Amount'])

    weekly_gross_sales['anomaly'] = weekly_gross_sales['z_score'].apply(lambda x: x > 2 or x < -2)

    plt.figure(figsize=(10,6))
    plt.plot(weekly_gross_sales['year_week'], weekly_gross_sales['Sales_Amount'], color='blue')
    plt.scatter(weekly_gross_sales[weekly_gross_sales['anomaly']]['year_week'], 
                weekly_gross_sales[weekly_gross_sales['anomaly']]['Sales_Amount'], color='red')
    plt.title('Weekly Gross Sales Amount with Anomalies')
    plt.xlabel('Week')
    plt.ylabel('Gross Sales Amount')

    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(nth_week))

    plt.show()

df_Sales = process_sales_data(df_orders)
plot_weekly_gross_sales(df_Sales)


# Anomalies are represented with the red points, they are calculated using the z score 2 to -2, which measures the deviations of this points from the mean 

# In[ ]:




