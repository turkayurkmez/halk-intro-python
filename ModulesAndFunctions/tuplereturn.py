import math
def employee_performance(sales):
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    max_sale = max(sales)
    min_sale = min(sales)
    count = len(sales)

    return (total_sales,average_sales,max_sale,min_sale,count)