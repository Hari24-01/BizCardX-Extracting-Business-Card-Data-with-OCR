# Import necessary libraries
import streamlit as st
import re
from streamlit_option_menu import option_menu
import mysql.connector as sql
import pandas as pd
from PIL import Image
import easyocr
import cv2
import numpy as np

# SETTING PAGE CONFIGURATIONS
icon = Image.open(r"H:\codes\image\briefcase.png")

st.set_page_config(page_title= "BizCardX: Business Card Data Extractor",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "auto",
                   menu_items={'About': """#This application is designed to extract data from business cards."""}
                   )

# APPLYING BACKGROUND
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.pinimg.com/736x/62/32/8c/62328c7d3a578c3d2289547a10bfe57a.jpg");
background-size: cover;
background-position: left-conner;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("https://i.pinimg.com/236x/6e/93/79/6e93792081de1444edcaf82a8d64aba6.jpg");
background-size: cover;
background-repeat: no-repeat;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

        
# Sidebar menu
with st.sidebar:
    menu= option_menu("MENU", ["Upload Card","View Cards","Update Card","Delete Card"], 
                           icons=["upload","person-vcard","pencil-square","trash3-fill"],
                           default_index=0,
                           orientation="vertical",
                           styles={"nav-link": {"font-size": "20px", "text-align": "centre", "margin": "10px", 
                                                "--hover-color": "#262730"},
                                   "icon": {"font-size": "20px"},
                                   "container" : {"max-width": "8000px"},
                                   "nav-link-selected": {"background-color": "#2F8E8A"}})

try:
    # CONNECTING WITH MYSQL DATABASE
    mydb = sql.connect(host="localhost",
                    user="root",
                    password="",
                    database= "bizcardx_data" #SELECT DATABASE FROM SQL SERVER
                    )
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute('''
                    CREATE TABLE IF NOT EXISTS bizcardx(
                        'Id' INTEGER(11) PRIMARY KEY AUTOINCREMENT,
                        'Company_name' VARCHAR(225),
                        'Card_holder' VARCHAR(225),
                        'Designation' VARCHAR(225),
                        'Mobile_number' CHAR(50),
                        'Email' TEXT,
                        'Website' TEXT,
                        'Area' VARCHAR(225),
                        'City' VARCHAR(225),
                        'State' VARCHAR(225),
                        'Pin_code' CHAR(10)
                    )
                ''')
    mydb.commit()

    
except:
    pass
    #st.warning("### ⚠️ Connect to SQL !!")

extracted_info = {
                'company_name': '',
                'card_holder': '',
                'designation': '',
                'mobile_number': [],
                'email': [],
                'website': [],
                'area': [],
                'city': [],
                'state': [],
                'pin_code': []
            }

st.title("💼 BizCardX: Business Card Data Extractor")

