"""Mongo Demo using pymongo"""
from pymongo import MongoClient

client = MongoClient("mongodb+srv://dalei:oarnud9I@analytics.fegzyn1.mongodb.net/?" +
                     "retryWrites=true&w=majority&appName=analytics")

movie_collection = client["sample_mflix"]["movies"]
movie = movie_collection.find_one()

print(movie)
