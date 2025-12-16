
import DataAnalysisProject as dt

data=dt.CustomerChurnAnalysis(r"Telco_Cusomer_Churn.csv")
data.load_data()
data.inspect_data()
data.data_cleaning()
data.data_statistics()
data.group_and_filter_data()
data.plot_data()

