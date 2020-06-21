# Analysis-GoogleApp
Analysis of Google Play Store Dataset (2010-2018)

Overview

The Play Store apps data has enormous potential to drive app-making businesses to success. Actionable insights can be drawn for developers to work on and capture the Android market. The dataset is chosen from Kaggle. It is the web scraped data of 10k Play Store apps for analyzing the Android market. 

This project consist of three phases

1. Google App's Dataset:

    1.1 Dataset overview:
    
         Google App is a computerized system that was created by Google Inc. for the Android framework. It serves the users to peruse and download apps, offering films, books, music, and TV programs. The Google app's dataset involves analyzing the rousing variable for individuals to download the application. Based on the app category, the attributes namely rating, reviews, and the price will be used to visualize the data. From this analysis, we will come to know why and how applications succeed.
         
    1.2 Dataset details:
    
         The dataset contain 10841 rows and 13 variables namely, App, Category, Rating,	Reviews, Size, Installs, Type, Price, Content 
          Rating, Genres, Last Updated, Current Ver, and Android Ver. The dataset is known to have outliers and missing values.
             
2. Pre-Processing: 

    2.1 Identifying missing values:
    
         With the help of plots and summary statistics, outlier and missing values is identified in the data. Specifically, the following columns have missing value such as Rating, Type, Current and Android Version. 
         
    2.2 Removing Outlier:
    
        To produce the quality result, there is a need to clean the data.The outlier is removed from original data using inplace
        function. 
        
    2.3 Handlying missing values:
      
        Imputing function is used to replace missing values from dataset using Aggregate Function (mean, median or mode). Applying
        impute_median function on rating attribute and fillna() function to replace missing values with the mode value for Type,
        Current and Android version column. 
        
    2.4 Converting attribute type:
    
        The type of Price, Review and Install attribute are converted from categorical to numerical data to perform data analysis.
    
3. Exploratory Data Analysis:

        Grouping the interesting attributes based on the category. The values of columns is first extracted and then taken the mean
        (aggregated) which is later on stored on a new variable. 

    3.1 Category vs Rating:
    
        The graph shows that Event, Education, Art and Design category are under top three rating from users. 
        
    3.2 Category vs Reviews:
    
        The individuals have given mostly reviews on Communication, Social and Games apps but have low rating.
        
    3.3 Category vs Price:
    
        Speciafically, the common people have played or downloaded the Finance, Lifestyle and Medical apps. Moreover, their reviews and
        rating are moderate. 
