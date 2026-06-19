def apply_filters(df, species_list):
    if species_list:
        df = df[df["species"].isin(species_list)]
    return df