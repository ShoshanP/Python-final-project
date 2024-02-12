import datetime
import sys

import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt
from fontTools.merge.util import current_time


class SalesData:
    def __init__(self, data):
        """
        Initialize the SalesData object.

        Args:
        - data: DataFrame containing sales data.
        """
        self.data = data

    def eliminate_duplicates(self):
        """
        Remove duplicate rows from the sales data.
        """
        try:
            self.data.drop_duplicates(inplace=True)
        except Exception as e:
            print(f"<Shoshi&Racheli&Zippi, {datetime.date.today()}, {current_time}> An error occurred while calculating total sales: {e} <Shoshi&Racheli&Zippi>")

    def calculate_total_sales(self):
        """
        Calculate total sales for each product.

        Returns:
        DataFrame: Total sales for each product.
        """
        try:
            total_sales = self.data.groupby('Product')['Quantity'].sum().reset_index()
            return total_sales
        except Exception as e:
            print(f"<Shoshi&Racheli&Zippi, {datetime.date.today()}, {current_time}> An error occurred while calculating total sales: {e} <Shoshi&Racheli&Zippi>")
            return None

    def identify_best_selling_product(self):
        """
        Identify the best-selling product.

        Returns:
        DataFrame: Information about the best-selling product.
        """
        try:
            return self.calculate_total_sales().sort_values(by='Quantity', ascending=False).head(1)
        except Exception as e:
            print(f"<Shoshi&Racheli&Zippi, {datetime.date.today()}, {current_time}> An error occurred while calculating total sales: {e} <Shoshi&Racheli&Zippi>")
            return None

    def calculate_total_sales_per_month(self):
        """
        Calculate total sales for each month.

        Returns:
        DataFrame: Total sales for each month.
        """
        try:
            self.data['Date'] = pd.to_datetime(self.data['Date'], format='%d.%m.%Y')
            total_sales = self.data.groupby(self.data['Date'].dt.strftime('%B'))['Quantity'].sum().reset_index()
            return total_sales
        except Exception as e:
            print(f"<Shoshi&Racheli&Zippi, {datetime.date.today()}, {current_time}> An error occurred while calculating total sales: {e} <Shoshi&Racheli&Zippi>")
            return None

    def identify_month_with_highest_sales(self):
        """
        Identify the month with the highest sales.

        Returns:
        DataFrame: Information about the month with the highest sales.
        """
        try:
            return self.calculate_total_sales_per_month().sort_values(by='Quantity', ascending=False).head(1)
        except Exception as e:
            print(f"<Shoshi&Racheli&Zippi, {datetime.date.today()}, {current_time}> An error occurred while calculating total sales: {e} <Shoshi&Racheli&Zippi>")
            return None

    def analys_sales_data(self):
        """
        Analyze sales data.

        Returns:
        dict: Dictionary containing analysis results.
        """
        try:
            return {
                'best_selling_product': self.identify_best_selling_product(),
                'month_with_highest_sales': self.identify_month_with_highest_sales()
            }
        except Exception as e:
            print("An error occurred while analyzing sales data:", e)
            return None

    def add_to_dict(self):
        """
        Add additional analysis results to the analysis dictionary.

        Returns:
        dict: Dictionary containing extended analysis results.
        """
        try:
            tmp = self.analys_sales_data()
            tmp.update({'minimest selling': self.calculate_total_sales_per_month()\
                .sort_values(by='Quantity').head(1),
                        'avg_sales_by_month': self.calculate_total_sales_per_month()['Quantity'].mean()})
            return tmp
        except Exception as e:
            print("An error occurred while adding to dictionary:", e)
            return None

    def calculate_cumulative_sales(self):
        """
        Calculate cumulative sales for each product across months.

        Returns:
        DataFrame: Cumulative sales for each product.
        """
        try:
            self.data['Date'] = pd.to_datetime(self.data['Date'], format="%d.%m.%Y")
            cumulative_sales = self.data.pivot_table(index='Product', columns=self.data['Date'].dt.month, values='Total',
                                                     aggfunc=np.sum, fill_value=0)
            return cumulative_sales
        except Exception as e:
            print("An error occurred while calculating cumulative sales:", e)
            return None

    def add_90_percent_values_column(self):
        """
        Add a column with 90% values to the sales data.
        """
        try:
            ninety_percent_values = self.data['Total'] * 0.9
            self.data['90%_Values'] = ninety_percent_values
        except Exception as e:
            print("An error occurred while adding 90% values column:", e)

    def calculate_mean_quantity(self):
        """
        Calculate mean, median, and second maximum quantity.

        Returns:
        tuple: Mean, median, and second maximum quantity.
        """
        try:
            total_column = self.data[:, 5].astype(int)
            mean = np.mean(total_column)
            median = np.median(total_column)
            second_max = np.partition(total_column, -2)[-2]  # Second maximum
            return mean, median, second_max
        except Exception as e:
            print("An error occurred while calculating mean quantity:", e)
            return None, None, None

    def filter_by_sellings_or_and_1(self):
        """
        Filter data based on quantity criteria.

        Returns:
        DataFrame: Filtered data.
        """
        try:
            quantities = self.data[:, 4].astype(int)
            filtered_products = self.data[(quantities > 5) | (quantities == 0)]
            return filtered_products
        except Exception as e:
            print("An error occurred while filtering by sellings or and 1:", e)
            return None

    def filter_by_sellings_or_and_2(self):
        """
        Filter data based on quantity and price criteria.

        Returns:
        DataFrame: Filtered data.
        """
        try:
            quantities = self.data[:, 4].astype(int)
            prices = self.data[:, 3].astype(int)
            filtered_products = self.data[(prices > 300) & (quantities <= 2)]
            return filtered_products
        except Exception as e:
            print("An error occurred while filtering by sellings or and 2:", e)
            return None

    def bar_chart_category_sum(self):
        """
        Generate a bar chart showing total quantity sold for each product.
        """
        try:
            sns.set(style="whitegrid")
            plt.figure(figsize=(12, 6))
            sns.barplot(x="Product", y="Quantity", data=self.calculate_total_sales())
            plt.title('Total Quantity Sold for Each Product')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print("An error occurred while generating bar chart:", e)

    def divide_by_2(self):
        five_percent = self.data['Price'] * 0.5
        self.data['BlackFridayPrice'] = five_percent

    def calculate_stats(self, columns: str = None):
        """
        Calculate statistics for the SalesData DataFrame.

        Args:
        - columns (str): Columns for which to calculate statistics. If None, calculate for all columns.

        Returns:
        dict: Dictionary containing statistics for each column.
        """
        try:
            if columns is None:
                columns = self.data.columns  # If no specific columns provided, calculate for all columns

            stats = {}  # Dictionary to store statistics for each column
            for col in columns:
                if self.data[col].dtype != 'object':  # Exclude non-numeric columns
                    col_stats = {}  # Dictionary to store statistics for the current column

                    # Calculate statistics
                    col_stats['max'] = self.data[col].max()
                    col_stats['sum'] = self.data[col].sum()
                    col_stats['absolute_values'] = self.data[col].abs().sum()
                    col_stats['cumulative_max'] = self.data[col].cummax().max()

                    stats[col] = col_stats  # Store statistics for the current column

            return stats
        except Exception as e:
            print("An error occurred while calculating statistics:", e)
            return None

    import pandas as pd
    import numpy as np

    def random_value(self,product_name):
        # סכום היחידות שהוזמנו מהמוצר הרצוי
        total_units_ordered = self.data.loc[self.data['Product'] == product_name, 'Quantity'].sum()

        # הסכום המקסימלי ששולם עבור הזמנה כלשהי
        max_total_amount = self.data['Total'].max()

        # יצירת ערך רנדומלי בין סכום היחידות לסכום המקסימלי
        random_value = np.random.randint(total_units_ordered, max_total_amount + 1)

        # אחסון הערך הרנדומלי והטווח ממנו הוגרל במערך
        result_array = [random_value, total_units_ordered, max_total_amount]

        print("Python version:", sys.version)
        return result_array

    def process_params(*args):
        result_dict = {}
        for arg in args:
            if isinstance(arg, dict):
                if "tag" in arg:
                    result_dict[arg["tag"]] = arg["VALUE"]
            else:
                print(arg)
        return result_dict

    def print_numeric_value(self,value):
        if pd.api.types.is_numeric_dtype(type(value)):
            print(value)






