# Weather classification and prediction
2024-2025 F20DL Assessed Coursework, Heriot-Watt University Dubai

### Group 7's members: 
  > Areej Ahmed: H00385913
> 
  > Muhammad Imaad: H00362645
> 
  > Ziyaan Mir: H00382769
> 
  > Syed Ammar: H00364774
> 
  > Mufaddal Abizar Ezzi: H00360993

Coursework Overview
The group project at hand involves choosing one topic of application and then selecting and analyzing 1–3
unique datasets while dividing the project into five distinct phases. The project's overarching goal is to
explore, analyze, and apply machine learning techniques to these datasets. The project emphasizes team
work, data exploration, and the application of various machine learning methods, including clustering,
decision trees, and neural networks

### Our Project Milestones:

  Week 3: Finalize topic, finalize datasets and lay out the objectives.
  
  Week 4: Carry out data visualization on datasets. Finish PowerPoint for D1. (R1)
  
  Week 5: Change PowerPoint slides as per feedback. Start preprocessing.
  
  Week 6: Complete preprocessing. Visualize data after preprocessing and analyze. (R2)
  
  Week 7: Experiment with clustering (R3)
  
  Week 8: Start training models. Evaluate their performance. (R4)
  
  Week 9:Experiment with Neural Networks (R5)
  
  Week 10: Work on the report
  
  Week 11: Finalize report


### Our datasets are: 
#### 1. Australian Weather Data
> Link for the dataset: https://www.kaggle.com/datasets/arunavakrchakraborty/australia-weather-data

> Original source of the data: Australian Bureau of Meteorology at http://www.bom.gov.au/climate/data/

> License: CC0: Public Domain

> Examples of dataset content:
![image](https://github.com/user-attachments/assets/4e9bb6f9-a5ff-4836-b76b-9535da8cb023)

#### 2. London Weather Data
> Link for the dataset: https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data

> Original source of the data: European Climate Assessment (ECA) at http://www.bom.gov.au/climate/data/](https://www.ecad.eu/dailydata/index.php)

> License: CC0: Public Domain

> Examples of dataset content:
![image](https://github.com/user-attachments/assets/1a9ad034-44ec-4b34-867c-a8a6ebfc0638)

#### 3. Weather Image Recognition
> Link for the dataset: https://www.kaggle.com/datasets/jehanbhathena/weather-dataset

> Original source of the data: Harvard Dataverse

> License: CC0: Public Domain

> Some images of this dataset include:
>
> # Dew: ![image](https://github.com/user-attachments/assets/248e3821-6a8f-4af8-a77b-ea1979f59b04)
>
> # Rain: ![image](https://github.com/user-attachments/assets/a37014bd-a993-49ae-80a6-3752e5c69591)



   

### Data Pipeline:
1. Tools\Software needed: Jupyter Notebook or Google Colab
2. Libraries Required: NumPy, Pandas, matplotlib.pyplot, seaborn, imbalanced-learn, scikit-learn, xgboost, lightgbm, catboost.
3. Load raw dataset from the specified directory in the header of the notebook.
4. Clean the data by removing null values and handling outliers.
5. Normalize numerical features and encode categorical features.
6. Split the data into training and testing sets.
7. Save the preprocessed dataset with a change in name for ease of use.

### Requirements
1. #### Australia Weather Data
> With this dataset, we are classifying based on chosen attributes, whether or not is raining the next day. The attribute we are predicting is the "RainTomorrow" attribute.
* Data Preprocessing and Analysis (R2)
> Process
* Clustering (R3)
> Cluster
* Model Training and Evaluation (R4)
> Model A
> What inputs is the model using to predict from
>
> Figure showing results using permanent links
>
> Model B
> What inputs is the model using to predict from
>
> Figure showing results using permanent links
> 
> Model C
> What inputs is the model using to predict from
>
> Figure showing results using permanent links
> 
*Neural Networks (R5)
> CNN
> 
> MLP
>
> Table of results (Markdown tables)

2. #### London Weather Data
> With this dataset, we are predicting based on chosen attributes, the amount of sunshine the next day. The attribute we are predicting is the "sunshine" attribute.
* Data Preprocessing and Analysis (R2)
> Process
* Model Training and Evaluation (R4)
> Model A
> What inputs is the model using to predict from
>
> Figure showing results using permanent links
>
> Model B
> What inputs is the model using to predict from
>
> Figure showing results using permanent links
> 
> Model C
> What inputs is the model using to predict from
>
> Figure showing results using permanent links
> 
*Neural Networks (R5)
> CNN
> 
> MLP
>
> Table of results (Markdown tables)

1. #### Weather Image Recognition
> With this dataset, we are classifying pictures into certain classes using neural networks.
* Data Preprocessing and Analysis (R2)
> Process
* Clustering (R3)
> Cluster
* Model Training and Evaluation (R4)
> Model A
> What inputs is the model using to predict from
>
> Figure showing results using permanent links
>
> Model B
> What inputs is the model using to predict from
>
> Figure showing results using permanent links
> 
> Model C
> What inputs is the model using to predict from
>
> Figure showing results using permanent links
> 
*Neural Networks (R5)
> CNN
> 
> MLP
>
> Table of results (Markdown tables)

### Folder and File Structure
* #### data/
> This folder stores our chosen datasets as well their the preprocessed versions.
* #### notebooks/
> This folder stores our notebooks for our analysis and model running.
* #### scripts/
> This folder stores our scripts for preprocessing our datasets.
* #### documentation/
> This folder stores our project documents as well as the weekly updates of our work
