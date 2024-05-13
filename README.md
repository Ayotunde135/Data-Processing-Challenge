# Data-Processing-Challenge
This challenge is designed to evaluate your proficiency in sourcing, transforming, and querying data.

## Tasks
Given two JSON files, one containing data for "products" and the other for "orders," your objective is to create functions to solve the following tasks:

1. Calculate the net sales amount. Note that there are three order statuses: created, cancelled, and returned.

1. Calculate the average net sales price.

1. Calculate the gross (total) sales amount.

1. Calculate the average gross (total) sales price.

1. Determine the average sales amount for the last 5 days of sales. Note that the sales do not have to be over 5 consecutive calendar days.

1. Identify the location with the highest sales.

1. In the `orders` dataset, for each `product_id`, calculate the price change (i.e., if the price of the order is increased, you can write `rise`. If the price of the order is decreased, you can write `fall`).

    Sample Input:
    ```
    +--------+------+-------------------+
    |prod_id |price |order_date         |
    +--------+------+-------------------+
    |<id-1>  |3.00  |2021-01-22 01:20:32|
    |<id-1>  |3.00  |2021-01-22 02:50:20|
    |<id-1>  |3.25  |2021-01-22 03:45:10|
    |<id-2>  |3.25  |2021-01-22 13:45:10|
    |<id-2>  |3.25  |2021-01-22 14:45:10|
    |<id-2>  |3.45  |2021-01-22 15:45:10|
    |<id-1>  |3.25  |2021-01-22 04:57:24|
    |<id-1>  |2.99  |2021-01-22 05:44:47|
    |<id-1>  |2.99  |2021-01-22 06:34:43|
    |<id-1>  |3.50  |2021-01-22 07:05:29|
    +--------+------+-------------------+
    ```

    Sample Output:
    ```
    +--------+------+-------------------+--------+
    |prod_id |price |order_date         |change  |
    +--------+------+-------------------+--------+
    |<id-1>  |3.25  |2021-01-22 03:45:10|rise    |
    |<id-1>  |2.99  |2021-01-22 05:44:47|fall    |
    |<id-1>  |3.50  |2021-01-22 07:05:29|rise    |
    |<id-2>  |3.45  |2021-01-22 15:45:10|fall    |
    +--------+------+-------------------+--------+
    ```

1. Which products were ordered in the same year as their release date?

1. Visualize the average price per release year for each location using the most suitable chart.

1. Visualize the distribution of weekly gross (total) sales amount. Does the distribution resemble a normal distribution?

1. Visualize gross (total) sales amount per week and highlight anomalies on the chart.

