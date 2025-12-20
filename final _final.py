# -----------------------------------------------------------------
# Digital Skills & Python Programming Final Project
# -----------------------------------------------------------------
# Team Members :
"""
    *** FATIMA ZAHRA EL HALFI ***
    *** AYA DOUBIANI ***
    *** IKRAM BEN AYA ***
    *** OUMAIMA SAID ***
    *** FATIMA ZAHRA EL-BOURIMI ***
"""

# import needed modules in this project
import pandas as pd
import matplotlib.pyplot as plt


# Build a class that will contain all methods to apply on dataset (load, analyze, plot )
class CustomerChurnAnalysis:
    def __init__(self, file_path):
        # constructor : initializes the class with the path to the dataset file
        # It stores the file's path to use it later in the class methods
        self.file_path = file_path
        # It creates an attribute called df (DataFrame) and sets it to empty at the beginning
        self.df = None

    # --------------------------------------------------
    # 1. Load Dataset : read the csv file containing the dataset for analysis and handle exceptions
    # --------------------------------------------------
    def load_data(self):
        """Load the data set from a csv file """
        try:
            # Read the csv file into a Data Frame for analysis
            self.df = pd.read_csv(self.file_path)
            print("File loaded successfully . ")
        except FileNotFoundError:
            # Error raised when the file does not exist
            print("File not found . ")
        except PermissionError:
            # Error raised when the user has no permission to open the file
            print("You don't have permission to access this file . ")
        except Exception as e:
            # Error raised when something went wrong while loading the csv file
            print(f"Something went wrong while loading the file : {e} ")

    # ------------------------------------------------
    # 2-Inspect DataSet : General information about dataset (numbers of rows , cols ,missing values and some statistic methods  )
    # ------------------------------------------------
    def inspect_data(self):
        """Inspect the data set
        Displays dataset information , missing values
        and basic statistics """
        # Check if the data set is well loaded , if not it run out of the method to not cause errors
        if self.df is None:
            print("Dataset not loaded . ")
            return  # To stop the function

        # summary of the dataframe with data types and missing values
        print("\nDataset Information ******************** ")
        print(self.df.info())

        # Display the first 10 rows
        print("\nFirst 10 rows : ")
        print(self.df.head(10))

        # Display the last 10 rows
        print("\nLast 10 rows : ")
        print(self.df.tail(10))

        # Display the dataset's shape : tuple containing number of rows and columns
        print("\nDataset's size is : ")
        print(self.df.shape)

        # List of columns along with data types
        print("\nDataset columns and datatypes : ")
        print(self.df.dtypes)

        # Provide basic statistical information about numerical columns
        print("\nDataset Description :")
        print(self.df.describe())

        # Identify and report missing values in each column
        print("\nMissing values in each column : ")
        # Cheks for Na values (empty or NULL values ) then sum the total number of missing values per column
        print(self.df.isnull().sum())

    # ----------------------------------------------------------------------------------------
    # 3-cleaning data: handling missing data,duplicate values and invalid entries
    # ----------------------------------------------------------------------------------------
    def data_cleaning(self):
        """Clean the dataset; remove rows with missing values,
        remove duplicate rows,fix data of wrong format"""

        # remove rows with missing values, apply changes to the original dataframe
        self.df.dropna(inplace=True)
        # remove duplicate rows
        self.df = self.df.drop_duplicates()
        # to reorder the index after dropping duplicate rows
        self.df = self.df.reset_index(drop=True)

        # convert tenure to numeric,coercing errors to NaN
        self.df['tenure'] = pd.to_numeric(self.df['tenure'], errors='coerce')
        # dropping rows where tenure is NaN
        self.df.dropna(subset=['tenure'], inplace=True)
        self.df = self.df.reset_index(drop=True)  # reorder the index after dropping

        # convert MonthlyCharges to numeric,coercing errors to NaN
        self.df['MonthlyCharges'] = pd.to_numeric(self.df['MonthlyCharges'], errors='coerce')
        self.df.dropna(subset=['MonthlyCharges'], inplace=True)  # dropping rows where monthly charges are NaN
        self.df = self.df.reset_index(drop=True)  # reset indexes after dropping

        # convert TotalCharges to numeric,coercing errors to Nan
        self.df['TotalCharges'] = pd.to_numeric(self.df['TotalCharges'], errors='coerce')
        self.df.dropna(subset=['TotalCharges'], inplace=True)  # dropping rows with Nan values in total charges column
        self.df = self.df.reset_index(drop=True)  # reset indexing after dropping

    # Data after cleaning
    def clean_data(self):
        # number of rows after cleaning
        number_rows = self.df.shape[0]  # 7020 row after cleaning from 7047 row (before cleaning)
        print("\nNumber of rows : ", number_rows)

        # Check columns types after cleaning
        print("\nColumns datatypes after cleaning : ", self.df.dtypes)

    # ================================================================
    # 4- data statistics
    # =================================================================
    def data_statistics(self):
        """Calculate and display statistics about the dataset:
           average,max,min,mean,median,std"""

        # max tenure
        print("Max tenure : ", self.df['tenure'].max())
        row_max = self.df.loc[self.df['tenure'].idxmax()]  # find row with max tenure
        print(row_max)

        # min tenure
        print("min tenure : ", self.df['tenure'].min())
        row_min = self.df.loc[self.df['tenure'].idxmin()]  # find row with min tenure
        print(row_min)

        # average tenure
        print("mean tenure : ", self.df['tenure'].mean())

        # sorting data in ascending order
        self.df.sort_values(by=['tenure'], inplace=True)
        # median tenure
        print("median tenure : ", self.df['tenure'].median())

        # the standard deviation
        print("std tenure : ", self.df['tenure'].std())

        # max monthly charges
        print("max monthly charges : ", self.df['MonthlyCharges'].max())
        # min monthly charges
        print("min monthly charges : ", self.df['MonthlyCharges'].min())
        # average monthly charges
        print("mean monthly charges : ", self.df['MonthlyCharges'].mean())
        # sorting data in ascending order for monthly charges
        self.df.sort_values(by=['MonthlyCharges'], inplace=True)
        # median monthly charges
        print("median monthly charges : ", self.df['MonthlyCharges'].median())
        # standard deviation
        print("std monthly charges : ", self.df['MonthlyCharges'].std())
        # sum of monthly charges
        self.sum_monthly_charges = self.df['MonthlyCharges'].sum()
        print("sum monthly charges : ", self.sum_monthly_charges)  # 455310.3

        # max total charges
        print("max total charges : ", self.df['TotalCharges'].max())
        # min total charges
        print("min total charges : ", self.df['TotalCharges'].min())
        # average total charges
        print("mean total charges : ", self.df['TotalCharges'].mean())
        # sorting values in ascending order (total charges)
        self.df.sort_values(by=['TotalCharges'], inplace=True)
        # median total charges
        print("median total charges : ", self.df['TotalCharges'].median())
        # standard charges
        print("std total charges : ", self.df['TotalCharges'].std())
        # sum of total charges:
        self.sum_total_charges = self.df['TotalCharges'].sum()  # 16050229.65
        print("sum total charges : ", self.sum_total_charges)

        self.old_customerscount = self.df["SeniorCitizen"].value_counts()
        print("Number of customers : ", self.old_customerscount)


    # -------------------------------------------------------------------------------------------------------------------
    # 5-Grouping and filtering data
    # -------------------------------------------------------------------------------------------------------------------


    def filter_churn_status(self):
        # filtering people who churned---------------------------------------------------------------------------------
        self.df_quit = self.df[(self.df['Churn'] == 'Yes')]  # making an attribute in case we need to call later
        # counting number of churns
        self.number_quit = self.df_quit.shape[0]
        print("\nNumber of Quit : ", self.number_quit)  # n=1867

        # filtering people who are still active-------------------------------------------------------------------------
        self.df_active = self.df[(self.df['Churn'] == 'No')]
        # counting number of subscribers
        self.number_active = self.df_active.shape[0]
        print("\nNumber of Active : ", self.number_active)  # n2=5153 number of actives superior to churns

        # Global churn
        print("\nGlobal churn rate : ", self.df["Churn"].value_counts())

    def analyze_contract_and_demographics(self):
        # Grouping by Churn to see who are people who quit and why------------------------------------------------------
        # counting number of churns and actives for each contract duration
        self.contract_count = self.df.groupby("Churn")["Contract"].value_counts()
        print("\nNumber of customers for each contract duration", self.contract_count)

        # Loyal Customers  (tenure > 5years ) [Tenure = duration per month ]
        self.df_long = self.df[self.df["tenure"] >= 60]
        print("\nCustomers who stay long :", self.df_long)

        # New customers (with less than 1 year )
        self.df_less = self.df[self.df["tenure"] <= 12]
        print("\nCustomers who stay less than 12 months :", self.df_less)

        self.tenure_max = self.df.groupby("Churn")["tenure"].max()
        print(f"\n max tenure: {self.tenure_max}")

        self.tenure_min = self.df.groupby("Churn")["tenure"].min()


        # counting number of churns and active citizen who are senior citizens and who are not
        self.senior_citizen_Count = self.df.groupby("Churn")["SeniorCitizen"].value_counts()
        print("\nSenior citizen churn count : ", self.senior_citizen_Count)


        # counting number of customers who have dependents
        self.dependents_count = self.df.groupby("Churn")["Dependents"].value_counts()
        print("\nDependents churn count : ", self.dependents_count)


        # Partners influence
        print("\nPartner influence : ", self.df.groupby("Churn")["Partner"].value_counts())


        # Gender influence  **
        print("\nGender influence ", self.df.groupby("gender")["Churn"].value_counts())



    def analyze_service_usage(self):
        # counting people churned with phone service
        self.phone_service_Count = self.df.groupby("Churn")["PhoneService"].value_counts()
        print("\nPhone service churn count:", self.phone_service_Count)


        # counting number of churn customers who have multiple lines
        self.customer_multipleLinescount = self.df.groupby("Churn")["MultipleLines"].value_counts()
        print("\n Customer multiple lines count : ", self.customer_multipleLinescount)


        # counting number of customers with their internet service
        self.Customer_internetservice = self.df.groupby("Churn")["InternetService"].value_counts()
        print("\n Internet service count : ", self.Customer_internetservice)

        # Customers with fiber-optic internet only
        self.df_f_o = self.df[self.df["InternetService"] == "Fiber Optic"]
        print("\nCustomers who have fiber optic internet service :", self.df_f_o)

        # Internet service usage ***********************************************
        print("\nInternet service usage: ", self.df["InternetService"].value_counts())

        Service_cols = ["StreamingTV", "StreamingMovies"]
        self.streaming_churn = self.df.groupby(Service_cols)["Churn"].value_counts()
        print("\nChurn by Streaming TV and Movies usage:", self.streaming_churn)


    def analyze_financial_metrics(self):
        # now we need to see how much time customers stay
        self.customer_mcharges = self.df.groupby("Churn")["MonthlyCharges"].mean()
        print("\nCustomer mcharges :", self.customer_mcharges)

        self.mcharges_q1 = self.df.groupby("Churn")["MonthlyCharges"].quantile(0.25)
        self.mcharge_q2 = self.df.groupby("Churn")["MonthlyCharges"].quantile(0.75)
        print(f"\n Q1:{self.mcharges_q1} Q2:{self.mcharge_q2}")


        self.tcharges_q1 = self.df.groupby("Churn")["TotalCharges"].quantile(0.25)
        self.tcharges_q2 = self.df.groupby("Churn")["TotalCharges"].quantile(0.75)
        print(f"\n Q1:{self.tcharges_q1} Q2:{self.tcharges_q2}")

        # Analyse expenses with each internet service
        print("\nMonthly charges by internet service : ", self.df.groupby("InternetService")["MonthlyCharges"].sum())

        # High revenue customers
        self.df_high = self.df[self.df["MonthlyCharges"] >= 90]
        print("\nCustomers with high revenue :", self.df_high)

        # Customers with high total charges
        self.df_high_total = self.df[self.df["TotalCharges"] >= 3000]
        print("\nCustomers with high total charges :", self.df_high_total)

        # High risk group
        self.High_risk = self.df[(self.df["Contract"] == "Month-to-month") & (self.df["TotalCharges"] > 80)]
        print("\n\nHigh risk groups : ", self.High_risk.groupby("Churn")["MonthlyCharges"].sum())


        # Total charges by Contract type
        print("\nTotal charges by contract : ", self.df.groupby("Contract")["TotalCharges"].sum())

    def analyze_payment_and_billing(self):
        # Paper less billing influence
        print("\nPaper less billing influence  : ", self.df.groupby("PaperlessBilling")["Churn"].value_counts())

        # Payment method influence
        print("\nPayment method influence : ", self.df.groupby("PaymentMethod")["Churn"].value_counts())

    def analyze_protection_and_support_services(self):
        # Online security by churn rate
        print("\nOnline security by churn rate  : ", self.df.groupby("OnlineSecurity")["Churn"].value_counts())

        # Online backup by churn rate
        print("\nOnline backup by churn rate : ", self.df.groupby("OnlineBackup")["Churn"].value_counts())

        # Device protection by churn rate
        print("\nDevice protection by churn rate : ", self.df.groupby("DeviceProtection")["Churn"].value_counts())

        # TechSupport by churn rate
        print("\nTechSupport by churn rate : ", self.df.groupby("TechSupport")["Churn"].value_counts())

        # Churn rate by internet service and protection services
        Service_cols = [
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport"
        ]
        print("\nChurn rate by internet service and protection services  : ",
              self.df.groupby(Service_cols)["Churn"].value_counts())


        # ============================================================
        # 6- Data Visualisation
        # ============================================================
        def plot_global_churn(self):
            """Visualizes the overall distribution of Churn vs No Churn"""
            self.global_churn = self.df["Churn"].value_counts()
            plt.figure(figsize=(5, 4))
            colors = ['#66b3ff', '#ff9999']
            explode = (0, 0.1)
            self.font_dict = {'fontsize': 14, 'fontweight': 'bold', 'color': 'black'}
            plt.pie(
                self.global_churn,
                labels=self.global_churn.index,
                autopct='%1.1f%%',
                colors=colors,
                explode=explode,
                shadow=True
            )
            plt.title("Global Churn Rate", fontdict=self.font_dict)
            plt.axis('equal')
            plt.legend()
            plt.show()

        def plot_internet_service_analysis(self):
            """Visualizes churn rate by internet service type and general subscription distribution"""
            # Churn by Internet Service (Bar)
            churn_by_internet = self.df.groupby(['InternetService', 'Churn']).size().unstack()
            self.font_dict = {'fontsize': 14, 'fontweight': 'bold', 'color': 'black'}
            churn_by_internet.plot(kind='bar', figsize=(6, 4), color=['#66b3ff', '#ff9999'], width=0.8)
            plt.title("Churn rate by internet service", fontdict=self.font_dict)
            plt.xlabel("Type of Internet Service", fontsize=12)
            plt.ylabel("Number of customers", fontsize=12)
            plt.xticks(rotation=0)
            plt.legend(title='Churn', labels=['No', 'Yes'])
            plt.grid(axis='y', linestyle='--', alpha=0.5)
            plt.show()

            # Distribution of Internet Subscriptions (Pie)
            counts = self.df["InternetService"].value_counts()
            plt.figure(figsize=(6, 4))
            colors = ['#ff9999', '#66b3ff', '#99ff99']
            explode = [0.1 if v == counts.max() else 0 for v in counts]
            plt.pie(
                counts,
                labels=counts.index,
                autopct='%1.1f%%',
                startangle=90,
                colors=colors,
                explode=explode,
                shadow=True,
                textprops={'fontsize': 14}
            )
            plt.title("Distribution of Internet subscriptions", fontdict=self.font_dict)
            plt.axis('equal')
            plt.show()

        def plot_contract_and_billing_influence(self):
            """Visualizes how contract length and paperless billing affect churn"""
            # Impact of Contract Duration
            contract_data = self.df.groupby(['Contract', 'Churn']).size().unstack()
            self.font_dict = {'fontsize': 14, 'fontweight': 'bold', 'color': 'black'}
            contract_data.plot(kind='bar', figsize=(6, 5), color=['#66b3ff', '#ff9999'], width=0.8)
            plt.title("Impact of Contract Duration on Churn", fontdict=self.font_dict)
            plt.xlabel("Contract Type", fontsize=12)
            plt.ylabel("Number of Customers", fontsize=12)
            plt.xticks(rotation=0)
            plt.legend(title='Churn', labels=['No', 'Yes'])
            plt.grid(axis='y', linestyle='--', alpha=0.5)
            plt.show()

            # Paperless Billing influence
            paperless_data = self.df.groupby(['PaperlessBilling', 'Churn']).size().unstack()
            paperless_data.plot(kind='bar', figsize=(7, 6), color=['#66b3ff', '#ff9999'], width=0.8)
            plt.title("Churn Rate by Billing Method (Paperless)", fontdict=self.font_dict)
            plt.xlabel("Paperless Billing Active?", fontsize=12)
            plt.ylabel("Number of Customers", fontsize=12)
            plt.xticks(rotation=0)
            plt.legend(title='Churn', labels=['Stayed (No)', 'Churned (Yes)'])
            plt.grid(axis='y', linestyle='--', alpha=0.5)
            plt.show()

        def plot_payment_and_security_influence(self):
            """Visualizes churn patterns across payment methods and online security services"""
            # Payment Method Influence (Horizontal Bar)
            churn_yes = self.df[self.df["Churn"] == "Yes"]
            self.font_dict = {'fontsize': 14, 'fontweight': 'bold', 'color': 'black'}
            payment_churn_counts = churn_yes["PaymentMethod"].value_counts()
            plt.figure(figsize=(10, 5))
            plt.barh(payment_churn_counts.index, payment_churn_counts.values, color='#66b3ff')
            plt.title("Payment method influence (Churned Customers Only)", fontdict=self.font_dict)
            plt.xlabel("Number of churn customers")
            plt.ylabel("Payment Method")
            plt.yticks(rotation=45)
            plt.show()

            # Online Security influence
            data_prep = self.df.groupby(['OnlineSecurity', 'Churn']).size().unstack()
            data_prep.plot(kind='bar', figsize=(7, 6), color=['#66b3ff', '#ff9999'])
            plt.title("Online security by churn rate", fontdict=self.font_dict)
            plt.xlabel("OnlineSecurity", fontsize=12)
            plt.ylabel("Number of customers", fontsize=12)
            plt.xticks(rotation=0)
            plt.legend(title='Churn', labels=['No', 'Yes'])
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.show()

        def plot_tenure_and_ltv_analysis(self):
            """Advanced plots: Churn probability line and LTV scatter plot"""
            # Churn Probability by Tenure (Line Plot)
            self.df['Churn_num'] = self.df['Churn'].map({'Yes': 1, 'No': 0})
            self.font_dict = {'fontsize': 14, 'fontweight': 'bold', 'color': 'black'}
            churn_rate = self.df.groupby('tenure')['Churn_num'].mean() * 100

            plt.figure(figsize=(9, 6))
            plt.plot(churn_rate.index, churn_rate.values, color='#ff9999', linewidth=3, marker='o', markersize=5,
                     markerfacecolor='white')
            plt.title("Churn Probability by Tenure", fontdict=self.font_dict)
            plt.xlabel("Tenure (Months)", fontsize=12)
            plt.ylabel("Churn Rate (%)", fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.6)
            plt.axvspan(0, 12, color='red', alpha=0.1, label='Critical Zone (0-12 months)')
            plt.legend()
            plt.show()

            # Customer Lifetime Value (Scatter Plot)
            plt.figure(figsize=(10, 7))
            churn_no = self.df[self.df['Churn'] == 'No']
            churn_yes = self.df[self.df['Churn'] == 'Yes']
            self.font_dict = {'fontsize': 14, 'fontweight': 'bold', 'color': 'black'}

            plt.scatter(churn_no['tenure'], churn_no['TotalCharges'], color='#66b3ff', alpha=0.4, s=30,
                        label='Loyal (Secured Revenue)')
            plt.scatter(churn_yes['tenure'], churn_yes['TotalCharges'], color='#ff9999', alpha=0.6, s=30,
                        label='Churned (Lost Revenue)')

            plt.title("Customer Lifetime Value (LTV) Analysis", fontdict=self.font_dict)
            plt.xlabel("Tenure (Months)", fontsize=12)
            plt.ylabel("Total Revenue Generated ($)", fontsize=12)
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.5)

            y_max = self.df['TotalCharges'].max()
            plt.text(5, y_max * 0.8, "High Value Customers\n(Steep slopes = Expensive plans)", fontsize=10,
                     color='gray')
            plt.show()

