import pandas as pd
import streamlit as st
import numpy as np

st.title('Sangai Honda Reports')
st.divider()
"""
##  Service Revenue for the Month of  - October 2024
"""
#st.divider()

#st.markdown(""" :green[*This website will show the reports of revenues from sales, service*]     
 #           :red[**This will be visible only to authenticated users!**]  
 #           :rainbow[***Cool!!***.]""")

st.divider()

# Read the CSV File
df = pd.read_csv('October_2024.csv')

# Set the display option for max columns
pd.set_option('display.max_columns',50)

# if one wants to see the whole data imported from the CSV file. There are 47 columns
# print(df)
#print df.info()


# Remove the unwanted columns - number of columns removed - 31
df1 = df.drop(columns = df.columns[[0,1,2,3,4,9,14,16,17,19,20,21,23,24,29,30,31,32,33,34,35,36,37,39,40,41,42,43,44,45,46]])

#The  number of columns left is 16
# df1.info()

# There are NaN values in the some of the rows of these 16 columns. We replace the values with zero which enables us to do calculations.
df1.fillna(0, inplace = True)

# We export the "Cleaned data". 16 columns and no NaN values.
#df1.to_excel('Cleaned_data_October_2024.xlsx')

######### THIS IS WHERE THE ANALYSIS BEGINS   ##########


# We create a pivot table and get summation values of Labor, Parts, Discount and BP Insurance. They are then segregated with RO Type and then by Labor/Parts.
#Summary_Labor_month = df1.pivot_table(index = ['RO Type'], values = ['Net Labor Amt','Net Parts Amt','BP Insurance Amount','Net Discount Amount'], aggfunc='sum', margins = True, margins_name = 'Total', sort = True)

Summary_Labor_month = df1.pivot_table(index = ['RO Type'], values = ['Net Labor Amt','Net Parts Amt', 'BP Insurance Amount'], aggfunc='sum', margins = True, margins_name = 'Total', sort = True)


Net_Labor_Amt = df1.pivot_table(index = ['RO Type'], values = ['Net Labor Amt'], aggfunc='sum', margins = True, margins_name = 'Total', sort = True)

Net_Parts_Amt = df1.pivot_table(index = ['RO Type'], values = ['Net Parts Amt'], aggfunc='sum', margins = True, margins_name = 'Total', sort = True)

Insurance_Amt = df1.pivot_table(index = ['Type'], values = ['BP Insurance Amount'], aggfunc='sum', margins = True, margins_name = 'Total', sort = True)


# We round off to two decimal points and rename it

x1 = Summary_Labor_month.round(0)

x2 = Net_Labor_Amt.round(0)

x3 = Net_Parts_Amt.round(0)

x4 = Insurance_Amt.round(0)



#st.dataframe(x1)
#st.write(x1)

#st.dataframe(x3)

col1,col2,col3= st.columns(3, gap = "large", vertical_alignment="bottom")

with col1:
    st.header("Labor Revenue")
    st.dataframe(x2)
    st.bar_chart(x2)

with col2:
    st.header(" Parts Revenue")
    st.dataframe(x3)
    st.bar_chart(x3)
with col3:
    st.header("Insurance Revenue")
    st.dataframe(x4)
    st.bar_chart(x4)


st.divider()

# We get a table of 4 columns and 7 seven rows including the Total row
#Summary_Labor_month.info()
# Draw a line chart for the data
#x1.plot.bar()
#st.write(x1.plot.bar())

#st.bar_chart(x1)


# We write some summary of the data shown in the bars

st.write("""*The Service  Summary -* """)

x11 = x1.iloc[3,1]

f"-- Net Labor Amount is {x11} "

st.write( "-- Net Labor Amount is ", x11)
st.write( "-- Net Parts Amount is ", x1.iloc[3,2])
st.write( "-- BP Insurance Amount is ", x1.iloc[3,0])
st.write( "-- Total Service Revenue for the month is ", (x1.iloc[3,1] + x1.iloc[3,0] + x1.iloc[3,2]).round(0) )
         
#print(x1[4,1])
st.divider()

Summary_Part_month = df1.pivot_table(index = ['Part Type'], values = ['Net Parts Amt'], aggfunc='sum', margins = True, margins_name = 'Total', sort = True)

#Summary_Part_Insurance = df1.pivot_table(index = ['Part Type'], values = ['BP Insurance Amount'], aggfunc='sum', margins = True, margins_name = 'Total', sort = True)


""" ## Parts Summary """
col4,col5 =st.columns(2)

with col4:
    st.dataframe(Summary_Part_month.round(0))

with col5:
    st.bar_chart(Summary_Part_month.round(0),horizontal=True)

#st.dataframe(Summary_Part_Insurance.round(2))

st.divider()






st.write("""*The Parts Summary -* """)

st.write( "-- Accessories Amount is ", Summary_Part_month.round(2).iloc[1,0])
st.write( "-- BP Parts Amount is ", Summary_Part_month.iloc[2,0])
st.write( "-- PM Parts Amount is ", Summary_Part_month.iloc[6,0])
st.write( "-- GR Parts Amount is ", Summary_Part_month.iloc[4,0])
#st.write( "-- BP Insurance Amount is ", x1.iloc[3,0])
#st.write( "-- Total Parts Revenue for the month is ", (x1.iloc[3,1] + x1.iloc[3,0] + x1.iloc[3,2]).round(2) )


st.divider()

Paint_Labor_month = df1.pivot_table(index = [df1['Description'].str.contains('PAINT'),], 
                                    values = ['Net Labor Amt', 'BP Insurance Amount','Net Parts Amt'], aggfunc='sum', fill_value = 0,
                                    margins = True, margins_name = 'Total', sort = True)
st.dataframe(Paint_Labor_month.round(2))
