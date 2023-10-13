# Pandas Ecommerce Exercises


## Importing the data

Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom.
````python
ecom = pd.read_csv('Ecommerce Purchases')
````


## Checking the head of the dataframe

````python
ecom.head()
````
which returns 
````
                                             Address    Lot  ... Language Purchase Price
0  16629 Pace Camp Apt. 448\nAlexisborough, NE 77...  46 in  ...       el          98.14
1  9374 Jasmine Spurs Suite 508\nSouth John, TN 8...  28 rn  ...       fr          70.73
2                   Unit 0065 Box 5052\nDPO AP 27450  94 vE  ...       de           0.95
3              7780 Julia Fords\nNew Stacy, WA 45798  36 vm  ...       es          78.04
4  23012 Munoz Drive Suite 337\nNew Cynthia, TX 5...  20 IE  ...       es          77.82
````

## Checking the amount of rows and columns

There are a couple of ways to do this:

We can use the `columns` function to return the number of columns in the dataframe:
````python
len(ecom.columns)
````

Then we can use the `index` function along with the `len` function to return the number of rows in the data frame:

````python
len(ecom.index)
````

Another way we can do this is to just use the `info` function.
````python
ecom.info()
````
which returns the following series filled with information about each column and the number of entries
````
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10000 entries, 0 to 9999
Data columns (total 14 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Address           10000 non-null  object 
 1   Lot               10000 non-null  object 
 2   AM or PM          10000 non-null  object 
 3   Browser Info      10000 non-null  object 
 4   Company           10000 non-null  object 
 5   Credit Card       10000 non-null  int64  
 6   CC Exp Date       10000 non-null  object 
 7   CC Security Code  10000 non-null  int64  
 8   CC Provider       10000 non-null  object 
 9   Email             10000 non-null  object 
 10  Job               10000 non-null  object 
 11  IP Address        10000 non-null  object 
 12  Language          10000 non-null  object 
 13  Purchase Price    10000 non-null  float64
dtypes: float64(1), int64(2), object(11)
memory usage: 1.1+ MB
None
````


## What is the average Purchase Price?
This can be easily done in one line:
````python
ecom['Purchase Price'].mean()
````

## What were the highest and lowest purchase prices?
For the max, we can do
````python
ecom['Purchase Price'].max()
````
which returns the value 
and for the min we can do 99.99.
````python
ecom['Purchase Price'].min()
````
which returns the float  0.0.

## How many people have English 'en' as their Language of choice on the website?

````python
ecom[ecom['Language'] == 'en']['Language'].value_counts()
````

## How many people have the job title of "Lawyer"?


````python
ecom[ecom['Job'] == 'Lawyer']['Job'].value_counts()
````
````
Lawyer    30
Name: Job, dtype: int64
````

If just want the number and not a series, we can just use the `count()` function; that is, 
````python
ecom[ecom['Job'] == 'Lawyer']['Job'].count()
````



## How many people made the purchase during the AM and how many people made the purchase during PM?

We can easily do this by typing the following:

````python
ecom[ 'AM or PM'].value_counts()
````
which returns the following series:
````
PM    5068
AM    4932
Name: AM or PM, dtype: int64
````

## What are the 5 most common Job Titles?

````python
ecom['Job'].value_counts().head(5)
````
which return the following series:
````
Interior and spatial designer    31
Lawyer                           30
Social researcher                28
Purchasing manager               27
Designer, jewellery              27
Name: Job, dtype: int64
````

Observe that the default ordering of the series above is in an ascending order.
## Someone made a purchase that came from Lot: "90 WT". What was the purchase price for this transaction?   
We can do this by typing the following:
````python
ecom[ecom['Lot'] == '90 WT']['Purchase Price']
````
which returns the following:
````
513    75.1
Name: Purchase Price, dtype: float64
````

## What is the email of the person with the following Credit Card Number: "4926535242672853"

````python
ecom[ecom['Credit Card'] == 4926535242672853]['Email']
````

````
1234    bondellen@williams-garza.com
Name: Email, dtype: object
````

## How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?

We can do this by typing the following code:
````python
ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95 )  ]['CC Provider'].value_counts()
````
````
Address             39
Lot                 39
AM or PM            39
Browser Info        39
Company             39
Credit Card         39
CC Exp Date         39
CC Security Code    39
CC Provider         39
Email               39
Job                 39
IP Address          39
Language            39
Purchase Price      39
dtype: int64
````

We can also get the same result by using the `index()` function 
````python
ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95 )  ]['CC Provider'].index()
````



## Hard: How many people have a credit card that expires in 2025?

First, we need to create a function that returns the credit cards whose expiration dates expires in 2025. We can do this by defining the following function:
````python
def getExp (x):
    if '25' in x.split('/'):
        return True
    else:
        return False
````

We can pass this function into our filter function whilst passing in our `CC Exp Date` column. Hence, we have
````python
len(list(filter(getExp, ecom['CC Exp Date'])))
````
which outputs the following amount

````
1033
````
Another way to do this is to pass in the column and use the `iloc` function which can be done in the following way:

````python
ecom['CC Exp Date'].iloc[0][3:]
````
Just like our first method, we will use the the `apply()` function with a lambda expression to apply this for every row in the `CC Exp Date` column. Hence, we have the following:
````python
ecom['CC Exp Date'].apply(lambda exp: exp[3:] == '25')
````
To get the number of credit cards that expires in 2025, we can pass in the expression above into the `sum()`. This returns `1033`.




##  Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)

First, we need to split the strings associated with every customer's email and store the email host name. We can do this by defining the following function:
````python
def getHost(x):
    return x.split("@")[1]
````
Next, we want to create a new column with rows containing the email host providers. We can do this by using  the `apply()` function to the `Email` column of our data frame and passing in our `getHost()` function:
````python
ecom['Email Host'] = ecom['Email'].apply(getHost)
````
Then we can print out our results by using `value_counts()` and `head()` function:
````python
print(
    ecom['Email Host'].value_counts().head(5)
)
````
which returns the following series:
````
hotmail.com     1638
yahoo.com       1616
gmail.com       1605
smith.com         42
williams.com      37
Name: Email, dtype: int64
````
We can shorten the code above by using a lambda expression instead; that is, 
````python
ecom['Email Host'] = ecom['Email'].apply(
    lambda x: x.split('@')[1]
    )
````

