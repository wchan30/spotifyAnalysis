**Introduction**

In the world of music, some new songs rise to the top of the charts. But what makes it so popular and trendy? Do these tracks share similar characteristics, or are they unique in their own ways? This project aims to explore if there are any underlying correlations between audio features of the top popular songs on Spotify.

**Objective**

For this project, the top 10 songs from Spotify's Top 50 playlist will be extracted and analyzed their audio features. By examining the correlations between these features, we can determine if there are any correlation that might explain the popularity amongst the songs.

**Methodology**

Data on the top 10 songs were extracted from Spotify's API, as well as audio features. Such features are tempo, danceability, engergy, etc. A correlation analysis was then conducted to explore any correlation between those features

**Data Collection**

In order to use the Spotify's API, authorization was required. Linking a spotify account will grant a client_id and client_secret. A token will be needed whenever the user needs to access a given resource. User can rely on the Spotify's API documentation for more information.

**Data Analysis**

After collecting the data and shaping it into a pandas dataframe, a correlation anaylsis was performed. For visualization, a heatmap and pairplot were created using seaborn.

**Results**

There was a weak correlation across features. This could potentially mean that the genres of the songs were different. There were mild positive correlation between energy and loudness, but that is expected.

**Conclusion**

Since there is a weak correlation across features, do Spotify user's listen to the song just to support their artists?



