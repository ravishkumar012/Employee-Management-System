import streamlit as st
import pathlib
from streamlit_option_menu import option_menu
from PIL import Image
selector='home'
import pandas as pd
from datetime import datetime
import random
import mysql.connector


st.session_state.page=selector

st.set_page_config(page_title="Edunet Foundation", page_icon="logo.jpg", layout="centered")

    
def login_button():
    login_url = "https://emp-system1.streamlit.app/"

    st.markdown(f"""
        <a href="{login_url}" target="_self">
            <button style='padding:10px 20px; font-size:16px; background-color:#4CAF50; color:white; border:none; border-radius:5px;'>Go to Login Page</button>
        </a>
    """, unsafe_allow_html=True)


def click():

    st.markdown("""<style>
             img
                {
                margin-top:10px;
                }        </style>
""",unsafe_allow_html=True)
    st.markdown("## Employee Management System")


st.markdown("""
<style>
            #employee-management-system
            {
            color:blue;
            margin-left:120px;
            margin-top:-50px;}
            img
            {
            background-color:black;
            margin-top:-25px;
            border:1px solid black;}
            img:hover
            {
                box-shadow: 2px 2px 15px purple;
            border:2px solid green;
            }
            </style>""",unsafe_allow_html=True)

with st.sidebar:
    st.sidebar.image('logo.jpg',width=700)
    selected=option_menu(
    "Main Menu",
        ["Home","About", "Services", "Events", "Carrier", "FAQ", "Contact","Login","Forgot password","Create account","Developed by"],
        icons=["house","person-circle", "tools", "calendar", "graph-up", "question-circle", "person-lines-fill","box-arrow-in-right","key","person","person	"],
        menu_icon="cast",
        default_index=0,
    )

# st.markdown("## Employee Management System")
# st.markdown("---")

# ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ

if selected=="Home":
    click()
    st.image('',width=1300)
    st.markdown("""
    <style>
                .two            {
                padding:9px 19px; font-size:16px; background-color:grey; color:white; border:none; border-radius:5px;
                }
                .three
                {
                padding:9px 20px; font-size:16px; background-color:grey; color:white; border:none; border-radius:5px;
                margin-top:20px;
                }
                .four:hover
                {
                background-color:#4CAF50;
                border:2px solid orange;
                }</style>""",unsafe_allow_html=True)
    st.markdown("""
        <a href="https://edunetfoundation.org/" target="_self">
                <button class="three four">Visit Official Website</button>
            </a>
        """, unsafe_allow_html=True)
elif selected == "About":

    # st.set_page_config(
    #     page_title='About us',
    #     page_icon='logo.jpg',
    #     layout='centered'
    # )
    st.markdown("""
    <style>
    .title{
        font-size:40px;
        color:#4CAF50;
        font-weight:bold;
        text-align:center;
                margin-top:-30px;
    }
    </style>
    <div class="title">🎓 About Edunet Foundation
    </div>
    """,unsafe_allow_html=True)
# # image = Image.open("logo.jpg")
# # st.image(image,width=300)


    st.markdown("""

    1. Edunet Foundation is a non-profit organization dedicated to empowering youth through technology and education.  
    2. It was established in 2015 with the mission to make future-ready skills accessible to all learners.  
    3. The foundation collaborates with industry leaders like Intel, Microsoft, and NASSCOM.  
    4. Edunet delivers programs focused on emerging tech like AI, cloud computing, cybersecurity, and digital literacy.  
    5. Its initiatives are designed to bridge the gap between academia and industry expectations.  
    6. The foundation works closely with schools, colleges, and skilling institutions across India.  
    7. It promotes inclusive learning, aiming to reach underprivileged and rural students.  
    8. Their programs use hands-on learning and real-world problem-solving to build practical skills.  
    9. Edunet also supports faculty development and entrepreneurship among students.  
    10. With a vision for a digitally skilled India, Edunet Foundation continues to transform education and employability.
    """)
 
    st.markdown("""    
        <a href="https://edunetfoundation.org/about-us/" >
                <button class="six"
                >Official Website</button>
            """, unsafe_allow_html=True)
