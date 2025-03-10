# -*- coding: utf-8 -*-
"""Cain HW1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13VmLAGmcW8glOKaGoK5d8HigJLm1phFz
"""

#Carmen Cain
#IS 733
#February 24, 2025
#Dr. Basnyat

import pandas as pd

df = pd.read_csv("Pavement_Condition_Index.csv")
df.head()
df.shape

#there are fifteen columns but many of these columns are symbolic: OBJECTID, Segment_ID, StreetName, CENSUS_ID, DEPOT_NUMB, DEPOT_NAME, MOCO_MAINT, FromStreet, ToStreet, and Surface Type
#interestingly, "DEPOT_NAME" and "DEPOT_NUMB" are duplicative
df['CENSUS_ID'].unique()
df['CENSUS_ID'].nunique()
df['CENSUS_ID'].value_counts()

df["DEPOT_NAME"].unique()
df["DEPOT_NAME"].nunique()
df[["DEPOT_NUMB", "DEPOT_NAME"]].value_counts()

df['MOCO_MAINT'].unique()
df["MOCO_MAINT"].nunique()
df["MOCO_MAINT"].value_counts()

df['FromStreet'].unique()
df['FromStreet'].nunique()
df['FromStreet'].value_counts()

df['ToStreet'].unique()
df['ToStreet'].nunique()
df['ToStreet'].value_counts()

df['SurfaceTyp'].unique()
df['SurfaceTyp'].nunique()
df['SurfaceTyp'].value_counts()

#Each of the counts above has a top three, except for whether the road is maintained by
#the county or not
#is there a way to specifically show the top three values for all of these? Or am I
#supposed to say so in real sentences.

#the dimensional columns
df[["Shape_Leng", "Length_1", "Width"]].apply(
    {"Shape_Leng":["mean", "median", "min", "max", "std"],
      "Length_1":["mean", "median", "min", "max", "std"],
     "Width":["mean", "median", "min", "max", "std"]
}
    )

#PCI is a measurement of pavement quality on a scale of 0-100, where 1 is a failure and 100 is perfect
df['PCI'].apply(["mean", "median", "min", "max", "std"])

#overall Montgomery County roads are fine.

#There's a road that is recorded as 0 feet long and 0 feet wide, which I think must be missing data.

df.groupby("SurfaceTyp").agg (
    avg_length = ("Length_1", "mean"),
    median_length = ("Length_1", "median"),
    avg_width = ("Width", "mean"),
    median_width = ("Width", "median"),
    number_of_roads = ("Length_1", "count")
)

#there isn't a legend of what these surface types are, so this chart is less interesting
#than it could be

df.groupby("DEPOT_NAME")["Length_1"].median()

#Poolesville's roads are on average longer than the other depots in Montgomey County

df.groupby("DEPOT_NAME").agg(
    avg_length = ("Length_1", "mean"),
    median_length = ("Length_1", "median"),
    total_length = ("Length_1", "sum"),
    median_quality = ("PCI", "median")
)

#It looks like the Colesville depot is responsible for the most roads, but Poolesville
#has the longest roads on average (as we know) followed distantly by Damascus
#Damascus has the highest median quality and Poolesville the lowest. We can only
#assume no one in Bethesda has looked at this dataset or they would be furious

#a histogram for this data shows that most roads in Montgomery County are relatively short
import matplotlib.pyplot as plt
plt.figure(figsize=(4,6))
plt.hist(df['Length_1'], bins=4)
plt.title('Length of Montgomery County Roads')
plt.xlabel('Length')
plt.ylabel('Number of Roads')


plt.figure(figsize=(4,6))
plt.hist(df['Width'], bins=4)
plt.title('Width of Montgomery County Roads')
plt.xlabel('Width')
plt.ylabel('Number of Roads')

#there's more variation in the width of Montgomery County roads, though overall they are relatively narrow

#it seems like there should be a more direct way to generate a bar graph but this is what I was able to find
import numpy as np
SurfaceTyp = ['AC', 'GR','BRG', 'PLN', 'X', 'UND', 'PCC', 'NOA', 'JUR', 'GTE', 'BR', 'BLK']
roads = [24952, 44, 44, 35, 29,27, 16, 15, 3, 3, 2, 1]

plt.bar(SurfaceTyp, roads)
plt.title("Surface Type")
plt.xlabel("Surface Type")
plt.ylabel("Number of Roads")
plt.show()

#There's a surprising amount of variety in Montgomery County's roads, including some relatively rare pavement types

DEPOT_NAME = ['Bethesda','Colesville', 'Damascus', 'Gaith East', 'Gaith West', 'Pooles', 'Silver Spring']
median_length = [368.35, 374.85, 467.03, 382.70, 396.55, 932.20, 328.7]
plt.bar(DEPOT_NAME, median_length)
plt.title("Median Length of Roads by Depot")
plt.xlabel("Depot")
plt.ylabel("Median Length")
plt.show()

DEPOT_NAME = ['Bethesda','Colesville', 'Damascus', 'Gaith East', 'Gaith West', 'Pooles', 'Silver Spring']
median_quality = [67.97, 68.69, 70.99, 69.84, 69.61, 64.00, 68.93]
plt.bar(DEPOT_NAME, median_quality)
plt.title("Median Quality of Roads by Depot")
plt.xlabel("Depot")
plt.ylabel("Median Quality")
plt.show()


MOCO_maintenance = ['yes', 'no']
roads = (25171, 1)
plt.bar(MOCO_maintenance, roads)
plt.title("County-Maintained Roads")
plt.xlabel("MOCO Maintenance")
plt.ylabel("Number of Roads")
plt.show()

#And yet the county overwhelmingly does the maintenance