import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def track_feature_df(track_feature_dict):
    return pd.DataFrame.from_dict(track_feature_dict,orient = 'index')

# Used seaborn documentation to generate a heatmap
def df_heatmap(df):
    # Compute the correlation matrix
    df_corr = df.corr()
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(df_corr, dtype = bool))
    # Create a figure
    f, ax = plt.subplots(figsize=(11,9))
    # custome colormap
    cmap = sns.diverging_palette(230,20,as_cmap= True)
    sns.heatmap(df_corr, mask = mask, cmap = cmap, vmax = .3, center = 0, square = True,
                linewidths = .5, cbar_kws={"shrink":.5})
    plt.show()

# Seaborn for pairplot
def df_pairplot(df):
    # since all of our data are numerical, there is no need for a hue
    sns.pairplot(df)
    plt.show()
