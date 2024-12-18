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
* #### __STEP 1:__ Application Setup:
   Create an intuitive UI in Streamlit with widgets such as file uploaders, buttons, and text boxes to guide users through uploading a business card image,Organize and present the         extracted data (company name, cardholder name, etc.) in the Streamlit GUI using tables or text boxes.

* #### __STEP 2:__ Database Connection:
  Create a table bizcardx (if not already present) to store extracted information, Use SQLite or MySQL to store the extracted information and uploaded business card images.
  
* #### __STEP 3:__ View Cards Page:
  Users can view all saved business card data in a tabular format using Pandas DataFrame in Streamlit.
  
* #### __STEP 4:__ Update Card Page:
  Editable fields are displayed, allowing users to make changes to the select a card from the list (identified by ID, holder name, and company name) to update its details.
  
* #### __STEP 5:__ Delete Card Page:
  Upon confirmation, the selected record the Users can delete the card from the database.
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- OUTPUT -->
### OUTPUT:
   ![Screenshot (143)](https://github.com/user-attachments/assets/72b44683-ebf0-42c2-b26d-20bac6050091)

  ![Screenshot (144)](https://github.com/user-attachments/assets/485e5638-f01f-4a4f-9232-2cea8488decb)

   
<p align="right">(<a href="#readme-top">back to top</a>)</p>


