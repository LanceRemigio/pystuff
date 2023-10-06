import pandas as pd  

ecom = pd.read_csv('Ecommerce Purchases')


# print(ecom['CC Provider'])

def getExp(x):
    if '25' in x.split('/'):
        return True
    else:
        return False

def getHost(x):
    return x.split("@")[1]

ecom['Email Host'] = ecom['Email'].apply(getHost)

print(
        ecom['Email Host'].value_counts().head(5)
        )



# print(
#         len(list(filter(getExp, ecom['CC Exp Date'])))
#         )




