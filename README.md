<a name="readme-top"></a>
#   __BizCardX Extracting Business Card Data with OCR__

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
The aim of this project is to create a Streamlit application with a visualisation dashboard that provides interactive and visually appealing insights on the Phonepe pulse Github repository.

<!-- PLATFORMS USED -->
### PLATFORMS USED:

* [PYTHON](https://www.python.org/)
* [XAMPP SQL](https://www.apachefriends.org/index.html)
* [STREAMLIT](https://streamlit.io/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
  
<!-- LIBRARY USED -->
### LIBRARY USED:
gitpython, pandas, plotly.express, streamlit, streamlit_option_menu, mysql.connector, sqlalchemy(create_engine), PIL, sklearn.

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

   ## HOME PAGE
  ![Screenshot (103)](https://github.com/Hari24-01/Phonephe_Pulse/assets/128268647/33874859-953a-4842-836b-aefd5efa3435)

   ## ANALYSIS PAGE
  ![Screenshot (104)](https://github.com/Hari24-01/Phonephe_Pulse/assets/128268647/035983d8-fbd2-49bc-b4a7-98205c5d5e28)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

* #### __STEP 5:__ Display data in the Streamlit app:
  The obtained data is shown within the [Streamlit](https://docs.streamlit.io/) application, where it is used to build charts, graphs and Map for user analysis.

<!-- OUTPUT -->
### OUTPUT:
   
   #### LINE PLOT:
   * Used To Analysis State-Wise Transaction From Year 2018 - 2023.
   
  ![Screenshot (105)](https://github.com/Hari24-01/Phonephe_Pulse/assets/128268647/6768a147-a01d-47fa-90d1-e17045539835)

  * Different State Transaction.
    
  ![WhatsApp Image 2024-02-14 at 8 45 44 PM](https://github.com/Hari24-01/Phonephe_Pulse/assets/128268647/802a4f48-28c0-44f6-9cd7-547614110743)
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

  #### BAR PLOT:
  * Top 10 State-Wise Transaction.
  
  ![newplot (7)](https://github.com/Hari24-01/Phonephe_Pulse/assets/128268647/6a86d487-0746-4ed0-90b6-534f7379aa49)

  #### PIE PLOT:
  * Number of User Percent of Top 10 State.
  
  ![newplot (5)](https://github.com/Hari24-01/Phonephe_Pulse/assets/128268647/857aa86b-d522-4eba-bb51-388ec8dd1fd0)

  #### MAP PLOT:
  * Transaction Percentage of Each State and Districts from Year 2018 - 2023.
  ![newplot (6)](https://github.com/Hari24-01/Phonephe_Pulse/assets/128268647/df2fa475-3ede-46ca-948b-ad573eed7452)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


