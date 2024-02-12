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
    print(check.identify_month_with_highest_sales())
    # print(check.identify_best_selling_product())

    # print(check.analys_sales_data())
    # print(check.add_to_dict())
    # print(check.calculate_cumulative_sales())
    check.add_90_percent_values_column()
    # print(pd.DataFrame(check.data))
    filtered_data_1 = check.filter_by_sellings_or_and_1()

    # Print filtered data based on condition 1
    # print("Filtered data based on condition 1 (selling more than 5 or selling 0):")
    # print(filtered_data_1)

    # Print filtered data based on condition 2
    # print("\nFiltered data based on condition 2 (price above $300 and sold less than 2 times):")
    # print(check.filter_by_sellings_or_and_2())
    # mean, median, second_max = check.calculate_mean_quantity()
    # print("Mean:", mean)
    # print("Median:", median)
    # print("Second Maximum:", second_max)

    # check.bar_chart_category_sum()
    check.divide_by_2()
    print(check.data)
    # Assume `my_data` is your DataFrame containing sales data
    sales_data = SalesData(data=check.data)

    # Calculate statistics for all columns
    # all_stats = sales_data.calculate_stats()
    # print("Statistics for all columns:")
    # print(all_stats)
    #
    # # Calculate statistics for specific columns
    # specific_columns = ['Quantity', 'Price']  # Example of specific columns
    # specific_stats = sales_data.calculate_stats(columns=specific_columns)
    # print("\nStatistics for specific columns:")
    # print(specific_stats)
    # result = check.random_value("Teilim")
    # print("Random value:", result[0])
    # print("Total units ordered for", "Teilim" + ":", result[1])
    # print("Maximum total amount for an order:", result[2])
    # param1 = 10
    # param2 = {"tag": "NAME", "VALUE": "John"}
    # param3 = "Hello"
    # param4 = {"tag": "AGE", "VALUE": 25}
    # param5 = 42
    #
    # result = check.process_params(param1, param2, param3, param4, param5)
    # print("Resulting dictionary:", result)
    # print(check.data.head(3))  # הצגת שלוש שורות ראשונות
    # print(check.data.tail(2))  # הצגת שתי שורות אחרונות
    # print(check.data.sample(1))  # הצגת שורה אקראית
    check.data.map(check.print_numeric_value)