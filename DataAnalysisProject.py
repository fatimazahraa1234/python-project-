#-----------------------------------------------------------------
#Digital Skills & Python Programming Final Project
#-----------------------------------------------------------------
#Team Members :
"""
    *** FATIMA ZAHRA EL HALFI ***
    *** AYA DOUBIANI ***
    *** IKRAM BEN AYA ***
    *** OUMAIMA SAID ***
    *** FATIMA ZAHRA EL-BOURIMI ***
"""

#import needed modules in this project
import matplotlib.pyplot as plt
import pandas as pd


#Build a class that will contain all methods to apply on dataset (load, analyze, plot )
class CustomerChurnAnalysis :
    def __init__(self,file_path):
        #constructor : initializes the class with the path to the dataset file
        #It stores the file's path to use it later in the class methods
        self.file_path = file_path
        #It creates an attribute called df (DataFrame) and sets it to empty at the beginning
        self.df = None

    #--------------------------------------------------
    #1. Load Dataset : read the csv file containing the dataset for analysis and handle exceptions
    #--------------------------------------------------
    def load_data(self):
        """Load the data set from a csv file """
        try :
            #Read the csv file into a Data Frame for analysis
            self.df = pd.read_csv(self.file_path)
            print("File loaded successfully . ")
        except FileNotFoundError :
            #Error raised when the file does not exist
            print("File not found . ")
        except PermissionError :
            #Error raised when the user has no permission to open the file
            print("You don't have permission to access this file . ")
        except Exception as e :
            #Error raised when something went wrong while loading the csv file
            print(f"Something went wrong while loading the file : {e} ")

    #------------------------------------------------
    #2-Inspect DataSet : General information about dataset (numbers of rows , cols ,missing values and some statistic methods  )
    #------------------------------------------------
    def inspect_data(self):
        """Inspect the data set
        Displays dataset information , missing values
        and basic statistics """
        #Check if the data set is well loaded , if not it run out of the method to not cause errors
        if self.df is None :
            print("Dataset not loaded . ")
            return #To stop the function

        #summary of the dataframe with data types and missing values
        print("\nDataset Information ******************** ")
        print(self.df.info())

        #Display the first 10 rows
        print("\nFirst 10 rows : ")
        print(self.df.head(10))

        #Display the last 10 rows
        print("\nLast 10 rows : ")
        print(self.df.tail(10))

        #Display the dataset's shape : tuple containing number of rows and columns
        print("\nDataset's size is : ")
        print(self.df.shape)

        #List of columns along with data types
        print("\nDataset columns and datatypes : ")
        print(self.df.dtypes)

        #Provide basic statistical information about numerical columns
        print("\nDataset Description :")
        print(self.df.describe())

        #Identify and report missing values in each column
        print("\nMissing values in each column : ")
        #Cheks for Na values (empty or NULL values ) then sum the total number of missing values per column
        print(self.df.isnull().sum())

    #----------------------------------------------------------------------------------------
    #3-cleaning data: handling missing data,duplicate values and invalid entries
    #----------------------------------------------------------------------------------------
    def data_cleaning(self):
        """Clean the dataset; remove rows with missing values,
        remove duplicate rows,fix data of wrong format"""

        # remove rows with missing values, apply changes to the original dataframe
        self.df.dropna(inplace=True)
        # remove duplicate rows
        self.df=self.df.drop_duplicates()
        # to reorder the index after dropping duplicate rows
        self.df=self.df.reset_index(drop=True)

        # convert tenure to numeric,coercing errors to NaN
        self.df['tenure'] = pd.to_numeric(self.df['tenure'], errors='coerce')
        #dropping rows where tenure is NaN
        self.df.dropna(subset=['tenure'], inplace=True)
        self.df.reset_index(drop=True)#reorder the index after dropping

        #convert MonthlyCharges to numeric,coercing errors to NaN
        self.df['MonthlyCharges']=pd.to_numeric(self.df['MonthlyCharges'], errors='coerce')
        self.df.dropna(subset=['MonthlyCharges'], inplace=True) #dropping rows where monthly charges are NaN
        self.df.reset_index(drop=True) #reset indexes after dropping

        #convert TotalCharges to numeric,coercing errors to Nan
        self.df['TotalCharges']=pd.to_numeric(self.df['TotalCharges'], errors='coerce')
        self.df.dropna(subset=['TotalCharges'], inplace=True) #dropping rows with Nan values in total charges column
        self.df.reset_index(drop=True) #reset indexing after dropping

    #------------------------------------------------------------------------------------------------------------------
    #4-Summarizing data:calculating basic statistics for numerical columns
    #------------------------------------------------------------------------------------------------------------------
    def data_statistics(self):
        """Calculate and display statistics about the dataset:
           average,max,min,mean,median,std"""

        #max tenure
        print("max tenure : ",self.df['tenure'].max())
        #min tenure
        print("min tenure : ",self.df['tenure'].min())
        #average tenure
        print("mean tenure : ",self.df['tenure'].mean())
        #sorting data in ascending order
        self.df.sort_values(by=['tenure'], inplace=True)
        #median tenure
        print("median tenure : ",self.df['tenure'].median())
        #the standard deviation
        print("std tenure : ",self.df['tenure'].std())

        #max monthly charges
        print("max monthly charges : ",self.df['MonthlyCharges'].max())
        #min monthly charges
        print("min monthly charges : ",self.df['MonthlyCharges'].min())
        #average monthly charges
        print("mean monthly charges : ",self.df['MonthlyCharges'].mean())
        #sorting data in ascending order for monthly charges
        self.df.sort_values(by=['MonthlyCharges'], inplace=True)
        #median monthly charges
        print("median monthly charges : ",self.df['MonthlyCharges'].median())
        #standard deviation
        print("std monthly charges : ",self.df['MonthlyCharges'].std())

        #max total charges
        print("max total charges : ",self.df['TotalCharges'].max())
        #min total charges
        print("min total charges : ",self.df['TotalCharges'].min())
        #average total charges
        print("mean total charges : ",self.df['TotalCharges'].mean())
        #sorting values in ascending order (total charges)
        self.df.sort_values(by=['TotalCharges'], inplace=True)
        #median total charges
        print("median total charges : ",self.df['TotalCharges'].median())
        #standard charges
        print("std total charges : ",self.df['TotalCharges'].std())

    #-------------------------------------------------------------------------------------------------------------------
    #5-Grouping and filtering data
    #-------------------------------------------------------------------------------------------------------------------
    def group_and_filter_data(self):
        """ Data Filtration """

        #Clients who quit (churn = yes )
        df_quit = self.df[self.df["Churn"]=="Yes" ]
        print("\nCustomers who quit :",df_quit)

        #Loyal Customers  (tenure > 5years ) [Tenure = duration per month ]
        df_long = self.df[self.df["tenure"] >= 60]
        print("\nCustomers who stay long :",df_long)

        #New customers (with less than 1 year )
        df_less = self.df[self.df["tenure"] <= 12 ]
        print("\nCustomers who stay less than 12 months :",df_less)

        #High revenue customers
        df_high = self.df[self.df["MonthlyCharges"] >= 90]
        print("\nCustomers with high revenue :",df_high)

        #Customers with fiber-optic internet only
        df_f_o=self.df[self.df["InternetService"]=="Fiber Optic" ]
        print("\nCustomers who have fiber optic internet service :",df_f_o)

        #High risk customers : month to month contract and high charges
        """These customers with high monthly charges but just with monthly contact 
        so they can leve anytime --> high churn rate --> more dissatisfaction """

        df_risk=self.df[(self.df["Contract"] == "Month-to-month") & (self.df["MonthlyCharges"] >= 80)]
        print("\nCustomers with high churn rate :",df_risk)

        #Customers with high total charges
        df_high_total = self.df[self.df["TotalCharges"] >= 3000 ]
        print("\nCustomers with high total charges :",df_high_total)



        """ Data Groupment """


        #Global churn *************************************************
        print("\nGlobal churn rate : ",self.df["Churn"].value_counts())
        """
        Churn
        No     5153
        Yes    1867
        --> People who churn represent about 27% of customers but others are approximatively 73% 
        --> meaningful churn issue cuz this 26% of people who leave service can affect negatively total revenue 
        --> We still have time to handle this issue 
        """

        #Internet service by churn rate *********************************
        Internet_churn = self.df.groupby("InternetService")["Churn"].value_counts()
        print("\nChurn rate by Internet Service :",Internet_churn)
        """
        InternetService  Churn
        DSL              No       1952
                         Yes       458
        Fiber optic      No       1799
                         Yes      1297
        No               No       1402
                         Yes       112
        --> So in this case people  with fiber optic who churn more than DSL Maybe the problem 
        is the internet service quality 
        or something else : for that we gonna check MonthlyCharges based on each service 
        """

        #Internet service usage ***********************************************
        print("\nInternet service usage: ",self.df["InternetService"].value_counts())
        """
        InternetService
        Fiber optic    3096
        DSL            2410
        No             1514
        -->Fiber optic has the highest churn rate 42%, so even though it has the most customers
         it also represents the largest number of churned users
         --> Fiber optic is popular and hig churn risk 
        """


        #Analyse expenses with each internet service ***********************************************
        print("\nMonthly charges by internet service : ",self.df.groupby("InternetService")["MonthlyCharges"].sum())
        """DSL            140108.85
           Fiber optic    283284.40
           No              31917.05

        --> As we see Monthly charges of fiber optic are so high than other services so maybe the problem 
        is highest monthly expenses
        """

        #High risk group **********************************************
        High_risk = self.df[(self.df["Contract"] == "Month-to-month") & (self.df["MonthlyCharges"] > 80)]
        print("\n\nHigh risk groups : " ,High_risk.groupby("Churn")["MonthlyCharges"].sum())
        """Churn
        No     126903.9
        Yes    103487.3 
        --> We can see that half of customers churn and their charges are so high barely equal to loyal customers
        --> Big losses
        """

        #Contract type influence on churn rate *********************************************
        print("\nChurn by contract type : ",self.df.groupby("Contract")["Churn"].value_counts())
        """
        Contract        Churn
        Month-to-month  No       2216
                        Yes      1653
        One year        No       1302
                        Yes       166
        Two year        No       1635
                        Yes        48
        --> More contract duration long more customers are loyal to the agency and churn rate is so low 
        """


        #Total charges by Contract type **************************************************
        print("\nTotal charges by contract : ",self.df.groupby("Contract")["TotalCharges"].sum())
        """
        Contract
        Month-to-month    5304884.50
        One year          4463244.25
        Two year          6282100.90
        -->longer contracts lead to higher revenues per customer
        """

        #Partners influence  ***************************************************************
        print("\nPartner influence : ",self.df.groupby("Churn")["Partner"].value_counts())
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

        #Paper less billing influence *****************************************************
        print("\nPaper less billing influence  : ",self.df.groupby("PaperlessBilling")["Churn"].value_counts())
        """
        PaperlessBilling  Churn
        No                No       2388
                          Yes       468
        Yes               No       2765
                          Yes      1399
        -->Customers with paperless billing are more likely to churn 33.6% compared to those without paperless billing 16.4%
        There is a strong relationship between PaperlessBilling and Churn 
        """

        #Payment method influence ****************************************************************
        print("\nPayment method influence : ",self.df.groupby("PaymentMethod")["Churn"].value_counts())
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

        #Gender influence  *********************************************************************
        print("\nGender influence ",self.df.groupby("gender")["Churn"].value_counts())
        """ 
        gender  Churn
        Female  No       2538
                Yes       939   -->27%
        Male    No       2614
                Yes       929   -->26.22%
        -->So as we see gender does not influence churn rate
        """


        #Online security by churn rate *******************************************************
        print("\nOnline security by churn rate  : ",self.df.groupby("OnlineSecurity")["Churn"].value_counts())
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


        #Online backup by churn rate ****************************************************
        print("\nOnline backup by churn rate : ",self.df.groupby("OnlineBackup")["Churn"].value_counts())
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

        #Device protection by churn rate ****************************************************
        print("\nDevice protection by churn rate : ",self.df.groupby("DeviceProtection")["Churn"].value_counts())
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

        #TechSupport by churn rate *******************************************************
        print("\nTechSupport by churn rate : ",self.df.groupby("TechSupport")["Churn"].value_counts())
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

        #Streaming TV and movies by churn rate ***********************************************************
        print("\nStreaming TV and movies by churn rate : ",self.df.groupby(["StreamingTV","StreamingMovies"])["Churn"].value_counts())
        """
        StreamingTV          StreamingMovies      Churn
        No                   No                   No       1318
                                                  Yes       695
                             Yes                  No        545
                                                  Yes       246
        No internet service  No internet service  No       1402
                                                  Yes       112
        Yes                  No                   No        521
                                                  Yes       243
                             Yes                  No       1367
                                                  Yes       571
        -->Weak retention factor : Subscribing to streaming services does not strongly prevent churn(weak influence)
        """


        #Churn rate by internet service and protection services
        Service_cols = [
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport"
        ]
        print("\nChurn rate by internet service and protection services  : ",self.df.groupby(Service_cols)["Churn"].value_counts())
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



        # ------------------------------------------------------------------
        # 6. Plotting Data
        # ------------------------------------------------------------------


    def plot_data(self):
        """Visualise le Global Churn Rate"""
        print("Génération du graphique...")  # Pour déboguer

        # Calcul des comptes (si pas déjà fait avant)
        self.global_churn = self.df["Churn"].value_counts()

        plt.figure(figsize=(5, 4))

        # Couleurs : Vert pour ceux qui restent, Rouge pour l'alerte
        colors = ['#66b3ff', '#ff9999']
        explode = (0, 0.1)

        font_dict = {
            'fontsize': 14,  # Font size
            'fontweight': 'bold',  # Font weight
            'color': 'black'}

        plt.pie(
                self.global_churn,
                labels=self.global_churn.index,
                autopct='%1.1f%%',
                colors=colors,
                explode=explode,
                shadow=True,

        )


        plt.title("Global Churn Rate",fontdict=font_dict)
        plt.axis('equal')
        plt.legend()
        plt.show()  # Ceci doit ouvrir la fenêtre

        """Visualise le Churn par type de service Internet"""


        # we cross InternetService and Churn
        # unstack() allows us to get 'No' and 'Yes' as a column side by side
        churn_by_internet = self.df.groupby(['InternetService', 'Churn']).size().unstack()
        churn_by_internet.plot(kind='bar', figsize=(6, 4), color=['#66b3ff', '#ff9999'], width=0.8)
        plt.title("Churn rate by internet service", fontdict=font_dict)
        plt.xlabel("Type of Internet Service", fontsize=12)
        plt.ylabel("Number of customers", fontsize=12)
        plt.xticks(rotation=0)
        plt.legend(title='Churn', labels=['No', 'Yes'])
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.show()


        # Internet service usage *****************************************

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

        plt.title(" Destribution of Internet subscriptions ", fontdict=font_dict)
        plt.axis('equal')
        plt.show()


        # Contract type influence on churn rate *********************************************

        """Visualizes the impact of contract type on churn"""

        contract_data = self.df.groupby(['Contract', 'Churn']).size().unstack()

        contract_data.plot(kind='bar', figsize=(6, 5), color=['#66b3ff', '#ff9999'], width=0.8)

        plt.title("Impact of Contract Duration on Churn", fontdict=font_dict)
        plt.xlabel("Contract Type", fontsize=12)
        plt.ylabel("Number of Customers", fontsize=12)
        plt.xticks(rotation=0)  # Keep text horizontal for readability

        plt.legend(title='Churn', labels=['No', 'Yes'])

        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.show()

        # Paper less billing influence *****************************************************

        paperless_data = self.df.groupby(['PaperlessBilling', 'Churn']).size().unstack()
        paperless_data.plot(kind='bar', figsize=(7, 6), color=['#66b3ff', '#ff9999'], width=0.8)

        plt.title("Churn Rate by Billing Method (Paperless)", fontdict=font_dict)
        plt.xlabel("Paperless Billing Active?", fontsize=12)
        plt.ylabel("Number of Customers", fontsize=12)
        plt.xticks(rotation=0)
        plt.legend(title='Churn', labels=['Stayed (No)', 'Churned (Yes)'])
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.show()

        # Payment method influence ***************************************************

        churn_yes = self.df[self.df["Churn"] == "Yes"]
        payment_churn_counts = churn_yes["PaymentMethod"].value_counts()

        plt.figure(figsize=(10, 5))
        plt.barh(payment_churn_counts.index, payment_churn_counts.values, color='salmon')

        plt.title("Payment method influence", fontdict=font_dict)
        plt.xlabel("Number of churn customers")
        plt.ylabel("PaymentMethod")
        plt.yticks(rotation=45)
        plt.show()

        # Online security by churn rate *******************************************

        data_prep = self.df.groupby(['OnlineSecurity', 'Churn']).size().unstack()
        data_prep.plot(kind='bar', figsize=(7, 6), color=['#4caf50', '#f44336'])

        plt.title("Online security by churn rate", fontdict=font_dict)
        plt.xlabel("OnlineSecurity", fontsize=12)
        plt.ylabel("Number of customers ", fontsize=12)
        plt.xticks(rotation=0)
        plt.legend(title='Churn', labels=['No', 'Yes'])

        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

        #LINE PLOT: Visualizes the evolution of the churn rate based on tenure.
        #Shows that the risk is highest during the first year.
        self.df['Churn_num'] = self.df['Churn'].map({'Yes': 1, 'No': 0})
        churn_rate = self.df.groupby('tenure')['Churn_num'].mean() * 100

        plt.figure(figsize=(9, 6))

        plt.plot(
            churn_rate.index,
            churn_rate.values,
            color='#800080',
            linewidth=3,
            marker='o',
            markersize=5,
            markerfacecolor='white'
        )

        plt.title("Churn Probability by Tenure", fontdict=font_dict)
        plt.xlabel("Tenure (Months)", fontsize=12)
        plt.ylabel("Churn Rate (%)", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.axvspan(0, 12, color='red', alpha=0.1, label='Critical Zone (0-12 months)')
        plt.legend()
        plt.show()


        #scatter plot ################################################
        #Customer Lifetime Value (LTV) Analysis

        plt.figure(figsize=(10, 7))
        # We split the data to assign different colors
        churn_no = self.df[self.df['Churn'] == 'No']
        churn_yes = self.df[self.df['Churn'] == 'Yes']
        plt.scatter(
            churn_no['tenure'],
            churn_no['TotalCharges'],
            color='#2ed573',
            alpha=0.4,
            s=30,  # Dot size
            label='Loyal (Secured Revenue)'
        )
        plt.scatter(
            churn_yes['tenure'],
            churn_yes['TotalCharges'],
            color='#ff4757',
            alpha=0.6,
            s=30,
            label='Churned (Lost Revenue)'
        )

        plt.title("Customer Lifetime Value (LTV) Analysis", fontdict=font_dict)
        plt.xlabel("Tenure (Months)", fontsize=12)
        plt.ylabel("Total Revenue Generated ($)", fontsize=12)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)

        y_max = self.df['TotalCharges'].max()
        plt.text(5, y_max * 0.8, "High Value Customers\n(Steep slopes = Expensive plans)", fontsize=10, color='gray')

        plt.show()











