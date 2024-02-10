# This is a sample Python script.
from FileOperation import FileOperation
from SalesData import SalesData



if __name__ == '__main__':
    sales_data_analyzer = FileOperation(data=None)

    # Read data from an Excel file
    sales_data_analyzer.read_excel("YafeNof.csv")

    print(sales_data_analyzer.data)

    df = sales_data_analyzer.data

    sales_data_analyzer.save_to_excel(df, "new.csv")

    df = sales_data_analyzer.data
    check = SalesData(data=df)

    check.eliminate_duplicates()
    # print(check.calculate_total_sales())
    # print(check.calculate_total_sales_per_month())
    # print(check.identify_month_with_highest_sales())
    # print(check.identify_best_selling_product())

    # print(check.analys_sales_data())
    print(check.add_to_dict())



    # Perform analysis


    # Print analysis results
    print("Analysis results:")

    # Save data to CSV

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
