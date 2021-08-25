import matplotlib.pyplot as plt

# GRAPHS
# missing value
def missing_value_colors(values, tot):
    clrs = []
    for x in values:
        x_perc = (x / tot) * 100
        if (x_perc <= 75):
            clrs.append('g')  # green when missing value < 75%
        elif (x_perc > 75) and (x_perc <= 85):
            clrs.append('y')
        else:
            clrs.append('r')
    return clrs


def missing_value_graphs(dataframe_missing_value, original_df, title):
    # variable
    tot_values = original_df.shape[0]
    print(tot_values)
    values = dataframe_missing_value.values
    row_index = dataframe_missing_value.index
    start = 0
    for i in range(2, 0, -1):
        end = int(len(row_index) / i)
        title_str = f'{title} valori mancanti  da {row_index[start]} a {row_index[end - 1]}'
        # graphs
        fig, ax = plt.subplots(figsize=(10, 12))
        colors = missing_value_colors(values, tot_values)
        ax.barh(row_index[start:end], values[start:end], color=colors[start:end])  # Horizontal Bar Plot
        ax.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.2)  # Add x, y gridlines
        for i in ax.patches:
            plt.text(i.get_width() + 0.2, i.get_y() + 0.5, str(round(((i.get_width() / tot_values) * 100), 2)) + '%',
                     fontsize=10, fontweight='bold', color='grey')  # Add annotation to bars
        ax.invert_yaxis()  # Show top values
        # labeling
        plt.xlabel("Valori mancanti")
        plt.ylabel("Caratteristiche")
        plt.title(title_str)
        plt.show()  # show the graphs
        start = end