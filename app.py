from flask import Flask,render_template,request
import pickle as pl
import numpy as np

popular_df = pl.load(open('popular.pkl','rb'))
books = pl.load(open('books.pkl','rb'))
pt = pl.load(open('pt.pkl','rb'))
similarity_score = pl.load(open('similarity_score.pkl','rb'))



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html'
                           ,book_name = list(popular_df['Book-Title'].values)
                           ,author = list(popular_df['Book-Author'].values)
                           ,img = list(popular_df['Image-URL-M'].values)
                           ,votes = list(popular_df['num_ratings'].values)
                           ,rating = list(popular_df['avg_ratings'].values))


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['POST'])
def recommend_books():
    user_input = request.form.get('book_name')
    if user_input not in pt.index:
        return []
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_score[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:11]

    recommendations = []

    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')

        if not temp_df.empty:
            recommendations.append({
                'title': temp_df['Book-Title'].values[0],
                'author': temp_df['Book-Author'].values[0],
                'image': temp_df['Image-URL-M'].values[0]
            })

    return render_template('recommend.html',data=recommendations)

if __name__ == '__main__':
    app.run(debug=True)