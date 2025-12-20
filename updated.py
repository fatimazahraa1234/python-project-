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
    def _init_(self, file_path):
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
        """
        max tenure : 6 years he s a young male with no dependents with partener,a phone service,multiple lines, DSL,
        online security,online backup,device protection,tech support, streaming tv, streaming movies. 2 years contract,
        paperless billing,paying with credit card (auto),90,25 monthly charges,6369.45 in total,still loyal (hasn't left
        agency)
        """
        # min tenure
        print("min tenure : ", self.df['tenure'].min())
        row_min = self.df.loc[self.df['tenure'].idxmin()]  # find row with min tenure
        print(row_min)
        """
        tenure=1 month,young male,with partner, has dependents,no phone service,DSL, no online security,with online backup,
        no device protection,no tech support,no streaming tv,no streaming movies, month to month contract, no paperless 
        billing, electronic check,30.2 monthly , total 30.2, has churned (stayed only for one month)
        """
        # average tenure
        print("mean tenure : ", self.df['tenure'].mean())
        """
        average 32 month
        average 32 months
        """
        # sorting data in ascending order
        self.df.sort_values(by=['tenure'], inplace=True)
        # median tenure
        print("median tenure : ", self.df['tenure'].median())
        """
        50% of the customers stay for abt 29 months 50%< 50% more
        -->average>median -> this means that the majority stay less than the average (less than 32 months)
        -->the agency must do smtg abt it 
        """
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
        """
        0    5878 young
        1    1142 senior
        --> N young customers > N senior
        """

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

        # Global churn *************************************************
        print("\nGlobal churn rate : ", self.df["Churn"].value_counts())
        """
        Churn
        No     5153
        Yes    1867
        --> People who churn represent about 27% of customers but others are approximatively 73% 
        --> meaningful churn issue cuz this 26% of people who leave service can affect negatively total revenue 
        --> We still have time to handle this issue 
        """

    def analyze_contract_and_demographics(self):
        # Grouping by Churn to see who are people who quit and why-------------------------------------------------------
        # counting number of churns and actives for each contract duration
        self.contract_count = self.df.groupby("Churn")["Contract"].value_counts()
        print("\nNumber of customers for each contract duration", self.contract_count)

        """
        No    Month-to-month    2216  --> still active
              Two year          1635
              One year          1302
        Yes   Month-to-month    1653  -->churn
              One year           166
              Two year            48
        --> customer churning most likely make month to month contract people still active make all kind of contracts
        """

        # Loyal Customers  (tenure > 5years ) [Tenure = duration per month ]
        self.df_long = self.df[self.df["tenure"] >= 60]
        print("\nCustomers who stay long :", self.df_long)

        # New customers (with less than 1 year )
        self.df_less = self.df[self.df["tenure"] <= 12]
        print("\nCustomers who stay less than 12 months :", self.df_less)

        self.tenure_max = self.df.groupby("Churn")["tenure"].max()
        print(f"\n max tenure: {self.tenure_max}")
        """
          max tenure: Churn
             No     72
             Yes    72
        the max is 72 month for both loyals and churns
            ->doesn't bring much of help
        """

        self.tenure_min = self.df.groupby("Churn")["tenure"].min()
        print(f"\n min tenure: {self.tenure_min}")
        """
        min tenure: Churn
        No     1
        Yes    1
        same thing the minimum is one month for both loyal and churn customers
        """

        # counting number of churns and active citizen who are senior citizens and who are not
        self.senior_citizen_Count = self.df.groupby("Churn")["SeniorCitizen"].value_counts()
        print("\nSenior citizen churn count : ", self.senior_citizen_Count)
        """
        No     0                4486  actives
               1                 667
        Yes    0                1392   churns
               1                 475
        -->people still active are younger customers 
        """

        # counting number of customers who have dependents
        self.dependents_count = self.df.groupby("Churn")["Dependents"].value_counts()
        print("\nDependents churn count : ", self.dependents_count)
        """
        No     No             3382  actives
               Yes            1771
        Yes    No             1541  churns
               Yes             326
        -->customers still active dont have dependents,I was expecting that people quitting will have people relying
        on them financially, but the results says otherwise !
        """

        # Partners influence
        print("\nPartner influence : ", self.df.groupby("Churn")["Partner"].value_counts())
        """
        Churn  Partner
        No     Yes        2720
               No         2433
        Yes    No         1198
               Yes         669
        --> Customers with partners have more stable lifestyle --> less likely to churn --> often choose long time services
        --> It' s like 39% of customers who churn does nkt have partners 
        but who have partners are like approximatively 10% --> Big difference 
        """

        # Gender influence  **
        print("\nGender influence ", self.df.groupby("gender")["Churn"].value_counts())
        """ 
        gender  Churn
        Female  No       2538
                Yes       939   -->27%
        Male    No       2614
                Yes       929   -->26.22%
        -->So as we see gender does not influence churn rate
        """

    def analyze_service_usage(self):
        # counting people churned with phone service
        self.phone_service_Count = self.df.groupby("Churn")["PhoneService"].value_counts()
        print("\nPhone service churn count:", self.phone_service_Count)
        """
        No     Yes              4648  actives
               No                505
        Yes    Yes              1698  churns
               No                169      
        --> many people with phone service are still active 
        """

        # counting number of churn customers who have multiple lines
        self.customer_multipleLinescount = self.df.groupby("Churn")["MultipleLines"].value_counts()
        print("\n Customer multiple lines count : ", self.customer_multipleLinescount)
        """
        No     No                   2531 actives
               Yes                  2117
               No phone service     505
        Yes    Yes                  850 churns
               No                   848
               No phone service     169
        -->people still active have multiple lines 2117 subscribers have multiple lines 
        -->people still active have multiple lines 2117 subscribers have multiple lines 2531 have one line
        """

        # counting number of customers with their internet service
        self.Customer_internetservice = self.df.groupby("Churn")["InternetService"].value_counts()
        print("\n Internet service count : ", self.Customer_internetservice)
        """
        No     DSL                1952 actives
               Fiber optic        1799
               No                 1402
        Yes    Fiber optic        1297 churns
               DSL                 458
               No                  112    
        --> people still active have DSL (1952 subscribers have DSL max number) maybe we must improve fiber optic
        services we dont know exactly people why churn so what we gonna do next is grouping by churn internet service 
        and 
        """

        # Customers with fiber-optic internet only
        self.df_f_o = self.df[self.df["InternetService"] == "Fiber Optic"]
        print("\nCustomers who have fiber optic internet service :", self.df_f_o)

        # Internet service usage ***********************************************
        print("\nInternet service usage: ", self.df["InternetService"].value_counts())
        """
        InternetService
        Fiber optic    3096
        DSL            2410
        No             1514
        -->Fiber optic has the highest churn rate 42%, so even though it has the most customers
         it also represents the largest number of churned users
         --> Fiber optic is popular and hig churn risk 
        """
        Service_cols = ["StreamingTV", "StreamingMovies"]
        self.streaming_churn = self.df.groupby(Service_cols)["Churn"].value_counts()
        print("\nChurn by Streaming TV and Movies usage:", self.streaming_churn)
        """
        --> Customers with no streaming or only one service churn more
        --> Streaming services have lower churn rates than essential services like InternetService
        """

    def analyze_financial_metrics(self):
        # now we need to see how much time customers stay
        self.customer_mcharges = self.df.groupby("Churn")["MonthlyCharges"].mean()
        print("\nCustomer mcharges :", self.customer_mcharges)
        """
        No     61.369930
        Yes    74.489047  
        -->people churning have more monthly charges
        """

        self.mcharges_q1 = self.df.groupby("Churn")["MonthlyCharges"].quantile(0.25)
        self.mcharge_q2 = self.df.groupby("Churn")["MonthlyCharges"].quantile(0.75)
        print(f"\n Q1:{self.mcharges_q1} Q2:{self.mcharge_q2}")
        """

        Q1:Churn
        No     25.10   25% of active customers pay less than 25.10$
        Yes    56.25   75% of churn customers pay more than 56.25$
        Q2:Churn
        No     88.550   25% of active customers pay more than 88.550$
        Yes    94.225   25% of churn customers pay more than 94.225$, 75% pay less
        -> monthly charges influence 
        """

        self.tcharges_q1 = self.df.groupby("Churn")["TotalCharges"].quantile(0.25)
        self.tcharges_q2 = self.df.groupby("Churn")["TotalCharges"].quantile(0.75)
        print(f"\n Q1:{self.tcharges_q1} Q2:{self.tcharges_q2}")
        """
        Q1:Churn
        No     580.10
        Yes    134.85
        Q2:Churn
        No     4265.0
        Yes    2333.3
        """

        # Analyse expenses with each internet service
        print("\nMonthly charges by internet service : ", self.df.groupby("InternetService")["MonthlyCharges"].sum())
        """DSL            140108.85
           Fiber optic    283284.40
           No              31917.05

        --> As we see Monthly charges of fiber optic are so high than other services so maybe the problem 
        is highest monthly expenses
        """

        # High revenue customers
        self.df_high = self.df[self.df["MonthlyCharges"] >= 90]
        print("\nCustomers with high revenue :", self.df_high)

        # Customers with high total charges
        self.df_high_total = self.df[self.df["TotalCharges"] >= 3000]
        print("\nCustomers with high total charges :", self.df_high_total)

        # High risk group
        self.High_risk = self.df[(self.df["Contract"] == "Month-to-month") & (self.df["TotalCharges"] > 80)]
        print("\n\nHigh risk groups : ", self.High_risk.groupby("Churn")["MonthlyCharges"].sum())
        """Churn
        No     126903.9
        Yes    103487.3 
        --> We can see that half of customers churn and their charges are so high barely equal to loyal customers
        --> Big losses
        """

        # Total charges by Contract type
        print("\nTotal charges by contract : ", self.df.groupby("Contract")["TotalCharges"].sum())
        """
        Contract
        Month-to-month    5304884.50
        One year          4463244.25
        Two year          6282100.90
        -->longer contracts lead to higher revenues per customer
        """

    def analyze_payment_and_billing(self):
        # Paper less billing influence
        print("\nPaper less billing influence  : ", self.df.groupby("PaperlessBilling")["Churn"].value_counts())
        """
        PaperlessBilling  Churn
        No                No       2388
                          Yes       468
        Yes               No       2765
                          Yes      1399
        -->Customers with paperless billing are more likely to churn 33.6% compared to those without paperless billing 16.4%
        There is a strong relationship between PaperlessBilling and Churn 
        """

        # Payment method influence
        print("\nPayment method influence : ", self.df.groupby("PaymentMethod")["Churn"].value_counts())
        """
        PaymentMethod              Churn
        Bank transfer (automatic)  No       1282
                                   Yes       258
        Credit card (automatic)    No       1288
                                   Yes       232
        Electronic check           No       1290
                                   Yes      1070
        Mailed check               No       1293
                                   Yes       307
        Bank transfer it's about 17% of customers who churn 
        Credit card (automatic)   16%
        Electronic check  about 47%
        Mailed chack 20%
        -->People with automatic payment --> lowest churn rate 
        -->Electronic check --> very high churn rate (technical issues,delays or dissatisfaction or maybe looking for 
        another service for switching )
        -->For retention agencies should encourage Automatic payment
        """

    def analyze_protection_and_support_services(self):
        # Online security by churn rate
        print("\nOnline security by churn rate  : ", self.df.groupby("OnlineSecurity")["Churn"].value_counts())
        """
        OnlineSecurity       Churn
        No                   No       2034
                             Yes      1460 --> 42%
        No internet service  No       1402
                             Yes       112
        Yes                  No       1717 --> 15%
                             Yes       295
        -->Customers without online security have the highest churn
        Nearly 42% churn rate, which is extremely high
        This is a major risk group
        """

        # Online backup by churn rate
        print("\nOnline backup by churn rate : ", self.df.groupby("OnlineBackup")["Churn"].value_counts())
        """
        OnlineBackup         Churn
        No                   No       1851
                             Yes      1232
        No internet service  No       1402
                             Yes       112
        Yes                  No       1900 
                             Yes       523  --> 21.5 %
        -->Customers without online backup have a very high churn rate (40%)
        -->Customers feel more secure and protected 
        -->Online backup is a cloud-based service that automatically stores customer data remotely 
        increasing service value and reducing churn by improving data security and customer attachment
        (I's hard to look for another provider)
        """

        # Device protection by churn rate
        print("\nDevice protection by churn rate : ", self.df.groupby("DeviceProtection")["Churn"].value_counts())
        """
        DeviceProtection     Churn
        No                   No       1880
                             Yes      1211
        No internet service  No       1402
                             Yes       112
        Yes                  No       1871
                             Yes       544
        -->Customers without device protection churn the most Nearly 40% churn rate, which is very high
        """
        """
        Conclusion : Among internet-related services, OnlineSecurity shows the strongest negative association with churn
        followed by OnlineBackup and DeviceProtection, making it the most effective retention level
        """

        # TechSupport by churn rate
        print("\nTechSupport by churn rate : ", self.df.groupby("TechSupport")["Churn"].value_counts())
        """
        TechSupport          Churn
        No                   No       2023
                             Yes      1445 -->40%
        No internet service  No       1402
                             Yes       112
        Yes                  No       1728
                             Yes       310 -->16%
        -->Customers without TechSupport have the highest churn, while having 
        TechSupport lowers churn dramatically, making it one of the most effective retention services
        """

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
        """
        --> Customers with Fiber optic and no protection services -> highest churn
        """

        """
        As we see : 
        OnlineSecurity , TechSupport : High churn rate
        OnlineBackup ,DevicProtection : Medium churn rate
        StreamingTV , StreamingMovies : Low churn rate  
         -->So agency should focus on high churn rate services and improve their quality 
        """
        """
        We covered :
        **Internet Service – high churn for Fiber Optic, likely due to cost or perceived quality
        **Monthly Charges & Total Charges – high charges linked to higher churn, especially for month-to-month contracts
        **Contract Type – longer contracts strongly reduce churn
        **Partner status – customers with partners churn less
        **Paperless Billing – associated with higher churn
        **Payment Method – automatic payments reduce churn; electronic checks have the highest churn
        **Gender – no significant effect
       """

        # ============================================================
        # 6- Data Visualisation
        # ============================================================

    def plot_data(self):
        """Master method to trigger all visualizations"""
        # Define a global font dictionary for consistency
        self.font_dict = {'fontsize': 14, 'fontweight': 'bold', 'color': 'black'}

        # Call specific plotting methods
        self.plot_global_churn()
        self.plot_internet_service_analysis()
        self.plot_contract_and_billing_influence()
        self.plot_payment_and_security_influence()
        self.plot_tenure_and_ltv_analysis()

    def plot_global_churn(self):
        """Visualizes the overall distribution of Churn vs No Churn"""
        self.global_churn = self.df["Churn"].value_counts()
        plt.figure(figsize=(5, 4))
        colors = ['#66b3ff', '#ff9999']
        explode = (0, 0.1)

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
        payment_churn_counts = churn_yes["PaymentMethod"].value_counts()
        plt.figure(figsize=(10, 5))
        plt.barh(payment_churn_counts.index, payment_churn_counts.values, color='salmon')
        plt.title("Payment method influence (Churned Customers Only)", fontdict=self.font_dict)
        plt.xlabel("Number of churn customers")
        plt.ylabel("Payment Method")
        plt.yticks(rotation=45)
        plt.show()

        # Online Security influence
        data_prep = self.df.groupby(['OnlineSecurity', 'Churn']).size().unstack()
        data_prep.plot(kind='bar', figsize=(7, 6), color=['#4caf50', '#f44336'])
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
        churn_rate = self.df.groupby('tenure')['Churn_num'].mean() * 100

        plt.figure(figsize=(9, 6))
        plt.plot(churn_rate.index, churn_rate.values, color='#800080', linewidth=3, marker='o', markersize=5,
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

        plt.scatter(churn_no['tenure'], churn_no['TotalCharges'], color='#2ed573', alpha=0.4, s=30,
                    label='Loyal (Secured Revenue)')
        plt.scatter(churn_yes['tenure'], churn_yes['TotalCharges'], color='#ff4757', alpha=0.6, s=30,
                    label='Churned (Lost Revenue)')

        plt.title("Customer Lifetime Value (LTV) Analysis", fontdict=self.font_dict)
        plt.xlabel("Tenure (Months)", fontsize=12)
        plt.ylabel("Total Revenue Generated ($)", fontsize=12)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)

        y_max = self.df['TotalCharges'].max()
        plt.text(5, y_max * 0.8, "High Value Customers\n(Steep slopes = Expensive plans)", fontsize=10, color='gray')
        plt.show()