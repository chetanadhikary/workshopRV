df_sales.groupby(by= ["sale_year","store_id"]).agg(
    highest_sale = ("sale_amount","max"),
    sales_man = ("associate","first")
).reset_index().sort_values("highest_sale",ascending = False).head(10)