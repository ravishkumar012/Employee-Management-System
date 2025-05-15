import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import mysql.connector
from datetime import date
import random
import ty
import matplotlib.pyplot as plt

# Initialize login state
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

def login_authentication():
    st.title("🔐Login Page !" )
    st.write("Welcome! Please log in to continue")
    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")
    login_btn = st.button("Login")
    check = True if username and password else False

    if login_btn and check:
        try:
            mydb = mysql.connector.connect(
                username='sql12773535',
                password='T5keKr2YFk',
                host='sql12.freesqldatabase.com',
                database='sql12773535'
            )
            cur = mydb.cursor()
            cur.execute("SELECT * FROM user_password WHERE username = %s", (username,))
            result = cur.fetchall()
            if len(result) < 1:
                st.error("❌ Invalid username or password")
            else:
                stored_password = str(result[0][6])
                if stored_password == password:
                    st.success("✅ Login Successful! 🎉")
                    st.session_state.is_logged_in = True
                    return (True,result[0][1])
                else:
                    st.error("❌ Invalid username or password")
        except mysql.connector.Error as err:
            st.error(f"❌ Database connection failed: {err}")
    elif login_btn:
        st.error("Fill in the blanks.. !⚠️")
    return False

def connect_database():
    try:
        mydb = mysql.connector.connect(
            username='sql12773535',
            password='T5keKr2YFk',
            host='sql12.freesqldatabase.com',
            database='sql12773535'
        )
        cur = mydb.cursor()
        return (mydb, cur)
    except mysql.connector.Error as err:
        st.error(f"❌ Database connection failed: {err}")
        st.stop()

st.set_page_config(page_title='Dashboard', page_icon='🫂')

# Authenticate
if not st.session_state.is_logged_in:
    login = login_authentication()


