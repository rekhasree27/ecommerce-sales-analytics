import pandas as pd
import os

folder = r"C:\Users\nothing\Downloads\archive"

orders   = pd.read_csv(os.path.join(folder, "olist_orders_dataset.csv"))
items    = pd.read_csv(os.path.join(folder, "olist_order_items_dataset.csv"))
products = pd.read_csv(os.path.join(folder, "olist_products_dataset.csv"))
customers= pd.read_csv(os.path.join(folder, "olist_customers_dataset.csv"))
payments = pd.read_csv(os.path.join(folder, "olist_order_payments_dataset.csv"))
reviews  = pd.read_csv(os.path.join(folder, "olist_order_reviews_dataset.csv"))

print("✅ All tables loaded!")

# Q1 - Monthly Revenue
q1 = orders.merge(payments, on='order_id')
q1 = q1[q1['order_status']=='delivered']
q1['month'] = pd.to_datetime(q1['order_purchase_timestamp']).dt.strftime('%Y-%m')
q1 = q1.groupby('month').agg(total_revenue=('payment_value','sum'), total_orders=('order_id','nunique')).round(2).reset_index()
q1.to_csv(os.path.join(folder, "monthly_revenue.csv"), index=False)
print("✅ Saved monthly_revenue.csv")

# Q2 - Top Categories
q2 = items.merge(products, on='product_id')
q2 = q2.groupby('product_category_name').agg(revenue=('price','sum'), total_orders=('order_id','count')).round(2).reset_index()
q2 = q2.sort_values('revenue', ascending=False).head(10)
q2.to_csv(os.path.join(folder, "top_categories.csv"), index=False)
print("✅ Saved top_categories.csv")

# Q3 - Revenue by State
q3 = orders.merge(customers, on='customer_id').merge(payments, on='order_id')
q3 = q3.groupby('customer_state').agg(avg_order_value=('payment_value','mean'), total_orders=('order_id','nunique')).round(2).reset_index()
q3 = q3.sort_values('avg_order_value', ascending=False)
q3.to_csv(os.path.join(folder, "revenue_by_state.csv"), index=False)
print("✅ Saved revenue_by_state.csv")

# Q4 - Cancellation Rate
orders['month'] = pd.to_datetime(orders['order_purchase_timestamp']).dt.strftime('%Y-%m')
q4 = orders.groupby('month').apply(lambda x: pd.Series({
    'cancelled_orders': (x['order_status']=='canceled').sum(),
    'total_orders': len(x),
    'cancel_rate_pct': round((x['order_status']=='canceled').sum()*100.0/len(x), 2)
})).reset_index()
q4.to_csv(os.path.join(folder, "cancellation_rate.csv"), index=False)
print("✅ Saved cancellation_rate.csv")

# Q5 - Customer Retention
q5 = orders.merge(customers, on='customer_id')
q5 = q5.groupby('customer_unique_id')['order_id'].nunique().reset_index()
q5['customer_type'] = q5['order_id'].apply(lambda x: 'Repeat Buyer' if x > 1 else 'One-Time Buyer')
q5 = q5.groupby('customer_type').size().reset_index(name='total_customers')
q5['percentage'] = (q5['total_customers']*100.0/q5['total_customers'].sum()).round(2)
q5.to_csv(os.path.join(folder, "customer_retention.csv"), index=False)
print("✅ Saved customer_retention.csv")

# Q6 - Delivery vs Reviews
q6 = orders.merge(reviews, on='order_id')
q6 = q6[q6['order_delivered_customer_date'].notna()]
q6['delivery_days'] = (pd.to_datetime(q6['order_delivered_customer_date']) - pd.to_datetime(q6['order_purchase_timestamp'])).dt.days
q6 = q6.groupby('review_score').agg(total_orders=('order_id','count'), avg_delivery_days=('delivery_days','mean')).round(1).reset_index()
q6 = q6.sort_values('review_score', ascending=False)
q6.to_csv(os.path.join(folder, "delivery_vs_reviews.csv"), index=False)
print("✅ Saved delivery_vs_reviews.csv")

# Q7 - Payment Types
q7 = payments.groupby('payment_type').agg(total_orders=('order_id','nunique'), total_revenue=('payment_value','sum'), avg_order_value=('payment_value','mean')).round(2).reset_index()
q7 = q7.sort_values('total_revenue', ascending=False)
q7.to_csv(os.path.join(folder, "payment_types.csv"), index=False)
print("✅ Saved payment_types.csv")

# Q8 - Top Revenue Months
q8 = orders.merge(payments, on='order_id')
q8['month'] = pd.to_datetime(q8['order_purchase_timestamp']).dt.strftime('%Y-%m')
q8 = q8.groupby('month').agg(total_revenue=('payment_value','sum'), total_orders=('order_id','nunique'), avg_order_value=('payment_value','mean')).round(2).reset_index()
q8 = q8.sort_values('total_revenue', ascending=False).head(10)
q8.to_csv(os.path.join(folder, "top_revenue_months.csv"), index=False)
print("✅ Saved top_revenue_months.csv")

print("\n🎉 All 8 CSVs exported successfully!")