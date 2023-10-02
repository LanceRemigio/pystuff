# SF Salaries Exercise

Import pandas as pd


````python
import pandas as pd
````

Read Salaries.csv as a dataframe called sal

````python
sal = pd.read_csv('Salaries.csv')
````

Check the head of the dataframe.

````python
sal.head()
````
The output:
````
   Id       EmployeeName                                        JobTitle  ...  Notes         Agency  Status
0   1     NATHANIEL FORD  GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY  ...    NaN  San Francisco     NaN
1   2       GARY JIMENEZ                 CAPTAIN III (POLICE DEPARTMENT)  ...    NaN  San Francisco     NaN
2   3     ALBERT PARDINI                 CAPTAIN III (POLICE DEPARTMENT)  ...    NaN  San Francisco     NaN
3   4  CHRISTOPHER CHONG            WIRE ROPE CABLE MAINTENANCE MECHANIC  ...    NaN  San Francisco     NaN
4   5    PATRICK GARDNER    DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)  ...    NaN  San Francisco     NaN

[5 rows x 13 columns]
````

Use the `.info()` method to find out how many entries there are. 

````
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 148654 entries, 0 to 148653
Data columns (total 13 columns):
 #   Column            Non-Null Count   Dtype  
---  ------            --------------   -----  
 0   Id                148654 non-null  int64  
 1   EmployeeName      148654 non-null  object 
 2   JobTitle          148654 non-null  object 
 3   BasePay           148045 non-null  float64
 4   OvertimePay       148650 non-null  float64
 5   OtherPay          148650 non-null  float64
 6   Benefits          112491 non-null  float64
 7   TotalPay          148654 non-null  float64
 8   TotalPayBenefits  148654 non-null  float64
 9   Year              148654 non-null  int64  
 10  Notes             0 non-null       float64
 11  Agency            148654 non-null  object 
 12  Status            0 non-null       float64
dtypes: float64(8), int64(2), object(3)
memory usage: 14.7+ MB
None
````
There are 14654 entries. 

Find the average base pay

````python
avg_pay = sal['BasePay'].mean()
````
which outputs  `66325.4488404877`

What is the highest amount of Overtimepay in the dataset?

````python
max_pay = sal['OvertimePay'].max()
````

What is the job title of JOSEPH DRISCOLL? 
````python
sal[['EmployeeName', 'JobTitle']].loc[sal['EmployeeName'] == 'JOSEPH DRISCOLL']
````

which returns 
````
       EmployeeName                   JobTitle
24  JOSEPH DRISCOLL  CAPTAIN, FIRE SUPPRESSION
````

How much does he make (including benefits)?
````python
jobsempl = sal['TotalPayBenefits'].loc[sal['EmployeeName'] == 'JOSEPH DRISCOLL']
````
which returns 
````
24    270324.91
Name: TotalPayBenefits, dtype: float64
````

What is the name of highest paid person (including benefits)?

````python
highest_pay = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]
````

which returns 
````
   Id    EmployeeName  ...         Agency  Status
0   1  NATHANIEL FORD  ...  San Francisco     NaN

[1 rows x 13 columns]
````

What is the name of the lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?

````python
lowest_pay = sal[['EmployeeName', 'TotalPayBenefits', 'TotalPay']].loc[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]
````
which outputs the following:
````
       EmployeeName  TotalPayBenefits  TotalPay
148653    Joe Lopez           -618.13   -618.13
````
The values returned are negative which does not make much sense.

What was the average (mean) BasePay of all employees per year? (2011-2014)?

````python
avg_pay = sal.groupby(by = 'Year', as_index = False)['BasePay'].mean()
````
which returns the following output:
````
   Year       BasePay
0  2011  63595.956517
1  2012  65436.406857
2  2013  69630.030216
3  2014  66564.421924
````

What are the top 5 most common jobs?

````python
sal['JobTitle'].value_counts().head(5)
````

which returns the following series:
````
JobTitle
Transit Operator                7036
Special Nurse                   4389
Registered Nurse                3736
Public Svc Aide-Public Works    2518
Police Officer 3                2421
Name: count, dtype: int64
````


How many Job Titles were represented by only one person in 2013? (e.g Job Titles with only one occurence in 2013?)
