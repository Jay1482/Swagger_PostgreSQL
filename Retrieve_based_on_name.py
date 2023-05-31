import psycopg2
from flask import Flask,jsonify,send_from_directory
from flask_restx import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

def fetch_data_from_database(id,name ):
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="data_jsonify",
        user="postgres",
        password="1010"
    )
    cursor = conn.cursor()

    #cursor.execute('SELECT * FROM "User" where (id =%s) or (name=%s)',(id,name))
    cursor.execute('SELECT * FROM "User" u inner join "Post" p on p.author_id =u.id where (id =%s) or (name=%s)',(id,name))
    data = cursor.fetchall()

    conn.close()

    return data

class DataResource(Resource):
    @api.doc(responses={200: 'Data fetched successfully'}, description='Fetches data from PostgreSQL and returns it')
    def get(self,id,name):
        try:
            """Fetches data from PostgreSQL and returns it"""
            data = fetch_data_from_database(id,str(name))
            
            response = {
                'id': data[0][0],
                'name':data[0][1],
                'age': data[0][2]
            }
            return jsonify(response)
        except IndexError:
            return jsonify({
                "Error" : "There is no user with this data has Posted yet !!!"
            })

api.add_resource(DataResource, '/data/<int:id>/<string:name>')



SWAGGER_URL = '/api/swagger'
API_URL = '\static\swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  
    API_URL,
    config={
        'app_name': "Test application"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(debug=True)
