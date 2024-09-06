def expand_dict_column(df, column_name):
    # Rozszerzamy słowniki na osobne kolumny
    expanded_df = df[column_name].apply(pd.Series)
    # Renomujemy kolumny, aby uwzględnić nazwę kolumny bazowej
    expanded_df.columns = [f"{column_name}.{col}" for col in expanded_df.columns]
    return expanded_df

# Rozszerzamy kolumny block1 i block2
expanded_block1 = expand_dict_column(df, 'block1')
expanded_block2 = expand_dict_column(df, 'block2')

# Łączymy z powrotem z oryginalnym DataFrame
df_expanded = pd.concat([df, expanded_block1, expanded_block2], axis=1)

# Usuwamy kolumny z oryginalnymi słownikami (opcjonalne)
df_expanded = df_expanded.drop(columns=['block1', 'block2'])
