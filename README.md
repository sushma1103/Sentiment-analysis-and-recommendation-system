# Sentiment analysis of company reviews and recommendation system
This project provides a system where the user can input any company name and the system does web scraping using a module called beautiful soup in python, collects reviews about that company from various employment websites and does sentiment analysis on the reviews. The system then displays the percentage of positive, negative and neutral reviews.

These ratings from sentiment analysis are then stored in a file which is used for further classification. C4.5 algorithm is used for classifying companies to 3 different classes: good , moderate or bad. The ratings obtained from C4.5 classification is used for showing recommendations of companies that belong to a similar class.

The user can select one of the recommended companies and compare visually by a graph displayed. The system also mines data from twitter to display the trending tweets about the company that is being queried. This application is developed using python for GUI and sentiment analysis. The recommendation system is built using R. This application is useful for those looking to make career decisions. 