elif selected=="Services":
    # import streamlit as st

    st.title("Edunet Foundation Services")
    st.markdown("""

    <h3 style='color: #117A65;'>Empowering Education Through Technology</h3>
    """, unsafe_allow_html=True)

    st.markdown("""
    Edunet Foundation is a not-for-profit organization working to bridge the digital divide 
    and provide accessible, high-quality education to students and educators across India.  
    We collaborate with academic institutions, industries, and government bodies to design 
    and deliver impactful educational programs, including:

    - 📚 Teacher training and development
    - 💻 Digital learning content
    - 🤝 Industry-academia collaboration
    - 🧠 AI & emerging tech skilling initiatives
    - 🌍 Outreach to underserved communities

    Our mission is to enable learners of today to become the leaders of tomorrow by harnessing the power of technology and education.
    """)

    st.markdown("""
    <style>
                .two            {
                padding:9px 19px; font-size:16px; background-color:grey; color:white; border:none; border-radius:5px;
                }
                .three
                {
                padding:9px 20px; font-size:16px; background-color:grey; color:white; border:none; border-radius:5px;
                margin-top:20px;
                }
                .four:hover
                {
                background-color:#4CAF50;
                border:2px solid orange;
                }</style>""",unsafe_allow_html=True)
    st.markdown("""
        <a href="https://edunetfoundation.org/" target="_self">
                <button class="three four">Visit Official Website</button>
            </a>
        """, unsafe_allow_html=True)
    
