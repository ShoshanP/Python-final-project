from FileOperation import FileOperation
from SalesData import SalesData
import pandas as pd

if __name__ == '__main__':
    sales_data_analyzer = FileOperation(data=None)

    # Read data from an Excel file
    sales_data_analyzer.read_excel("YafeNof.csv")

    # print(sales_data_analyzer.data)

    df = sales_data_analyzer.data
    check = SalesData(data=df)

    check.eliminate_duplicates()
    # print(check.calculate_total_sales())
    # print(check.calculate_total_sales_per_month())
    # print(check.identify_month_with_highest_sales())
    # print(check.identify_best_selling_product())

    # print(check.analys_sales_data())
    # print(check.add_to_dict())
    # print(check.calculate_cumulative_sales())
    check.add_90_percent_values_column()
    # print(pd.DataFrame(check.data))
    filtered_data_1 = check.filter_by_sellings_or_and_1()

    # Print filtered data based on condition 1
    print("Filtered data based on condition 1 (selling more than 5 or selling 0):")
    print(filtered_data_1)

    # Print filtered data based on condition 2
    print("\nFiltered data based on condition 2 (price above $300 and sold less than 2 times):")
    print(check.filter_by_sellings_or_and_2())