# Exoplanet Detector

A web app that utilizes machine learning in order to detect exoplanet presence based on **Kepler Objects of Interest Data (KOI)** using several characteristics including **orbital period**, **equilibrium temperature**, **planetary radius**, and more. 

## Overview

Through KOI Data, this web app uses a **DecisionTreeClassifier** in order to predict whether or not a stellar object is indeed an exoplanet or a false positive. It uses several libraries such as ``scikit-learn``, ``pandas``, and ``matplotlib`` in order to clean, evaluate, and utilize data in order to create a well trained model. 

## Why was it Created?

In exoplanet detection, false positives can lead to misunderstandings and conclusions that may later affect future research. Due to this, there could be a waste of time and resources while trying to confirm false positives through extra observations. Machine learning can allow for the confirmation of false positives and also mitgating the effects by reducing usage of time and resources, making it a more efficient way of confirming false positives. 

## Features

-  Model trained on cleaned and preprocessed data, allowing maximum efficiency
-  Usage of ``joblib`` in order to save and load trained model
-  Evaluated using **classification_report**, **accuracy_score**, **confusion_matrix**, and **roc_curve**
-  Uses a user-friendly user interface using ``HTML`` and ``CSS``

## Steps to Install

### #1 Clone the Repository

````{bash}
git clone https://github.com/CookieCodesAI/Exoplant-Detection
cd Exoplanet-Detection
````

### #2 Create a virtual environment

````{bash}
python3 -m venv venv
source venv/bin/activate #For Windows use venv\Scripts\activate
````

### #3 Install the dependancies

````{bash}
pip install -r requirements.txt
````

### #4 Run the Web App

````{bash}
python app.py
````

## Dataset

This project uses data from the **NASA Exoplanet Archive - Kepler Objects of Interest (KOI)**
> Source: NASA Exoplanet Archive - Kepler Objects of Interest:
>
> https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=cumulative