elif selected=="Events":
    # st.set_page_config(page_title="Event Page", layout="centered")

    # Title & Banner
    st.title("🚀 FutureTech Conference 2025")
    st.markdown("Empowering Innovations | April 20–22, 2025 | Virtual Event")
    # st.image("logo.jpg", width=300)
    st.markdown("""
    <style>
                
                img
                {
                margin-top:30px;}
                </style>""",unsafe_allow_html=True)
    # About the Event
    st.header("🎯 About the Event")
    st.write("""
    The FutureTech Conference is a 3-day virtual summit bringing together tech leaders, developers, entrepreneurs, and students 
    to explore emerging technologies such as AI, Blockchain, Web3, and Cybersecurity. 
    Join us for expert sessions, workshops, and networking opportunities!
    """)

    # Schedule
    st.header("📅 Event Schedule")
    schedule = {
        "Day 1 - April 20": ["Opening Keynote", "AI & Ethics", "Startup Pitch Round 1"],
        "Day 2 - April 21": ["Web3 Panel", "Cybersecurity Workshop", "Tech Trivia"],
        "Day 3 - April 22": ["Blockchain Bootcamp", "Startup Finals", "Closing Ceremony"]
    }
    for day, events in schedule.items():
        with st.expander(day):
            for event in events:
                st.markdown(f"- {event}")

    # Speakers
    st.header("🎤 Featured Speakers")
    speakers = [
        {"name": "Shri Vishnu Saran", "topic": "Chairman Sir", "photo": "https://www.mitedu.ac.in/assets/images/Image-2.jpg"},
        {"name": "Dr. Himanshu Sharma", "topic": "Principal Sir", "photo": "https://www.mitedu.ac.in/assets/images/IMG-3282.jpg"},
        {"name": "Dr. Pankaj Sharma", "topic": " Head of the Department (BCA)", "photo": "https://mitmeerut.ac.in/media_image/hodmessage/2024_12_11_04_25_30_572IMG-20241211-WA0012.jpg"},
    ]

    cols = st.columns(len(speakers))
    for idx, speaker in enumerate(speakers):
        with cols[idx]:
            st.image(speaker["photo"], width=150)
            st.subheader(speaker["name"])
            st.caption(speaker["topic"])

    # Registration
    st.header("📝 Register Now")
    with st.form("registration_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        role = st.selectbox("Your Role", ["Student", "Developer", "Entrepreneur", "Educator", "Other"])
        interest = st.multiselect("Interested Topics", ["AI", "Web3", "Blockchain", "Cybersecurity", "Startups"])
        submit = st.form_submit_button("Register")


       

    if submit:
            st.success(f"Thanks for registering, {name}! Check your inbox at {email} for event updates.")

    # Footer
    st.markdown("---")
    st.caption("© 2025 FutureTech Conference. All rights reserved.")


elif selected=="Carrier":

# # Main heading
    st.title("Career Opportunities at Edunet Foundation")

    # Sidebar listing (for visual aid, not interactive)
    st.sidebar.title("Program List")
    st.sidebar.markdown("- Advanced Diploma in IT")
    st.sidebar.markdown("- SkillSaksham Program")
    st.sidebar.markdown("- TechSaksham Program")
    st.sidebar.markdown("- Skills4Future Program")
    st.sidebar.markdown("- CPIT Program")

    # Show all program details
    st.subheader("1. Advanced Diploma in Information Technology")
    st.write("""
    A two-year, full-time NSQF Level 6 diploma conducted in collaboration with the Directorate General of Training (DGT). 
    This program provides comprehensive training in emerging technologies, including cloud computing and artificial intelligence.
    It combines classroom instruction with expert talks, bootcamps, industry visits, and on-the-job training to prepare students for careers in IT.
    """)

    st.subheader("2. SkillSaksham Program")
    st.write("""
    A collaborative initiative between Edunet Foundation, Microsoft, and DGT, aimed at enhancing the skills of ITI and NSTI students across India.
    The program includes training in Microsoft tools, digital literacy, employability skills, artificial intelligence, cybersecurity, and Power BI.
    """)

    st.subheader("3. TechSaksham Program")
    st.write("""
    A joint initiative by Microsoft and Edunet Foundation to upskill female students in Tier 2 & 3 cities with industry-relevant digital skills.
    The program covers web development, cloud computing, AI, and more — with mentorship and career guidance.
    """)

    st.subheader("4. Skills4Future Program")
    st.write("""
    In partnership with Shell India, this program empowers youth in higher and vocational education with green skills through artificial intelligence technologies.
    It prepares students for green jobs and AI-based roles, fostering a future-ready workforce with a focus on sustainability.
    """)

    st.subheader("5. Certificate Program in Information Technology (CPIT)")
    st.write("""
    A joint initiative with IIIT Dharwad and Mindtree Foundation, this 18-month program targets individuals who have exited the formal education system.
    It provides holistic training in basic IT and employability skills, including hands-on projects to bridge the gap between training and employment.
    """)

    if "selected_program" not in st.session_state:
        st.session_state.selected_program = None

    st.title("Career Opportunities at Edunet Foundation")
    st.write("Choose a program from the sidebar to view its details.")
    st.markdown("""
    <style>
                .two            {
                padding:9px 19px; font-size:16px; background-color:grey; color:white; border:none; border-radius:5px;
                }
                .three
                {
                padding:9px 20px; font-size:16px; background-color:grey; color:white; border:none; border-radius:5px;
                margin-top:20px;
                }
                .four:hover
                {
                background-color:#4CAF50;
                border:2px solid orange;
                }</style>""",unsafe_allow_html=True)
    st.markdown("""
        <a href="https://edunetfoundation.org/" target="_self">
                <button class="three four">Visit Official Website</button>
            </a>
        """, unsafe_allow_html=True)

    # Sidebar with buttons
    st.sidebar.title("Select a Program")

    if st.sidebar.button("Advanced Diploma in Information Technology"):
        st.session_state.selected_program = "ADIT"

    if st.sidebar.button("SkillSaksham Program"):
        st.session_state.selected_program = "SkillSaksham"

    if st.sidebar.button("TechSaksham Program"):
        st.session_state.selected_program = "TechSaksham"

    if st.sidebar.button("Skills4Future Program"):
        st.session_state.selected_program = "Skills4Future"

    if st.sidebar.button("Certificate Program in Information Technology (CPIT)"):
        st.session_state.selected_program = "CPIT"

    # Display content based on selection
    if st.session_state.selected_program == "ADIT":
        st.subheader("Advanced Diploma in Information Technology")
        st.write("""
        A two-year, full-time NSQF Level 6 diploma conducted in collaboration with the Directorate General of Training (DGT). 
        This program provides comprehensive training in emerging technologies, including cloud computing and artificial intelligence.
        It combines classroom instruction with expert talks, bootcamps, industry visits, and on-the-job training to prepare students for careers in IT.
        """)

    elif st.session_state.selected_program == "SkillSaksham":
        st.subheader("SkillSaksham Program")
        st.write("""
        A collaborative initiative between Edunet Foundation, Microsoft, and DGT, aimed at enhancing the skills of ITI and NSTI students across India.
        The program includes training in Microsoft tools, digital literacy, employability skills, artificial intelligence, cybersecurity, and Power BI.
        """)

    elif st.session_state.selected_program == "TechSaksham":
        st.subheader("TechSaksham Program")
        st.write("""
        A joint initiative by Microsoft and Edunet Foundation to upskill female students in Tier 2 & 3 cities with industry-relevant digital skills.
        The program covers web development, cloud computing, AI, and more — with mentorship and career guidance.
        """)

    elif st.session_state.selected_program == "Skills4Future":
        st.subheader("Skills4Future Program")
        st.write("""
        In partnership with Shell India, this program empowers youth in higher and vocational education with green skills through artificial intelligence technologies.
        It prepares students for green jobs and AI-based roles, fostering a future-ready workforce with a focus on sustainability.
        """)

    elif st.session_state.selected_program == "CPIT":
        st.subheader("Certificate Program in Information Technology (CPIT)")
        st.write("""
        A joint initiative with IIIT Dharwad and Mindtree Foundation, this 18-month program targets individuals who have exited the formal education system.
        It provides holistic training in basic IT and employability skills, including hands-on projects to bridge the gap between training and employment.
        """)


        st.markdown("""
        <style>
                    .one            {
                    padding:10px 20px; font-size:16px; background-color:grey; color:white; border:none; border-radius:5px;
                    }
                    .one:hover
                    {
                    background-color:#4CAF50;
                    border:2px solid orange;
                    }
                    </style>""",unsafe_allow_html=True)
        home_url = "http://localhost:8501/1app.py"
        st.markdown(f"""
            <a href="{home_url}" target="_self">
                    <button class="one">Go to Home Page</button>
                    </a>
                """, unsafe_allow_html=True)
        
elif selected=="FAQ":

    # Main heading
    st.title("Frequently Asked Questions (FAQ)")

    # Subtitle
    st.markdown("Welcome to our FAQ section. Click on a question to view the answer.")

    # Sample FAQs
    faq_items = [
        {
            "question": "What is Edunet?",
            "answer": "Edunet refers to several organizations and initiatives in the education sector. Here's an overview of the most prominent ones:​"
        },
        {
            "question": "How do I install Edunet?",
            "answer": "The term Edunet encompasses various platforms and services, each with its own installation procedures. To provide accurate guidance, could you please specify which Edune you're referring to? Here are some possibilities:​"
        },
        {
            "question": "Can I use Edunet for production apps?",
            "answer": "Streamlit is great for prototypes, internal tools, and data apps, but whether it's suitable for production apps depends on what kind of production you're aiming for. Here's the breakdown:"
        },
        {
            "question": "How do I deploy a Edunet app?",
            "answer": "The answer depends on which Edunet you're referring to, as Edunet can mean different things depending on the country or organization:"
        },
    ]

    # Display FAQs using expanders
    for item in faq_items:
        with st.expander(item["question"]):
            st.write(item["answer"])

    # Footer
    st.markdown("---")
    st.markdown("Still have questions? [ Visit Official Website](https://edunetfoundation.org/contact/)")


elif selected=="Contact":


    import os
    # st.set_page_config(page_title="Contact Us", layout="centered")
    st.title("📞 Contact Us")
    st.markdown("""
    We'd love to hear from you!  
    Whether you have questions, feedback, or partnership opportunities, feel free to reach out.
    """)

    st.header("📝 Send us a message")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name", placeholder="John Doe")
        email = st.text_input("Your Email", placeholder="john@example.com")
        subject = st.text_input("Subject", placeholder="Feedback, Question, etc.")
        message = st.text_area("Message", placeholder="Type your message here...")
        submit = st.form_submit_button("Send Message")

        if submit:
            submission = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": name,
                "Email": email,
                "Subject": subject,
                "Message": message
            }

            file_path = "messages.csv"

            try:
                # Check if file exists and is not empty
                if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                    df = pd.read_csv(file_path)
                    df = pd.concat([df, pd.DataFrame([submission])], ignore_index=True)
                else:
                    # Create new file with this submission
                    df = pd.DataFrame([submission])

                df.to_csv(file_path, index=False)
                st.success("✅ Your message has been sent! We'll get back to you soon.")
            except Exception as e:
                st.error(f"❌ Error saving your message: {e}")

    # Contact Info
    st.header("📌 Other Ways to Reach Us")
    st.write("""
    - 📧 Email: contact@yourdomain.com  
    - 📱 Phone: +1 234 567 890  
    - 🌐 Website: [www.yourdomain.com](https://yourdomain.com)  
    - 📍 Address: 123 Main Street, YourCity, Country  
    """)

    # Optional: Embed a map
    st.map(pd.DataFrame({
        'lat': [28.984644],
        'lon': [77.705956]
    }, columns=['lat', 'lon']))

    st.markdown("""
    <style>
                .one            {
                padding:10px 20px; font-size:16px; background-color:grey; color:white; border:none; border-radius:5px;
                }
                .one:hover
                {
                background-color:#4CAF50;
                border:2px solid orange;
                }
                </style>""",unsafe_allow_html=True)
    # home_url = "http://localhost:8501/1app.py"
    st.markdown("""
        <a href="https://edunetfoundation.org/contact/" target="_self">
                <button class="one">Official website</button>
                </a>
            """, unsafe_allow_html=True)
    
