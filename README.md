# Olympics Analysis Application

## Project Overview

This project is a web-based interactive dashboard application built using **Streamlit** to analyze Olympic data. The dataset includes historical data of athletes from various Olympic events, combined with region-wise data. Users can explore different analyses such as medal tallies, country-wise performance, athlete-specific data, and more.

## Features

1. **Medal Tally**: 
   - View medal tallies for specific countries and Olympic years.
   - Filter data by country and year to see both overall and specific results.
![Screenshot from 2024-09-18 14-51-43](https://github.com/user-attachments/assets/b79ea66a-7b98-436f-9f95-a849cf1a608e)

2. **Overall Analysis**: 
   - Display various statistics such as the number of editions, host cities, sports, events, nations, and athletes.
   - Visualizations showing how countries, events, and athlete participation have evolved over the years.
   - Heatmap visualization for events across different sports.
![Screenshot from 2024-09-18 14-52-17](https://github.com/user-attachments/assets/08187b9a-b6e7-4636-b51a-6865a582703e)

3. **Country-wise Analysis**:
   - Detailed breakdown of a selected country’s performance over the years.
   - Heatmap of country performance in different sports.
   - Top 10 athletes from the selected country.
![Screenshot from 2024-09-18 14-57-42](https://github.com/user-attachments/assets/1c9bdd88-e4c6-48d0-bc1f-7c86508eedb2)
![Screenshot from 2024-09-18 14-59-18](https://github.com/user-attachments/assets/4843245d-0e12-4aed-9fd5-adf222de4b29)
![Screenshot from 2024-09-18 14-59-32](https://github.com/user-attachments/assets/7026fc5a-628e-4a84-8bab-d9c614c443e6)



4. **Athlete-wise Analysis**:
   - Distribution of athlete ages based on medal achievements (Gold, Silver, Bronze).
   - Scatter plot analysis of athletes' height vs. weight based on sport and gender.
   - Visualizing the participation trends of men and women athletes over the years.
![Screenshot from 2024-09-18 14-59-53](https://github.com/user-attachments/assets/c7dcf833-0a47-494c-b4b4-2c4d62dd7b56)
![Screenshot from 2024-09-18 15-00-05](https://github.com/user-attachments/assets/081159a4-ccd7-4195-89ea-d82c120f6e4b)
![Screenshot from 2024-09-18 15-00-14](https://github.com/user-attachments/assets/017c4198-f4f4-49e0-8be8-73411867b5c0)



## Main Libraries

The main libraries used in the project include:

- **Streamlit**: For creating the web interface.
- **Pandas**: For data manipulation.
- **Plotly**: For interactive visualizations.
- **Matplotlib** and **Seaborn**: For static visualizations.
- **Scipy**: For statistical computations.

### Custom Modules:
- **preprocessor**: Preprocessing the dataset.
- **helper**: Contains utility functions for data retrieval and processing.

## Credits

This project was inspired by a tutorial video. Special thanks to the creator of the following YouTube video for providing guidance on building an Olympics analysis application:

- [YouTube Tutorial](https://youtu.be/5nQXhusiu7s?si=Ts5tsjGGJet6p_Ro)