if __name__=="__main__":
    data = CustomerChurnAnalysis(r"Telco_Cusomer_Churn.csv")

    # Load and inspect data
    data.load_data()
    print("\nInspecting data: -----")
    data.inspect_data()

    # Clean data
    data.data_cleaning()
    print("\nAfter cleaning data: -----")
    data.clean_data()

    # Data statistics
    print("\nData statistics: -----")
    data.data_statistics()

    # Grouping and filtering
    print("\nChurn Status:-------")
    data.filter_churn_status()
    print("\nAnalyzing contract and demographics: -----")
    data.analyze_contract_and_demographics()
    print("\nAnalyzing service usage: -----")
    data.analyze_service_usage()
    print("\nAnalyzing financial metrics: -----")
    data.analyze_financial_metrics()
    print("\nAnalyzing payment and billing: -----")
    data.analyze_payment_and_billing()
    print("\nAnalyzing protection and support services: -----")
    data.analyze_protection_and_support_services()

    # Data Visualization
    print("\nPlotting global churn: -----")
    data.plot_global_churn()
    print("\nPlotting internet service analysis: -----")
    data.plot_internet_service_analysis()
    print("\nPlotting contract and billing influence: -----")
    data.plot_contract_and_billing_influence()
    print("\nPlotting payment and security influence: -----")
    data.plot_payment_and_security_influence()
    print("\nPlotting tenure and LTV analysis: -----")
    data.plot_tenure_and_ltv_analysis()






