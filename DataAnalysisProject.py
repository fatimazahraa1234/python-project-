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
    #1. Load Dataset
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
    #2-Inspect DataSet
    #------------------------------------------------
    def inspect_data(self):
        """Inspect the data set
        Displays dataset information , missing values
        and basic statistics """
        #Check if the data set is well loaded , if not it run out of the method to not cause errors
        if self.df is None :
            print("Dataset not loaded . ")
            return #To stop the function

        #summary of the dataframe with data types and number of non_null values for each column
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
        print(self.df.shape) #(7047,21)

        #List of columns along with data types
        print("\nDataset columns and datatypes : ")
        print(self.df.dtypes)

        #Provide basic statistical information about numerical columns
        print("\nDataset Description :")
        print(self.df.describe())

        #Identify and report missing values in each column
        print("\nMissing values in each column : ")
        #Cheks for Na values (empty or NULL values ) then sum the total number of missing values per column
        print(self.df.isnull().sum()) #after testing we observed that we have some missing values in some columns

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

        #number of rows after cleaning
        number_rows = self.df.shape[0]  #7020 row after cleaning from 7047 row (before cleaning)
        print("Number of rows : ", number_rows)

    #------------------------------------------------------------------------------------------------------------------
    #4-Summarizing data:calculating basic statistics for numerical columns
    #------------------------------------------------------------------------------------------------------------------
    def data_statistics(self):
        """Calculate and display statistics about the dataset:
           average,max,min,mean,median,std"""

        #max tenure
        print("Max tenure : ",self.df['tenure'].max())
        row_max= self.df.loc[self.df['tenure'].idxmax()] #find row with max tenure
        print(row_max)
        """
        max tenure : 6 years he s a young male with no dependents with partener,a phone service,multiple lines, DSL,
        online security,online backup,device protection,tech support, streaming tv, streaming movies. 2 years contract,
        paperless billing,paying with credit card (auto),90,25 monthly charges,6369.45 in total,still loyal (hasn't left
        agency)
        """
        #min tenure
        print("min tenure : ",self.df['tenure'].min())
        row_min = self.df.loc[self.df['tenure'].idxmin()]  # find row with min tenure
        print(row_min)
        """
        tenure=1 month,young male,with partner, has dependents,no phone service,DSL, no online security,with online backup,
        no device protection,no tech support,no streaming tv,no streaming movies, month to month contract, no paperless 
        billing, electronic check,30.2 monthly , total 30.2, has churned (stayed only for one month)
        """
        #average tenure
        print("mean tenure : ",self.df['tenure'].mean())
        """
        average 32 month
        """
        #sorting data in ascending order
        self.df.sort_values(by=['tenure'], inplace=True)
        #median tenure
        print("median tenure : ",self.df['tenure'].median())
        """
        50% of the customers stay for abt 29 months 50%< 50% more
        -->average>median -> this means that the majority stay less than the average (less than 32 months)
        -->the agency must do smtg abt it 
        """
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
        #sum of monthly charges
        self.sum_monthly_charges=self.df['MonthlyCharges'].sum()
        print("sum monthly charges : ",self.sum_monthly_charges) #455310.3

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
        #sum of total charges:
        self.sum_total_charges=self.df['TotalCharges'].sum() #16050229.65
        print("sum total charges : ",self.sum_total_charges)

        self.old_customerscount=self.df["SeniorCitizen"].value_counts()
        print("Number of customers : ",self.old_customerscount)
        """
        0    5878 young
        1    1142 senior
        --> N young customers > N senior
        """

    #-------------------------------------------------------------------------------------------------------------------
    #5-Grouping and filtering data
    #-------------------------------------------------------------------------------------------------------------------
    def group_and_filter_data(self):
        """ Data Filtration and grouping for data analysis """
        # filtering people who churned---------------------------------------------------------------------------------
        self.df_quit=self.df[(self.df['Churn']=='Yes')] #making an attribute in case we need to call later
        # #counting number of churns
        self.number_quit=self.df_quit.shape[0]
        print("\nNumber of Quit : ",self.number_quit) #n=1867

        # filtering people who are still active-------------------------------------------------------------------------
        self.df_active = self.df[(self.df['Churn'] == 'No')]
        # counting number of subscribers
        self.number_active = self.df_active.shape[0]
        print("\nNumber of Active : ", self.number_active)  # n2=5153 number of actives superior to churns

        #Grouping by Churn to see who are people who quit and why-------------------------------------------------------
        # counting number of churns and actives for each contract duration
        self.contract_count = self.df.groupby("Churn")["Contract"].value_counts()
        print("\nNumber of customers for each contract duration",self.contract_count)

        """
        No     Month-to-month    2216  --> still active
               Two year          1635
               One year          1302
        Yes    Month-to-month    1653  -->churn
               One year           166
               Two year            48
        --> customer churning most likely make month to month contract people still active make all kind of contract
        """

        #counting number of churns and active citizen who are senior citizens and who are not
        self.senior_citizen_Count=self.df.groupby("Churn")["SeniorCitizen"].value_counts()
        print("\nSenior citizen churn count : ",self.senior_citizen_Count)
        """
        No     0                4486  actives
               1                 667
        Yes    0                1392   churns
               1                 475
        -->people still active are younger customers 
        """

        #counting number of customers who have dependents
        self.dependents_count=self.df.groupby("Churn")["Dependents"].value_counts()
        print("\nDependents churn count : ",self.dependents_count)
        """
        No     No            3382  actives
               Yes           1771
        Yes    No            1541  churns
               Yes            326
        -->customers still active dont have dependents,I was expecting that people quitting will have people relying
        on them financially, but the results says otherwise !
        """

        #counting people churned with phone service
        self.phone_service_Count=self.df.groupby("Churn")["PhoneService"].value_counts()
        print("\nPhone service churn count:",self.phone_service_Count)
        """
        No     Yes             4648  actives
               No               505
        Yes    Yes             1698  churns
               No               169      
        --> many people with phone service are still active 
        """

        #counting number of churn customers who have multiple lines
        self.customer_multipleLinescount=self.df.groupby("Churn")["MultipleLines"].value_counts()
        print("\n Customer multiple lines count : ",self.customer_multipleLinescount)
        """
        No     No                  2531 actives
               Yes                 2117
               No phone service     505
        Yes    Yes                  850 churns
               No                   848
               No phone service     169
        -->people still active have multiple lines 2117 subscribers have multiple lines 
        """

        #counting number of customers with their internet service
        self.Customer_internetservice=self.df.groupby("Churn")["InternetService"].value_counts()
        print("\n Internet service count : ",self.Customer_internetservice)
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
        """grouping by churn internet service , streaming tv and streaming movies to see which internet service needs to
        be improved"""
        self.group=(
              self.df.groupby(["Churn", "InternetService", "StreamingTV", "StreamingMovies"])
              .size()
              .reset_index(name="count"))
        print("\nGrouping by churn internet service count : ")
        print(self.group)
        self.max_count=self.group.sort_values(by="count", ascending=False).head(1)
        print("\nmax count row: ",self.max_count)
        #I will add multiple lines to see exactly people who stay do they have multiple lines
        self.group2=(
              self.df.groupby(["Churn","MultipleLines", "InternetService", "StreamingTV", "StreamingMovies"])
              .size()
              .reset_index(name="count"))
        pd.set_option('display.max_columns', None) #to display all columns
        self.max_count2=self.group2.sort_values(by="count", ascending=False).head(1) #to display max count row
        print(self.max_count2)
        """
        need visualisation for better analysis but we got the max count row:
        No              No  No internet service  No internet service   1402 -->these are people still active they don't
        use any internet service
        No            No       No  No internet service  No internet service   1072
        -->this gives additional info : the majority of customers are people still active with one line,no internet
        service and no streaming  
        """
        #We need to see if these customers are senior or young
        self.group3= (
            self.df.groupby(["Churn","SeniorCitizen", "MultipleLines", "InternetService", "StreamingTV", "StreamingMovies"])
            .size()
            .reset_index(name="count"))
        pd.set_option('display.max_columns', None)  # to display all columns
        self.max_count3 = self.group3.sort_values(by="count", ascending=False).head(1)  # to display max count row
        print(self.max_count3)
        """
        No              0            No              No  No internet service  No internet service   1045
        -->additionally to what we found before the majority of customers are young people who are still active 
        """
        #now we need to see how much time customers stay
        self.customer_mcharges=self.df.groupby("Churn")["MonthlyCharges"].mean()
        print("\nCustomer mcharges :",self.customer_mcharges)
        """
        No     61.369930
        Yes    74.489047  
        -->people churning have more monthly charges
        """
        self.mcharges_q1=self.df.groupby("Churn")["MonthlyCharges"].quantile(0.25)
        self.mcharge_q2=self.df.groupby("Churn")["MonthlyCharges"].quantile(0.75)
        print(f"\n Q1:{self.mcharges_q1} Q2:{self.mcharge_q2}")
        """
        
        """








