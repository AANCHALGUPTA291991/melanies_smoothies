# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(":cup_with_straw: Customize your smoothie :cup_with_straw:")
st.write(
    """Choose the fruits you want in your smoothie"""
)
from snowflake.snowpark.functions import col

session= get_active_session()
my_data_frame= session.table("smoothies.public.fruit_options").select (col('FRUIT_NAME'))   
st.dataframe(data=my_data_frame, use_container_width=True)

ingredients_List = st.multiselect
('Choose upto 5 ingredients:'
 , my_data_frame)
