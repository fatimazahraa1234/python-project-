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
class DataAnalysisProject :
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
        df_long = self.df[self.df["Tenure"] >= 60]
        print("\nCustomers who stay long :",df_long)

        #New customers (with less than 1 year )
        df_less = self.df[self.df["Tenure"] <= 12 ]
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
        #Global churn distribution (numbers of clients who quit and who stayed )
        print("\nGlobal Churn : ",self.df.groupby(['Churn']).sum())

        #Count churn rate by internet service (counts the number of non-null values in this group )
        print("\nChurn rate by internet service : ",self.df.groupby("InternetService")["Churn"].count())

        #Churn rate by gender
        print("\nChurn rate by gender : ",self.df.groupby("Gender")["Churn"].count())

        #Average monthly charges by churn
        print("\nAverage monthly charges by churn : ",self.df.groupby("Churn")["MonthlyCharges"].mean())

        #Average total charges by churn
        print("\nAverage total charges by month :",self.df.groupby("Churn")["TotalCharges"].mean())

        #Monthly charges by contract type
        print("\nMonthly charges by contract type : ",self.df.groupby("Contract")["MonthlyCharges"].sum())

        #Total charges by internet service
        print("\nTotal charges by internet service : ",self.df.groupby("InternetService")["TotalCharges"].sum())

        #Multiple service Usage based on churn
        print("\nService usage : ",self.df.groupby("Churn")["PhoneService","OnlineBackup","TechSupport","StreamingTV","StreamingMovies"].mean())