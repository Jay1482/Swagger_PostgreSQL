import psycopg2
from flask import Flask
from flask_restx import Api, Resource, fields
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

    cursor.execute('SELECT * FROM "User" where (id =%s) or (name=%s)',(id,name))
    data = cursor.fetchall()

    conn.close()

    return data

data_model = api.model('Data', {
    'data': fields.List(fields.String)
})


class DataResource(Resource):
    @api.doc(responses={200: 'Data fetched successfully'}, description='Fetches data from PostgreSQL and returns it')
    @api.marshal_with(data_model)
    def get(self,id,name):
        """Fetches data from PostgreSQL and returns it"""
        data = fetch_data_from_database(id,str(name))
        return {'data': data}

api.add_resource(DataResource, '/data/<int:id>/<string:name>')

@app.route("/swagger.json")
def get_swagger():
    return api.__schema__

swagger_ui_blueprint = get_swaggerui_blueprint(
    "/swagger",
    "/swagger.json",
    config={"app_name": "Flask Swagger API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix="/swagger-ui")

if __name__ == "__main__":
    app.run(debug=True)