elif selected=="Login":


      

    st.markdown("""
    <style>
        .stButton{
            width:50%;
            display:flex;
        }</style>""",unsafe_allow_html=True)

    st.markdown(
        """
    <h1 style='text-align:center; color:red;'>
            🎓 Edunet Foundation
        </h1>
        """, unsafe_allow_html=True
    )
    st.title("🔐 Go to Login Page !" )
    st.write("Welcome! Please log in to continue")
    # login = login_authentication()
    # Login Function

    login_url = "https://emp-system1.streamlit.app/"
    st.markdown(f"""
        <a href="{login_url}" target="_self">
                <button class="one">Go to Login page</button>
                </a>
            """, unsafe_allow_html=True)
        


elif selected=="Forgot password":
    import mysql.connector
    st.markdown("## Forget Password")
    mob_n=st.text_input("Enter Mobile Number",placeholder="Mobile Number")
    username=st.text_input("Enter Username",placeholder="Username")
    done = st.button("Submit")
    go =True if username and mob_n else False
    if done and go:
        try:
            mydb = mysql.connector.connect(
                username='sql12773535',
                password='T5keKr2YFk',
                host='sql12.freesqldatabase.com',
                database='sql12773535'
            )
            cur = mydb.cursor()
        except mysql.connector.Error as err:
            st.error(f"❌ Database connection failed: {err}")
            st.stop()
        query = f"SELECT * FROM user_password WHERE username='{username}'"
        cur.execute(query)
        data=cur.fetchall()
        if len(data)==0:
            st.error("❌Username or mobile number is wrong !❌")
            cur.close()
            mydb.close()
            
        elif str(data[0][8])==(mob_n):
            name,password = data[0][1],data[0][6]
            st.success(f"✅Dear '{name}', your password is '{password}'. ✅")
            cur.close()
            mydb.close()
        else:
            st.error("❌Username or mobile number is wrong !❌")
            cur.close()
            mydb.close()
    elif done:
        st.error("Fill out of all fields !⚠️")
