from fastapi import FastAPI,HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel


class Expense(BaseModel):
   amount:float
   category:str
   notes:str

class AnalyticsRequest(BaseModel):
   start_date:date
   end_date:date


app=FastAPI()

@app.get("/expenses/{expense_date}",response_model  = List[Expense])

def get_expenses(expense_date:date):
   expenses=db_helper.fetch_records_for_date(expense_date)
   return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date:date,expenses:List[Expense]):
   db_helper.delete_expenses_for_date(expense_date)
   for expense in expenses:
      db_helper.insert_expense(expense_date,expense.amount,expense.category,expense.notes)
   return {"message":"Expenses updated successfully"}

@app.post(f"/analytics")
def get_expenses_between_dates(request:AnalyticsRequest):
    expenses=db_helper.fetch_expenses_between_dates(request.start_date,request.end_date)
    if expenses is None:
       raise HTTPException(status_code = 500,detail="Failed to retrieve expense summary from the database")

    breakdown = {}
    sum=0
    for row in expenses:
       sum+=row['total']
    for row in expenses:
       percentage = (row['total']/sum)*100
       breakdown[row['category']] = {"total":row['total'],'percentage':percentage}
   
    return breakdown


@app.get(f'/analytics_months')
def get_expenses_months():
   data = db_helper.monthly_expenses()
   return data