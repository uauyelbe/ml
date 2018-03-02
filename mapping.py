import pandas as pd

def get_data():
    df = pd.read_csv("dataset_matching.csv")
    return df

df = get_data()

df["gender"] = df["gender"].replace({"Female":1, "Male":0})
df["Partner"] = df["Partner"].replace({"Yes":1, "No":0})
df["Dependents"] = df["Dependents"].replace({"Yes":1, "No":0})
df["PhoneService"] = df["PhoneService"].replace({"Yes":1, "No":0})
df["MultipleLines"] = df["MultipleLines"].replace({"Yes":1, "No":0, "No phone service":2})
df["InternetService"] = df["InternetService"].replace({"DSL":1, "No":0, "Fiber optic":2})
df["OnlineSecurity"] = df["OnlineSecurity"].replace({"Yes":1, "No":0, "No internet service":2})
df["OnlineBackup"] = df["OnlineBackup"].replace({"Yes":1, "No":0, "No internet service":2})
df["DeviceProtection"] = df["DeviceProtection"].replace({"Yes":1, "No":0, "No internet service":2})
df["TechSupport"] = df["TechSupport"].replace({"Yes":1, "No":0, "No internet service":2})
df["StreamingTV"] = df["StreamingTV"].replace({"Yes":1, "No":0, "No internet service":2})
df["StreamingMovies"] = df["StreamingMovies"].replace({"Yes":1, "No":0, "No internet service":2})
df["Contract"] = df["Contract"].replace({"One year":1, "Month-to-month":0, "Two year":2})
df["PaperlessBilling"] = df["PaperlessBilling"].replace({"Yes":1, "No":0})
df["PaymentMethod"] = df["PaymentMethod"].replace({"Electronic check":1, "Mailed check":0, "Bank transfer (automatic)":2, "Credit card (automatic)":3})
df.to_csv("matching.csv", index=False)
print(df["gender"])