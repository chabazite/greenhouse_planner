# greenhouse_planner
==============================

## Business Case
<a name="Business_Case"></a>
This is a knowledge-based personal project for me. I tasked myself with creating a project that relied heavily on classes, methods, and unit tests. At the same time, I am always looking to work on projects I find relevent. In my own life, I love planning out my garden. However, I find that excel sheets can lead to something not as informative as I hoped for. Additionally, it takes a while to make one each time I want to plan a  new garden. 

With classes and methods, I wanted to build out something that could save a Garden for me and its particular attributes such as sunlight and soil fertility. I wanted to be able to store different plants in each garden, with their own attributes about the plant. With that I had the following goals:

1. Create a Garden & Plant Class
2. Have the garden respond to plant additions to optimize garden placement (sunlight, bed space, etc.)
3. Create Methods that allow adding bed space and plants to the garden
4. Create unit tests for the classes and methods
4. Turn this into a web app to share. 


## Table of Contents
<details open>
  <summary>Show/Hide</summary>
  <br>
 
1. [ File Descriptions ](#File_Description)
2. [ Technologies Used ](#Technologies_Used)    
3. [ Evaluation ](#Evaluation)
4. [ Future Improvements ](#Future_Improvements)

</details>


## Project Organization

<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
 <br>


    ├── LICENSE
    ├── .gitignore
    ├── README.md          <- The top-level README for developers using this project.
    ├──
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── venv                <- Virtual Environment for the project
    │
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── tests              <- The location for unit tests
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        │
        └── modules  <- Scripts to for the classes and methods
        │   ├── Garden.py       <- Garden class and methods
        │   ├── Plants.py       <- plants class and methods
        │   └── __init__.py     <- Makes modules a Python module

--------
  </details>   

## Technologies Used:
<details>
<a name="Technologies_Used"></a>
<summary>Show/Hide</summary>
<br>


    ├── Python
        ├── datetime
        ├── unittest 
        ├── Pypi       
        └── AWS    
 ------------
 </details>


## Evaluation:
<a name="Evaluation"></a>
<details>
<summary>Show/Hide</summary>
<br>

The package works as intended. It is simple and allows for the creation of garden objects and plant objects. The plants can be stored in a list within each garden. The garden responds to the addition of any plant with checks ensuring it has the proper sunlight and space to house the plant. Additionally, it will provide the total cost of planting the garden as well as update your remaining sqft left for planting. 

</details>
  
## Future Improvements
 <a name="Future_Improvements"></a>
 <details>
<summary>Show/Hide</summary>
<br>

I will be turning this package into a webapp to provide a GUI. 

</details>

<p>README outline tailored from [awesomeahi95][]<p>