if menu == "Upload Card":
    st.subheader("• Upload Business Card⬆️")
    

     # Upload image
    uploaded_image = st.file_uploader("Choose an image", type=['jpg', 'png', 'jpeg'])


    # Note
    st.markdown('''Supported File Extension: **PNG, JPG, JPEG**; 
                File size limit: **2 MB**; 
                Image dimension limit: **1500 pixels**.''')


    if uploaded_image is not None:
        # Convert uploaded image to OpenCV image
        file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        image_text=reader.readtext(image)

        def draw_bounding_boxes(image, detections, threshold=0.25):
            for bbox, text, score in detections:
                if score > threshold:
                    cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (5, 255, 0), 2)

        threshold = 0.02
        image_1=image.copy()
        draw_bounding_boxes(image_1, image_text, threshold)

        result=[]
        for (bbox, text, prob) in image_text:
            result.append(text)
        
    
        st.image(cv2.cvtColor(image_1, cv2.COLOR_BGR2RGBA), caption="Uploaded Image")

        # Divide image into right and left halves
        height, width, _ = image.shape
        left_half = image[:, :width//2, :]
        right_half = image[:, width//2:, :]


        # Extract text from left and right halves
        left_half_text = reader.readtext(left_half)
        right_half_text = reader.readtext(right_half)

        l1=[]
        for (bbox, text, prob) in left_half_text:
            l1.append(text)
        
        l2=[]
        for (bbox, text, prob) in right_half_text:
            l2.append(text)

        if len(l1)>len(l2):
            if len(l2) > 2:
                for i in range(0,len(l2)-1):
                    if len(l2[i]) <= 3:
                        l2.remove(i)
            extracted_info["company_name"]=l2
        else:
            if len(l1) > 2:
                for i in range(0,len(l1)-1):
                    if len(l1[i]) <= 3:
                        l1.pop(i)
            extracted_info["company_name"]=l1   

        city = ""  # Initialize the city variable
        for ind, i in enumerate(result):
            # To get website_URL
            if "www " in i.lower() or "www." in i.lower():
                extracted_info["website"].append(i)
            elif "WWW" in i:
                extracted_info["website"].append(result[ind] + "." + result[ind+1])

            # To get email ID
            elif "@" in i:
                extracted_info["email"].append(i)

            # To get MOBILE NUMBER
            elif "-" in i:
                extracted_info["mobile_number"].append(i)
                if len(extracted_info["mobile_number"]) == 2:
                    extracted_info["mobile_number"] = " & ".join(extracted_info["mobile_number"])
            
            # To get CARD HOLDER NAME
            elif ind == 0:
                extracted_info["card_holder"]=i

            # To get designation
            elif ind == 1:
                extracted_info["designation"]=i

            # To get area
            if re.findall("^[0-9].+, [a-zA-Z]+", i) or "St" in i:
                extracted_info["area"].append(i.split(",")[0])
            elif re.findall("[0-9] [a-zA-Z]+", i):
                extracted_info["area"].append(i)
            

            # To get city NAME
            match1 = re.findall(".+St , ([a-zA-Z]+).+", i)
            match2 = re.findall(".+St,, ([a-zA-Z]+).+", i)
            match3 = re.findall("^[E].*", i)
            if match1:
                city = match1[0]  # Assign the matched city value
            elif match2:
                city = match2[0]  # Assign the matched city value
            elif match3:
                city = match3[0]  # Assign the matched city value

            # To get state
            state_match = re.findall("[a-zA-Z]{9} +[0-9]", i)
            if state_match:
                extracted_info["state"].append(i[:9])
            elif re.findall("^[0-9].+, ([a-zA-Z]+);", i):
                extracted_info["state"].append(i.split()[-1])
            if len(extracted_info["state"]) == 2:
                extracted_info["state"].pop(0)

            # To get PINCODE
            if len(i) >= 6 and i.isdigit():
                extracted_info["pin_code"].append(i)
            elif re.findall("[a-zA-Z]{9} +[0-9]", i):
                extracted_info["pin_code"].append(i[10:])

        
        extracted_info["city"].append(city)

        if "," in extracted_info["city"][0]:
            extracted_info["city"][0] = extracted_info["city"][0].replace(",", "")  

        if ";" in extracted_info["state"][0]:
            extracted_info["state"][0] = extracted_info["state"][0].replace(";", "")        
        

        st.subheader("🔍 Extracted Information")
        edited_info = {}
        cols = st.columns(2)

        for key, value in extracted_info.items():
            if isinstance(value, list):
                extracted_info[key] = ''.join(extracted_info[key])
        
        with cols[0]:
            edited_info['company_name'] = st.text_input("Company Name", extracted_info['company_name'])
            edited_info['card_holder'] = st.text_input("Card Holder", extracted_info['card_holder'])
            edited_info['designation'] = st.text_input("Designation", extracted_info['designation'])
            edited_info['mobile_number'] = st.text_input("Mobile Number", extracted_info['mobile_number'])
            edited_info['email'] = st.text_input("Email", extracted_info['email'])
                
        with cols[1]:
            edited_info['website'] = st.text_input("Website", extracted_info['website'])
            edited_info['area'] = st.text_input("Area", extracted_info['area'])
            edited_info['city'] = st.text_input("City", extracted_info['city'])
            edited_info['state'] = st.text_input("State", extracted_info['state'])
            edited_info['pin_code'] = st.text_input("Pin Code", extracted_info['pin_code'])


        if st.button("Upload to SQL"):
            try:
                value=()
                for key,data in  extracted_info.items():
                    value+=(data,)
                sql = """INSERT INTO bizcardx (company_name,card_holder,designation,mobile_number,email,
                            website,area,city,state,pin_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                mycursor.execute(sql, value)
                mydb.commit()
                st.success("Transformation to MySQL Successful")

            except:
                st.warning("DATA ALREADY EXISTS!!!")
            
elif menu == "View Cards":
    st.subheader("• View Business Card🪪")
    mycursor.execute("SELECT * FROM bizcardx")
    cards = mycursor.fetchall()
        
    if cards:
        columns = ['ID', 'Company', 'Holder', 'Designation', 'Mobile', 
                       'Email', 'Website', 'Area', 'City', 'State', 'Pin Code']
        df = pd.DataFrame(cards, columns=columns)
        st.dataframe(df)
    else:
        st.info("No business cards saved yet.")
        
elif menu == "Update Card":
    st.subheader("• Update Business Card📝")
    try:
        mycursor.execute("SELECT id, card_holder, company_name FROM bizcardx")
        cards = mycursor.fetchall()
        # Create mapping for display
        card_options = [f"ID {card[0]}: {card[1]} ({card[2]})" for card in cards]
        selected_card = st.selectbox("Select Card to Update", card_options)
        
        # Extract card ID
        card_id = int(selected_card.split(':')[0].split()[1])
        
        # Fetch current card details
        mycursor.execute("SELECT * FROM bizcardx WHERE id = %s", (card_id,))
        current_card = mycursor.fetchone()
        
        # Prepare update form
        cols = st.columns(2)
        updated_info = {}
        
        with cols[0]:
            updated_info['company_name'] = st.text_input("Company Name", current_card[1])
            updated_info['card_holder'] = st.text_input("Card Holder", current_card[2])
            updated_info['designation'] = st.text_input("Designation", current_card[3])
            updated_info['mobile_number'] = st.text_input("Mobile Number", current_card[4])
        
        with cols[1]:
            updated_info['email'] = st.text_input("Email", current_card[5])
            updated_info['website'] = st.text_input("Website", current_card[6])
            updated_info['area'] = st.text_input("Area", current_card[7])
            updated_info['pin_code'] = st.text_input("Pin Code", current_card[10])
        
        #Update button
        if st.button("Update Card"):
            # Remove empty values
            cleaned_info = {k: v for k, v in updated_info.items() if v}
            
            try:
                update_query = "UPDATE bizcardx SET "
                update_params = []
                for key, value in updated_info.items():
                    if value:
                        update_query += f"{key} = %s, "
                        update_params.append(value)
            
                update_query = update_query.rstrip(", ") + " WHERE id = %s"
                update_params.append(card_id)
            
                mycursor.execute(update_query, tuple(update_params))
                mydb.commit()
                st.success("Updated")
            except Exception as e:
                 st.error(f"Error updating card: {e}")
    except:
        st.info("No business cards saved yet.")
       
elif menu == "Delete Card":
    st.subheader("• Delete Business Card🗑️")
        
    # Get list of card IDs
    mycursor.execute("SELECT id, card_holder, company_name FROM bizcardx")
    cards = mycursor.fetchall()
        
    if not cards:
        st.warning("No cards to delete. Please upload a card first.")
        
    # Create mapping for display
    card_options = [f"ID {card[0]}: {card[1]} ({card[2]})" for card in cards]
    selected_card = st.selectbox("Select Card to Delete", card_options)
    try: 
        # Extract card ID
        card_id = int(selected_card.split(':')[0].split()[1])
            
        # Delete button
        if st.button("Confirm Delete"):
            try:
                mycursor.execute("DELETE FROM bizcardx WHERE id = %s", (card_id,))
                mydb.commit()
                st.success("Card deleted successfully!")
            except Exception as e:
                st.error(f"Error deleting card: {e}")
    except:
        pass