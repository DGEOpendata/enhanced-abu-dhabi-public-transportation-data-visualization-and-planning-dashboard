## Enhanced Abu Dhabi Public Transportation Data Visualization and Planning Dashboard

### Overview
This project provides an interactive dashboard for analyzing public transportation data in Abu Dhabi. The dashboard is designed to help urban planners optimize routes, enable commuters to plan their journeys, and assist researchers and transport authorities in assessing and improving public transportation services.

### Features
- Interactive dropdown menu to select specific bus routes.
- Line graphs showing ridership trends over time.
- Bar charts displaying average wait times per route.
- Filtering feature to customize data visualization.
- Real-time data updates (if integrated with a live data source).

### Requirements
- Python 3.7+
- Libraries: `pandas`, `dash`, `plotly`  
  To install dependencies, run:  
  bash
  pip install pandas dash plotly
  

### Dataset
The dataset should follow the structure mentioned below:
- **Route_ID**: Unique identifier for each bus route.
- **Date**: Date of data collection.
- **Ridership**: Number of passengers.
- **Average_Wait_Time**: Average wait time in minutes.

Save the dataset as a CSV file named `Abu_Dhabi_Public_Transportation_Metrics.csv` in the same directory as the script.

### How to Run
1. Clone this repository.
2. Install the required Python libraries.
3. Place the dataset in the project directory.
4. Run the script using the command:
   bash
   python app.py
   
5. Open your browser and navigate to `http://127.0.0.1:8050/` to interact with the dashboard.

### How to Use
1. Select a bus route from the dropdown menu.
2. View the ridership trends over time in the line graph.
3. Analyze average wait times for the selected route in the bar chart.

### Extending the Dashboard
- Additional features such as heatmaps for service coverage or pie charts for ridership distribution can be incorporated.
- Authentication mechanisms can be added to restrict access to authorized users.
- The dashboard can be integrated with a real-time API to fetch live transportation data.

### Support
For any issues or queries, please open an issue in this repository or contact the project maintainer.

### License
This project is licensed under the MIT License.