if st.session_state.is_logged_in:
    st.markdown("""<style>img{margin-top:-35px;}#edunet-foundation-employee-list{margin-top:-70px;} .st-emotion-cache-ocsh0s{color:green;}</style>""", unsafe_allow_html=True)

    with st.sidebar:
        st.sidebar.image('logo.jpg', width=700)
        st.markdown("""
        <style>
        .title{font-size:15px;color:#4CAF50;font-weight:bold;text-align:center;margin-top:-13px;color:orange;}
        </style>
        <div class="title">Welcome to Dashboard !😊</div>
        """, unsafe_allow_html=True)
        # st.markdown(f"Welcome {user_name} !😊",unsafe_allow_html=True)

        selected = option_menu(
            "Details",
            ["Dashboard", "Add Employee", "Edit Employee", "Remove", "Search", "Salary Analysis", "Department analysis"],
            icons=["", "person-plus", "pencil-square", "x", "search", "cash", "bar-chart"],
            menu_icon="cast",
            default_index=0
        )

    st.markdown("# Edunet Foundation Employee List")
    st.markdown("---")

    if selected == "Dashboard":
        st.image('mitt.jpg',width=1300)
        home_url = "https://emp-system.streamlit.app/"
        st.markdown(f"""
            <a href="{home_url}" target="_self">
                    <button class="one">Home page</button>
                    </a>
                """, unsafe_allow_html=True)

    elif selected == "Add Employee":
        st.title("🧑‍💼 Employee Details")

        with st.form("employee_form",clear_on_submit=True):
            st.subheader("Please fill in the following information:")

            name = st.text_input("Full Name")
            age = st.text_input("Age")
            department = st.selectbox("Department", ["HR", "Finance", "Engineering", "Sales", "Marketing", "Other"])
            position = st.text_input("Position")
            salary = st.text_input("Salary")

            address = st.text_area("Address")
            contact_number = st.text_input("Contact Number")
            email = st.text_input("Email")
            marital_status = st.selectbox("Marital Status", ["Unmarried", "Married"])
            start_date = st.date_input("Job Start Date", value=date.today())

            submitted = st.form_submit_button("Submit")

            if submitted:
                empid = random.randint(10000,99999)
                if name and position and address and contact_number and email:
                    st.success("Employee details submitted successfully!")
                    st.write("### Submitted Information:")
                    st.write(f"Name: {name}")
                    st.write(f"Age: {age}")
                    st.write(f"Department: {department}")
                    st.write(f"Position: {position}")
                    st.write(f"Salary: {salary}")
                    st.write(f"Address: {address}")
                    st.write(f"Contact Number: {contact_number}")
                    st.write(f"Email: {email}")
                    st.write(f"Marital Status: {marital_status}")
                    st.write(f"Job Start Date: {start_date}")
                    st.success(f"Your Employee ID:{empid}.  \n\nPlease note these details for furture use")
 
                    c = connect_database()  
                    if not c:
                        st.error("Database connection failed !⚠️") 
                    else:
                        mydb,cur = c
                        query = "INSERT INTO emp_data(empid,name,age,department,position,salary,address,mobile,email,merital_status,start_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"         
                        start_date=str(start_date)
                        marital_status=True if marital_status=="Married" else False
                        salary = float(salary)
                        data = (empid,name,age,department,position,salary,address,contact_number,email,marital_status,start_date)
                        cur.execute(query,data)
                        mydb.commit()
                        cur.close()
                        mydb.close()
                else:
                    st.warning("Please fill in all required fields before submitting.")


    elif selected == "Edit Employee":
        if "edit_emp_data" not in st.session_state:
            st.session_state.edit_emp_data = None
        if "emp_id_searched" not in st.session_state:
            st.session_state.emp_id_searched = None
        # code continues from edit section
        st.title("✏ Edit Employee Information")

        

        # col1, col2 = st.columns([5, 2])
        # with col2:
        emp_id = st.text_input("Search by Employee ID", key="search_id")
        search = st.button("Search")
        # if search:
        st.error("✏ Edit Employee Information is currently not working !❌")
        if search:

            c = connect_database()
            if not c:
                st.error("Database connection Failed !⚠️")
            else:
                mydb, cur = c
                emp_id = int(emp_id)
                query = f"SELECT * FROM emp_data WHERE empid = {emp_id}"

                try:
                    cur.execute(query)
                    data = cur.fetchall()
                    cur.close()
                    mydb.close()

                    if data:
                        st.session_state.edit_emp_data = data[0]
                        st.session_state.emp_id_searched = emp_id
                    else:
                        st.warning("No employee found with that ID.")
                except Exception as e:
                    st.error(f"Some Error: {e}")


            if st.session_state.edit_emp_data:
                data = st.session_state.edit_emp_data
                emp_id = st.session_state.emp_id_searched
                with st.form("Edit Employee Data"):
                    name = st.text_input("Full Name", value=data[1])
                    age = st.text_input("Age", value=data[2])
                    department = st.selectbox("Department", ["HR", "Finance", "Engineering", "Sales", "Marketing", "Other"])
                    st.write("Old Department:", data[3])
                    position = st.text_input("Position", value=data[4])
                    salary = st.text_input("Salary", value=data[5])
                    address = st.text_area("Address", value=data[6])
                    contact_number = st.text_input("Contact Number", value=data[7])
                    email = st.text_input("Email", value=data[8])
                    marital_status = st.selectbox("Marital Status", ["Unmarried", "Married"])
                    st.write("Old Marital Status:", "Married" if data[9] else "Unmarried")
                    start_date = st.date_input("Job Start Date", value=data[10])

                    submit = st.form_submit_button("Submit")
                    # submit=True
                    if submit:
                        marital_status = 1 if marital_status == "Married" else 0
                        start_date = str(start_date)
                        salary = float(salary)
                        st.success("done")
                        c = connect_database()
                        if not c:
                            st.error("Database connection Failed !⚠️")
                        else:
                            mydb, cur = c
                            update_query = """
                                UPDATE emp_data
                                SET name=%s, age=%s, department=%s, position=%s, salary=%s,
                                    address=%s, mobile=%s, email=%s, merital_status=%s, start_date=%s
                                WHERE empid=%s
                            """
                            data_to_update = (name, age, department, position, salary, address,
                                            contact_number, email, marital_status, start_date, emp_id)
                            cur.execute(update_query, data_to_update)
                            mydb.commit()
                            cur.close()
                            mydb.close()
                            st.success("Information Updated Successfully! ✅")
                            st.session_state.edit_emp_data = None  # Clear session after update
                    else:
                        st.error("no")
            else:
                st.error("Some Error occured !❌")
    elif selected == "Remove":
        # st.error("🗑 Remove Employee currently not working !❌")

        st.title("🗑 Remove Employee")

        col1, col2, col3 = st.columns([5, 2, 1])
        with col3:
            emp_id = st.text_input("Search by Emp ID", key="search_id")
            search = st.button("Search",disabled=True)
        st.error("🗑 Remove Employee currently not working !❌")
        employee_db={}
        if search:

            if emp_id in employee_db:
                emp = employee_db[emp_id]

                st.success(f"Employee found: {emp_id}")
                st.write("### Employee Details:")
                st.write(f"Name: {emp['name']}")
                st.write(f"Department: {emp['department']}")
                st.write(f"Position: {emp['position']}")
                st.write(f"Email: {emp['email']}")
                st.write(f"Contact: {emp['contact_number']}")
                st.write(f"Start Date: {emp['start_date']}")

                if st.button("🚨 Confirm Remove"):
                    del employee_db[emp_id]
                    st.success(f"Employee {emp_id} has been removed from the system.")
            else:
                st.error("Employee ID not found. Please try again.")
    elif selected == "Search":
        st.title("🔍Search Employee")

        col1, col2, col3 = st.columns([5, 2, 1])
        with col3:
            emp_id = st.text_input("Search by Emp ID", key="search_id")
            search = st.button("Search")

        if search:
            c = connect_database()
            if not c:
                st.error("Database connection Failed !⚠️")
            else:
                mydb, cur = c
                emp_id = int(emp_id)
                query = f"SELECT * FROM emp_data WHERE empid = {emp_id}"

                try:
                    cur.execute(query)
                    data = cur.fetchall()
                    st.write(f"Emloyee ID: {data[0][0]}")
                    st.write(f"Name: {data[0][1]}")
                    st.write(f"Age: {data[0][2]}")
                    st.write(f"Department: {data[0][3]}")
                    st.write(f"Position: {data[0][4]}")
                    st.write(f"Salary: {data[0][5]}")
                    st.write(f"Address: {data[0][6]}")
                    st.write(f"Mobile No.: {data[0][7]}")
                    st.write(f"Email: {data[0][8]}")
                    m = "Married" if data[0][9] else "Unmarried"
                    st.write(f"Marital Status: {m}")
                    st.write(f"Job Start Date: {data[0][10]}")
                    cur.close()
                    mydb.close()
                except Exception as e:
                    st.error(f"Some Error:{e}")

    elif selected == "Salary Analysis":
        # salary analysis
        c = connect_database()
        if not c:
            st.error("Database connection Failed !⚠️")
        else:
            mydb, cur = c
            query = "SELECT salary FROM emp_data"
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            mydb.close()
            data1 = [float(e[0]) for e in data]

            st.success(f"Total Number of employee:{len(data)}")
            y = ["Low","Medium","High"]
            x = ty.analyse(data1)
            ex = [0.1,0.0,0.0]
            c=["g","b","r"]

            plt.pie(x,labels=y,explode=ex,colors=c,autopct="%0.1f%%",radius=0.8)
            st.pyplot(plt)
            st.markdown("## Employee salary analysis")


    elif selected == "Department analysis":
        # department analysis
        c = connect_database()
        if not c:
            st.error("Database connection Failed !⚠️")
        else:
            mydb, cur = c
            query = "SELECT department FROM emp_data"
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            mydb.close()
            data1 = [str(e[0]) for e in data]
            st.success(f"Total Number of employee:{len(data)}")

            depart_list=["HR","Finance","Engineering","Sales","Marketing","Other"]

            x = ty.analysis1(data1)
            ex = [0.0,0.0,0.0,0.0,0.0,0.0]
            c = ["r","g","b","y","m","c"]

            fig, ax = plt.subplots()
            ax.pie(x, labels=depart_list, colors=c, autopct="%0.1f%%", radius=0.8)
            st.pyplot(fig)

            st.markdown("## Employee Department Analysis !")
