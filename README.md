# Mental-Health-Prediction
> Mental health prediction model made with sci-kit learn.

# How to run the app?
Setup your virtual environment and run the following command:
```
python app.py
```

# What is the payload to be sent?
```
{
    "features":[[0.54,1,1,2,0,0,4,1]]
}
```

# URL to be hit on
Once the app is up and running the hit this endpoint with above payload: <strong>http://127.0.0.1:5000/predict</strong>

# Data Dictionary 
The following are the features we'll use to predict our target variable (heart disease or no heart disease)
1. Age - age in years,
2. Gender - (1 = male; 0 = female),
3. family_history - (0= No or 1 = yes),
4. benefits - additional Benifits (yes=2, dont know=1, no=0)
5. care_options - (yes=2, no=0 and probable=1)
6. anonymity - 
7. leave - Ease of getting leaves (0 to 4)
8. work_interfere - (yes=1 or no=0)