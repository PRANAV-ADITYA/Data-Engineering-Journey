import streamlit as st 
from datetime import datetime 
import requests
import pandas as pd
st.title("Expense Management System")




API_URL = "http://127.0.0.1:8000/"

tab1 , tab2,tab3 = st.tabs(['Add/Update','Analytics by Category','Analytics by months'])

categories = ['Rent','Food','Shopping','Entertainment','Other']

with tab1:
    selected_date = st.date_input("Enter the date: ",datetime(2024,8,1),label_visibility="collapsed")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")

    if(response.status_code == 200):
       existing_expenses = response.json()
    else:
        st.error("Failed to retrieve expenses")
        existing_expenses = []

    with st.form(key="expense_form"):

        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("Amount")
        with col2:
            st.subheader("Category")
        with col3:
            st.subheader("Notes")


        expenses = []

        for i in range(len(existing_expenses)):
            amount = existing_expenses[i]['amount']
            category = existing_expenses[i]['category']
            notes = existing_expenses[i]['notes']
            
    
            col1,col2,col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label = "Amount",min_value=0.0,step =1.0,value = amount ,key=f'amount_{i}',label_visibility = "collapsed")
            with col2:
                category_input = st.selectbox(label = "Category",options = categories,index = categories.index(category),key = f"category_{i}",label_visibility = "collapsed")
            with col3:
               notes_input =  notes_input = st.text_input(label="notes",value=notes,key=f"notes_{i}",label_visibility = "collapsed")
            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes':notes_input
            })

        submit_button =  st.form_submit_button()
        if(submit_button):
            requests.post(f'{API_URL}/expenses/{selected_date}',json = expenses)
            if response.status_code==200:
                st.success("expenses updated successfully")
            else:
                st.error("Failed to update expenses")


with tab2:
    col1,col2= st.columns(2)
    with col1:
        start_date = st.date_input("Enter the start date: ",datetime(2024,8,1))
    with col2:
        end_date = st.date_input("Enter the end date: ",datetime(2024,8,1))
    if(st.button("Get Analytics")):
        payload = {'start_date':start_date.strftime("%Y-%m-%d"),'end_date':end_date.strftime("%Y-%m-%d")}
        response = requests.post(f'{API_URL}/analytics',json=payload)
        response = response.json()

        df=pd.DataFrame({
            "Category":list(response.keys()),
            "Total":[response[category]['total'] for category in response],
            'Percentage':[response[category]['percentage'] for category in response]
        })
  
        df_sorted = df.sort_values(by="Percentage",ascending=False)

        st.title("Expense Breakdown By Category")
        st.bar_chart(data=df_sorted.set_index("Category")['Percentage'])
        st.table(df_sorted)

with tab3:
    response = requests.get(f'{API_URL}/analytics_months')
    response = response.json()

    df = pd.DataFrame({
        'Month':[dt['month'] for dt in response],
        'Total':[dt['total'] for dt in response]
    })

    df_sorted = df.sort_values(by="Month")

    st.bar_chart(data=df_sorted.set_index('Month'))

    st.table(df_sorted)