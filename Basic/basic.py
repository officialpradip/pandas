import pandas as pd

# creating dataframe

df = pd.DataFrame(
    {
        'name': ["Pradip Thapa", "Hari Bahadur", "Shyam Bahadur"],
        'age': [24, 30, 35],
        "address": ["Kathmandu", "Kathmandu", "Kathmandu"]
    }
)
print(df)