elif selected=="Create account":

    st.title("Create Account")
    import random
    import mysql.connector



    r = random.randint(10000,99999)

    with st.form(key="create_account_form",clear_on_submit=True):
        full_name = st.text_input("Full Name")
        # employee_id = st.text_input("Enter Employee ID")
        gender = st.radio("Select your gender", options=["Male", "Female", "Other"])
        departments_list = ["HR", "Engineering", "Sales", "Marketing", "Finance", "IT"]
        department = st.selectbox("Select your department", options=departments_list)
        mob_no=st.text_input("Mobile No")
        email = st.text_input("Email")
        age = st.number_input("Enter your age", min_value=0, step=1)
        salary=st.text_input("Salary")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if not full_name or not email or not password or not confirm_password:
                st.error("Please fill out all fields.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            else:
                try:
                    # mydb = mysql.connector.connect(
                    #     username='root',
                    #     password='Vikash@123',
                    #     host='localhost',
                    #     database='project'
                    # )

                    mydb = mysql.connector.connect(
                        username='sql12773535',
                        password='T5keKr2YFk',
                        host='sql12.freesqldatabase.com',
                        database='sql12773535'
                    )


                    # st.write("✅ Database Connected. Connection ID:", mydb.connection_id)
                    cur = mydb.cursor()
                except mysql.connector.Error as err:
                    st.error(f"❌ Database connection failed: {err}")
                user=full_name.split(' ')[0]+'_'+str(r)
                message =[f"Dear {full_name}, Your Account created Successfully ✅ !",f"Your Employee ID {r}",f"Username: {user}","Please note these informations for furture use📝 "]
                for e in message:
                    st.success(e)
                # st.success(message)
                query = "INSERT INTO user_password (empid,name,age,gender,department,username,password,email,mobile,salary) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                r=int(r)
                data = (r, full_name, int(age), gender, department, user, password, email, mob_no, salary)
                cur.execute(query,data)
                mydb.commit()
                cur.close()
                mydb.close()
elif selected=="Developed by":
    st.title("💻 Meet Minds Behind the Code")
    st.markdown("""
    <style>
                .border
                {
                # background-color:red;
                color:rgba(0, 0, 255, 0.578);
                padding: 20px; border-radius: 10px; background-color: #f8f9fa; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                border-radius:10px;}
                .border:hover
                {
                border:1px solid black;
                
                box-shadow: 4px 4px 25px purple;
                # background-color:rgba(255, 166, 0, 0.573);
                background-color:rgba(255, 192, 203, 0.432);


                transition: box-shadow 0.3s ease;
                    }
                </style>""",unsafe_allow_html=True)
    developers = [
        {
            "name": "Vikash Kumar Mehta",
            "bio": "I'm a passionate and sincere programmer who truly enjoys creating meaningful and useful projects. Coding is not just a task for me—it's something I genuinely love. I enjoy solving problems, learning new technologies, and turning ideas into working applications.In every project I work on, I focus on clean and efficient code, good structure, and user-friendly design. I always give my full effort and attention to detail, whether it's a small feature or the overall functionality.This project reflects my dedication, curiosity, and growing skills in programming. I’m always looking forward to learning more and becoming better with each new challenge.",
            "handle": "@linkedin",
            "link": "https://github.com/Mehta-g1 ",
        },
        {
        "name": "Singh Rishav Amboj",
            "bio": " I’m a passionate and detail-oriented web developer with a strong foundation in frontend technologies . I enjoy building intuitive, responsive user interfaces and ensuring seamless user experiences across devices. I’m always eager to learn and explore new tools, frameworks, and trends in the tech world. With hands-on project experience and certifications from NASSCOM and IMUN, I aim to blend creativity with functionality in every project I take on. I thrive in collaborative environments, love solving real-world problems through code, and continuously seek opportunities to grow both personally and professionally."

    ,
            "handle": "@linkedin",
            "link": "https://github.com/Singhrishav85",  
        },
        {
            "name": "Ravish Kumar Singh",
            "bio": "My name is Ravish Kumar, and I am currently pursuing a Bachelor of Computer Applications (BCA) with a focus on Software Engineering. I have a keen interest in coding, technology, and developing innovative software solutions. I enjoy learning new programming languages and working on practical projects to enhance my skills. My aim is to become a successful software engineer and contribute to the tech industry by creating impactful and efficient applications that solve real-world problems.",
            "handle": "@linkedin",
            "link": "https://www.linkedin.com/in/ravish-kumar-singh-9abba9296?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app", 
        },
        {
            "name": "Ujjwal Satyaprakash",
            "bio": "My name is Ujjwal Satyaprakash, and I am currently pursuing a Bachelor of Computer Applications (BCA) with a focus on Software Engineering. I have a keen interest in coding, technology, and developing innovative software solutions. I enjoy learning new programming languages and working on practical projects to enhance my skills. My aim is to become a successful software engineer and contribute to the tech industry by creating impactful and efficient applications that solve real-world problems.",
            "handle": "@linkedin",
            "link": "https://www.linkedin.com/in/ujjwal-satya-prakash-a11523290?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app", 
        }
    ]

    col1, col2 ,col3,col4= st.columns(4)
    with col1:
        dev = developers[0]
        st.markdown(f"""
            <div class="border" >
                <h4 style='margin-bottom: 5px;'>{dev['name']}</h4>
                <p style='font-size: 15px; color:black;'>{dev['bio']}</p>
                <p style='font-size: 13px; color: grey;'>
                    <a href="{dev['link']}" target="_blank" style="text-decoration: none; color: grey;">{dev['handle']}</a>
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        dev = developers[1]
        st.markdown(f"""
            <div class="border">
                <h4 style='margin-bottom: 5px;'>{dev['name']}</h4>
                <p style='font-size: 15px;color:black'>{dev['bio']}</p>
                <p style='font-size: 13px; color: grey;'>
                    <a href="{dev['link']}" target="_blank" style="text-decoration: none; color: grey;">{dev['handle']}</a>
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        dev = developers[2]
        st.markdown(f"""
            <div  class="border">
                <h4 style='margin-bottom: 5px;'>{dev['name']}</h4>
                <p style='font-size: 15px;color:black'>{dev['bio']}</p>
                <p style='font-size: 13px; color: grey;'>
                    <a href="{dev['link']}" target="_blank" style="text-decoration: none; color: grey;">{dev['handle']}</a>
                </p>
            </div>
        """, unsafe_allow_html=True)

    
    with col4:
        dev = developers[3]
        st.markdown(f"""
            <div  class="border">
                <h4 style='margin-bottom: 5px;'>{dev['name']}</h4>
                <p style='font-size: 15px;color:black'>{dev['bio']}</p>
                <p style='font-size: 13px; color: grey;'>
                    <a href="{dev['link']}" target="_blank" style="text-decoration: none; color: grey;">{dev['handle']}</a>
                </p>
            </div>
        """, unsafe_allow_html=True)
