import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    """
    The DataVisualizer class provides functions to create various visualizations for the given DataFrame.
    """

    def __init__(self, dataframe):
        self.df = dataframe

    def plot_passenger_count_over_time(self):
       plt.figure(figsize=(12, 6))
       sns.lineplot(data=self.df, x='Activity Period', y='Passenger Count')
       plt.title('Passenger Count Over Time')
       plt.xlabel('Date')
       plt.ylabel('Passenger Count')
       plt.xticks(rotation=45)
       plt.tight_layout()
       plt.show()


    def plot_passenger_count_by_airline(self, top_n=10):
    # """
    # This function plots a bar chart showing total passenger count by airline.
    # Limiting to top N airlines for clarity.
    # """
      airline_passenger_counts = self.df.groupby('Operating Airline')['Passenger Count'].sum().reset_index()
      top_airlines = airline_passenger_counts.nlargest(top_n, 'Passenger Count')  # Top N airlines by passenger count

      plt.figure(figsize=(12, 6))
      sns.barplot(data=top_airlines, x='Operating Airline', y='Passenger Count')
      plt.title(f'Total Passenger Count by Airline (Top {top_n} Airlines)')
      plt.xlabel('Operating Airline')
      plt.ylabel('Total Passenger Count')
      plt.xticks(rotation=45)
      plt.tight_layout()
      plt.show()


    def plot_monthly_traffic_trend(self):
       monthly_traffic = self.df.groupby(['Year', 'Month'])['Passenger Count'].sum().reset_index()
       plt.figure(figsize=(12, 6))
       sns.lineplot(data=monthly_traffic, x='Month', y='Passenger Count', hue='Year', marker='o')
       plt.title('Monthly Traffic Trend')
       plt.xlabel('Month')
       plt.ylabel('Total Passenger Count')
       plt.tight_layout()
       plt.show()


    def plot_year_month_heatmap(self):
    # """
    # This function creates a heatmap for traffic by Year and Month.
    # """
      traffic_pivot = self.df.pivot_table(index='Year', columns='Month', values='Passenger Count', aggfunc='sum')
      plt.figure(figsize=(14, 8))
      sns.heatmap(traffic_pivot, annot=True, cmap='YlGnBu', fmt='g', linewidths=0.5, annot_kws={"size": 10})
      plt.title('Yearly Traffic Heatmap by Month')
      plt.xlabel('Month')
      plt.ylabel('Year')
      plt.tight_layout()
      plt.show()


