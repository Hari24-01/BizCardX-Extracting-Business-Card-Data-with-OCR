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

<p align="right">(<a href="#readme-top">back to top</a>)</p>
  
<!-- LIBRARY USED -->
### LIBRARY USED:
easyocr, pandas, streamlit, streamlit_option_menu, mysql.connector, Pillow, re, cv2, numpy.

<!-- PROCEDURE -->
### PROCEDURE:
* #### __STEP 1:__ Connecting To Github Repository For Data Extraction:
   Cloning the Phonepe Pulse Github repository with [gitpython](https://github.com/gitpython-developers/GitPython), then retrieving the data and saving it in the proper format (JSON or CSV).
* #### __STEP 2:__ Data Cleaning:
  Using [Python](https://www.python.org/) and [Pandas](https://pandas.pydata.org/docs/getting_started/index.html) are used for data manipulation and pre-processing, 
  which includes data cleansing, addressing missing values, and transforming data 
  formats for analysis and visualisation.
* #### __STEP 3:__ Data Insertion in MYSQL Server:
  The [mysql-connector-python](https://github.com/mysql/mysql-connector-python) Python package is used to connect to a [MySQL](https://www.apachefriends.org/index.html) database and insert converted data in JSON or CSV format using SQL commands.
* #### __STEP 4:__ Setting up a Streamlit app:
  Utilising [Python](https://www.python.org/) libraries Using [Streamlit](https://docs.streamlit.io/) and [Plotly](https://plotly.com/python/), an interactive dashboard is developed with [geo-map](https://plotly.com/python/maps/) functionalities and a user-friendly 
  interface with many drop-down options.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

* #### __STEP 5:__ Display data in the Streamlit app:
  The obtained data is shown within the [Streamlit](https://docs.streamlit.io/) application, where it is used to build charts, graphs and Map for user analysis.

<!-- OUTPUT -->
### OUTPUT:
   ![Screenshot (143)](https://github.com/user-attachments/assets/72b44683-ebf0-42c2-b26d-20bac6050091)

  ![Screenshot (144)](https://github.com/user-attachments/assets/485e5638-f01f-4a4f-9232-2cea8488decb)

   
<p align="right">(<a href="#readme-top">back to top</a>)</p>


