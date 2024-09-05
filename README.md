# Projects Overview

- [Resume Screening using Machine Learning](#resume-screening-using-machine-learning)
- [Sentiment Analysis of COVID-19 Tweets](#sentiment-analysis-of-covid-19-tweets)
- [Sentiment Analysis of Airline Tweets](#sentiment-analysis-of-airline-tweets)

## Resume Screening using Machine Learning

This project implements a resume screening system using machine learning techniques to classify resumes into distinct categories based on their content. The goal is to automate and streamline the resume review process, making it easier to categorize candidates by their skills and experience.

### Introduction

This project leverages natural language processing (NLP) and machine learning algorithms to classify resumes into different job categories. By analyzing the content of resumes, the system can predict the appropriate category such as `Data Science`, `Web Designing`, `HR`, and more.

### Dataset

The dataset used in this project is a CSV file (`resume.csv`) containing resumes with the following fields:

- **Category**: The job category of the resume.
- **Resume**: The full text of the resume.

The dataset is pre-processed to clean the resume text for better classification performance.

### Features

- **Text Preprocessing**: Includes cleaning of resumes by removing URLs, punctuation, stopwords, and special characters.
- **Word Cloud Generation**: A visual representation of the most common words in the resumes.
- **Classification Models**: The project uses the K-Nearest Neighbors (KNN) algorithm with `OneVsRestClassifier` for multi-class classification.
- **Accuracy and Performance Metrics**: The model's performance is evaluated using accuracy and a classification report with precision, recall, and F1-score.

### Model and Evaluation

The model achieves high accuracy on both training and test datasets, reaching around **99% accuracy**. The classification report provides detailed performance metrics for each category, ensuring the model performs well across all categories.

<hr>

## Sentiment Analysis of COVID-19 Tweets

This project performs sentiment analysis on tweets related to the COVID-19 pandemic using Natural Language Processing (NLP) and machine learning techniques. It categorizes tweets into various sentiment classes like `Positive`, `Negative`, `Neutral`, and others.

### Introduction

This project analyzes the sentiment of COVID-19-related tweets to determine the emotional tone conveyed by users. By applying NLP techniques such as text cleaning, feature extraction, and Random Forest classification, we classify tweets into different sentiment categories.

### Dataset

The dataset used is a CSV file containing tweets about COVID-19 with the following fields:

- **UserName**: The name of the user who tweeted.
- **ScreenName**: The Twitter handle of the user.
- **Location**: The user's location.
- **TweetAt**: The date of the tweet.
- **OriginalTweet**: The full text of the tweet.
- **Sentiment**: The sentiment label for the tweet (`Positive`, `Negative`, `Neutral`, `Extremely Positive`, `Extremely Negative`).

### Features

- **Data Cleaning**: Removes special characters, single characters, and extra spaces from the tweet text.
- **Sentiment Classification**: Uses the Random Forest Classifier to predict the sentiment of the tweets.
- **Confusion Matrix Visualization**: Generates a confusion matrix to evaluate model performance visually.

### Model and Evaluation

The Random Forest classifier was trained on 80% of the data and tested on the remaining 20%. The accuracy of the model is approximately **51.4%**, and further improvements could be made by tuning hyperparameters or using other classification algorithms.

<hr>

## Sentiment Analysis of Airline Tweets

This project performs sentiment analysis on tweets related to various airlines using Natural Language Processing (NLP) techniques and machine learning models. The tweets are classified into different sentiment categories such as `Positive`, `Negative`, and `Neutral`.

### Introduction

This project aims to analyze the sentiment of airline-related tweets by classifying them into distinct sentiment categories. It leverages text processing, feature extraction, and machine learning techniques to predict the sentiment of the tweets.

### Dataset

The dataset used is a CSV file containing airline-related tweets with the following fields:

- **tweet_id**: Unique ID of the tweet.
- **airline_sentiment**: Sentiment of the tweet (`positive`, `negative`, `neutral`).
- **airline_sentiment_confidence**: Confidence score of the sentiment prediction.
- **airline**: Name of the airline.
- **text**: The content of the tweet.
- Additional fields such as location, retweet count, and creation time.

### Features

- **Data Cleaning**: Removes special characters, single characters, and extra spaces from the tweet text.
- **Sentiment Classification**: Uses the Random Forest Classifier to predict the sentiment of the tweets.
- **Confusion Matrix Visualization**: Generates a confusion matrix to evaluate model performance visually.

### Model and Evaluation

The Random Forest classifier was trained on 80% of the dataset and tested on the remaining 20%. The accuracy of the model is approximately **25.4%**, with the classification performance visualized using a confusion matrix.
