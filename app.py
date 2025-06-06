import streamlit as st
import pandas as pd

# ฟังก์ชันโหลดข้อมูลจาก Google Sheets แบบ CSV
@st.cache_data
def load_data():
    sheet_url = "https://docs.google.com/spreadsheets/d/1tfNywRmEf-SYwCXMRXXhXU9NRAhKxsv7zaSBwjGxxF4/export?format=csv&gid=630269328"
    df = pd.read_csv(sheet_url)
    return df

st.title("เว็บเทียบโคมไฟ Ligman")

df = load_data()

# แสดงข้อมูลตารางทั้งหมด (สำหรับตรวจสอบ)
st.subheader("ข้อมูลโคมทั้งหมด")
st.dataframe(df)

# เลือกโคมเพื่อเทียบ
options = df['Product Code'].unique()
selected = st.multiselect("เลือก Product Code เพื่อเทียบ (เลือกได้หลายตัว)", options)

if selected:
    selected_df = df[df['Product Code'].isin(selected)]
    st.subheader("ข้อมูลโคมที่เลือก")
    st.dataframe(selected_df)
else:
    st.info("กรุณาเลือก Product Code เพื่อแสดงข้อมูลเทียบ")
