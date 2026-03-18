Smart Transaction Risk Detector

Problem Understanding
This problem is about analyzing a list of transaction amounts made by a user in a day. Each transaction is classified into categories like normal, large, high risk, or invalid based on its value. After classification, patterns such as frequent transactions, large spending, and suspicious activity are checked. Finally, the program decides whether the user is low, moderate, or high risk.

Logic / Approach Used
First, I took input values from the user and stored them in a list. Then, I used list comprehension to classify transactions into different categories and stored them in a dictionary. I separated valid transactions (greater than 0) and calculated their total using a loop.

After that, I checked conditions for frequent transactions, large spending, and suspicious patterns. For risk classification, I used a personalized scoring method based on my roll number (591). I assigned weights to different conditions such as frequency, total amount, and high risk transactions. Based on the final score, the risk level is decided.

Test Cases

Test Case 1
Input: 4, 50, 100, 200, 300
Output: Low Risk, no suspicious patterns

Test Case 2
Input: 6, 2500, 3000, 4000, 100, 200, 300
Output: High Risk, suspicious pattern, large spending

Reflection
The main decision I made was to use a scoring system instead of fixed conditions. I used my roll number to assign weights to different factors. This makes the program more flexible and different from standard solutions.
