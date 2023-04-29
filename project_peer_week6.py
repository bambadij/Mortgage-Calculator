#-----Azubi Store --------
# Calculate the total Price average for all products
products =["Sankofa Foods","Jamestown Coffee",
"Bioko Chocolate","Blue Skies Ice Cream",
"Fair Afric Chocolate","Kawa Moka Coffee",
"Aphro Spirit", "Mensado Bissap", "Voltic"]

prices =[30,25,40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]
average = sum(prices)/len(products)
print(f"the total price average for all products is : {round(average,2)}")
#-create a new price list that reduces the old prices by GHC5
new_price_reduce = [-5 +x for x in prices]

print(f"The new price that reduces the old prices by GHC5 are :{new_price_reduce}")

# -calculate the total revenue generated from the products
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]
revenu =[]
for r in range(len(new_price_reduce)):
    revenu.append(new_price_reduce[r]*last_week[r])
print(f"the total revenue generated from the products is : {sum(revenu)} GHC")
    
# based on the new prices, which products are less than GHC30 
dict_new_pro={}
for n in range(len(new_price_reduce)):
    dict_new_pro[products[n]]=new_price_reduce[n]

for x,y in dict_new_pro.items():
    if y < 30 :
        print(x,y)
