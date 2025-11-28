Book Recommendation System

📌 Overview

This project is a Book Recommendation System built using Flask,
scikit-learn, and preprocessed dataset files.
The system recommends similar books based on user input using a
similarity matrix and displays popular books on the homepage.

------------------------------------------------------------------------

🚀 Features

-   Shows a curated list of popular books using precomputed popularity
    metrics.
-   Provides book recommendations using:
    -   Pivot table (pt.pkl)
    -   Cosine similarity scores (similarity_score.pkl)
-   Accepts user input to search for a specific book.
-   Displays recommended books with:
    -   Title
    -   Author
    -   Image

------------------------------------------------------------------------

🧠 Technologies Used

-   Flask – For web routing and UI rendering
-   scikit-learn – For similarity computation
-   Pickle – To load preprocessed machine learning artifacts
-   NumPy – For numerical operations
-   HTML Templates – index.html and recommend.html

------------------------------------------------------------------------

📂 Project Structure

    |-- app.py
    |-- templates/
    |     |-- index.html
    |     |-- recommend.html
    |-- popular.pkl
    |-- books.pkl
    |-- pt.pkl
    |-- similarity_score.pkl
    |-- README.txt

------------------------------------------------------------------------

🧪 How It Works

1.  The system loads necessary data files using pickle.
2.  The homepage (/) displays the list of popular books.
3.  The recommendation page (/recommend) allows the user to submit a
    book name.
4.  Using the similarity score matrix:
    -   The system finds the most similar books.
    -   Fetches their information from the dataset.
5.  Displays results on the same page.

------------------------------------------------------------------------

▶️ Running the Application

1. Install Dependencies

    pip install flask numpy scikit-learn

2. Run the App

    python app.py

3. Access in Browser

    http://127.0.0.1:5000/

------------------------------------------------------------------------

📥 Summary

This project provides a simple yet effective book recommendation engine
using machine learning and Flask. It visualizes popular books and
returns similar book suggestions based on past data and similarity
computations.

------------------------------------------------------------------------

✨ Author

Developed for learning and academic purposes.
