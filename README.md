<a name="readme-top"></a>
#   __BizCardX: Business Card Information Extractor__

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#problem-statement">PROBLEM STATEMENT</a>
    </li>
    <li>
      <a href="#platforms-used">PLATFORMS USED</a>
    </li>
    <li><a href="#library-used">LIBRARY USED</a></li>
    <li><a href="#procedure">PROCEDURE</a></li>
    <li><a href="#output">OUTPUT</a></li>
  </ol>
</details>

<!-- PROBLEM STATEMENT -->
### PROBLEM STATEMENT:
The aim of the project is to develop a Streamlit application that permits users to input business card photos, extract essential information with easyOCR, and display it in an interactive user interface.

<!-- PLATFORMS USED -->
### PLATFORMS USED:

* [PYTHON](https://www.python.org/)
* [XAMPP SQL](https://www.apachefriends.org/index.html)
* [STREAMLIT](https://streamlit.io/)
  
<!-- LIBRARY USED -->
### LIBRARY USED:
easyocr, pandas, streamlit, streamlit_option_menu, mysql.connector, Pillow, re, cv2, numpy.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- PROCEDURE -->
### PROCEDURE:

* #### __STEP 2:__ Install the required Python packages:
     pip install streamlit easyocr mysql-connector-python pandas opencv-python 
     pillow 
     streamlit-option-menu
  
* #### __STEP 3:__ Set up the MySQL database:
*   Create a database named bizcardx_data.
*   Run the SQL commands in the app to create the required table structure.

* #### __STEP 6:__ Navigate the Application:
*   Upload Card: Upload a business card image. The application extracts and 
    displays the data for review and correction. Save the data to the database by clicking "Upload to SQL."
*   View Cards: View a table of saved business cards.
*   Update Card: Select an entry to update and modify the fields as needed. Click "Update Card" to save changes.
*   Delete Card: Select an entry to delete and confirm the action.

* #### __STEP 8:__ Database Management:
*   Each business card's data is stored in a MySQL table.
*   The app supports CRUD (Create, Read, Update, Delete) operations.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- OUTPUT -->
### OUTPUT:
   ![Screenshot (143)](https://github.com/user-attachments/assets/72b44683-ebf0-42c2-b26d-20bac6050091)

  ![Screenshot (144)](https://github.com/user-attachments/assets/485e5638-f01f-4a4f-9232-2cea8488decb)

   
<p align="right">(<a href="#readme-top">back to top</a>)</p>


