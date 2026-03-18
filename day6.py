m=int(input("enter number of values to be taken"))
num=[0]*m

for i in range(m):
    num[i]=int(input("enter number: "))

cate={
    "invalid":[i for i in num if i<=0],
    "normal":[i for i in num if i>0 and i<=500],
    "large":[i for i in num if i>500 and i<=2000],
    "high_risk":[i for i in num if i>2000],
}

valid=[i for i in num if i>0]
freq=len(valid)

total=0
for i in valid:
    total=total+i

if len(num)>5:
    print("Frequent Transactions")

if total>5000:
    print("Large Spending")

if len(cate["high_risk"])>=3:
    print("Suspicious Pattern")

risk="Low Risk"

if freq>4 and total>3000:
    risk="High Risk"
elif freq>3 or total>2500 or len(cate["high_risk"])>=3:
    risk="Moderate Risk"

print("Invalid:",cate["invalid"])
print("Normal:",cate["normal"])
print("Large:",cate["large"])
print("High Risk:",cate["high_risk"])

print("Total transaction value:",total)
print("Number of transactions:",len(num))
print("Risk Classification:",risk)

summary=(len(num),freq,total,risk)
print("Summary:",summary)
