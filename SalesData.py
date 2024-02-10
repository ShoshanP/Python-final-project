import pandas as pd
import numpy as np

class SalesData:
    def __init__(self, data):
        self.data = data

    def eliminate_duplicates(self):
        self.data.drop_duplicates(inplace=True)

    def calculate_total_sales(self):
        total_sales = self.data.groupby('Product')['Quantity'].sum().reset_index()

        #  .reset_index()

        return total_sales

    def identify_best_selling_product(self):
        return self.calculate_total_sales().sort_values(by='Quantity', ascending=False).head(1)

    def calculate_total_sales_per_month(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%d.%m.%Y')

        total_sales = self.data.groupby(self.data['Date'].dt.strftime('%B'))['Quantity'].sum().reset_index()
        return total_sales



    def identify_month_with_highest_sales(self):
        return self.calculate_total_sales_per_month().sort_values(by='Quantity', ascending=False).head(1)

    def analys_sales_data(self):
        return {
            'best_selling_product': self.identify_best_selling_product(),
            'month_with_highest_sales': self.identify_month_with_highest_sales()
        }
    def add_to_dict(self):
        tmp = self.analys_sales_data()
        tmp.update({'minimest selling': self.calculate_total_sales_per_month()\
            .sort_values(by='Quantity').head(1),
                    'avg_sales_by_month': self.calculate_total_sales_per_month()['Quantity'].mean()})
        return tmp

    def calculate_cumulative_sales(self):
        # Convert 'Date' column to datetime format
        self.data['Date'] = pd.to_datetime(self.data['Date'], format="%d.%m.%Y")

        # Create a new DataFrame with the cumulative sum of sales for each product across months
        cumulative_sales = self.data.pivot_table(index='Product', columns=self.data['Date'].dt.month, values='Total',
                                                 aggfunc=np.sum, fill_value=0)

        return cumulative_sales

    def add_90_percent_values_column(self):
        # Assuming self.data is a numpy array where each row represents a sale
        # and the last column contains the sale values
        # sale_values = self.data[:, -1]  # Extracting sale values from the last column
        ninety_percent_values = self.data['Total'] * 0.9  # Calculating 90% of the sale values
        self.data = np.column_stack((self.data, ninety_percent_values))  # Adding a new column with 90% values

    def filter_by_sellings_or_and_1(self):
        quantities = self.data[:, 4].astype(int)  # Assuming the quantity column is at index 1
        filtered_products = self.data[(quantities > 5) | (quantities == 0)]  # Assuming the product column is at index 0
        return filtered_products

    def filter_by_sellings_or_and_2(self):
        quantities = self.data[:, 4].astype(int)  # Assuming the quantity column is at index 1
        prices = self.data[:, 3].astype(int)  # Assuming the quantity column is at index 1
        filtered_products = self.data[(prices > 300) & (quantities <= 2)]  # Assuming the product column is at index 0
        return filtered_products
