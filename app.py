from flask import Flask, render_template, jsonify

app = Flask(__name__)



JOBS = [
    {
        'id': 1,
        'title': 'Data analyst',
        'location' : 'Bangalore, India',
        'salary' : 'Rs 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data scientist',
        'location' : 'Delhi, India',
        'salary' : 'Rs 12,00,000'
    },
    {
        'id': 3,
        'title': 'Business analyst',
        'location' : 'San Francisco, USA',
        'salary' : '$100000'
    },
    {
        'id': 4,
        'title': 'Data engineer',
        'location' : 'Remote',
        'salary' : 'Rs 12,00,000'
    },
]


@app.route("/")
def hello():
    return render_template('index.html', jobs=JOBS, company_name='Jovian')


# @app.route("/jobdetails")
# def job_details():
#     return render_template('/jobdetails.html', jobs=JOBS)



# @app.route("/api/jobs")
# def list_jobs():
#     return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)