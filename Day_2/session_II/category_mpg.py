def get_cars(ser):
    return list(ser)

df_mpg.groupby(by=["model_year","origin"]).agg(
    sale_number = ("origin","count"),
    lst_cars=("name",get_cars)
).reset_index().groupby(["model_year"])["sale_number"].last()#.sort_values(by=["model_year","sale_number"],ascending=[True,False])