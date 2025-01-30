# expensetracker
## Features:  
✅ **Add Expense** – Store date, category, amount, and description.  
✅ **View Expenses** – Display all recorded expenses in a tabular format.  
✅ **Delete Expense** – Remove an expense by selecting its index.  
✅ **Calculate Total Expenses** – Sum up all expenses and display the total.  
✅ **Data Persistence** – Save expenses in a CSV file for future use.  

## Algorithms:  

1. **Load Expenses** (At startup)  
   - If `expenses.csv` exists, read data and store it in a list.  
   - Else, create an empty list for expenses.  

2. **Add Expense**  
   - Get input (date, category, amount, description).  
   - Append it to the expense list.  
   - Save the updated list to `expenses.csv`.  

3. **View Expenses**  
   - Read expenses from the list.  
   - Display them in a formatted table.  

4. **Delete Expense**  
   - Display expenses with an index.  
   - Get the index from the user.  
   - Remove the selected expense from the list.  
   - Save the updated list to `expenses.csv`.  

5. **Calculate Total Expenses**  
   - Loop through all expenses.  
   - Convert amounts to float and sum them up.  
   - Display the total amount spent.  

Let me know if you need more details! 🚀
