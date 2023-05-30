import psycopg2
from flask import Flask
from flask_restful import Api, Resource
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
import psycopg2
app = Flask(__name__)
api = Api(app)
@app.route("/swagger")
def get_swagger():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Flask Swagger API"
    return swag

swagger_ui_blueprint = get_swaggerui_blueprint(
    "/swagger",
    "/swagger.json",
    config={"app_name": "Flask Swagger API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix="/swagger-ui")

class Dataset1(Resource):
    def get(self):
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="your_database_name",
            user="your_username",
            password="your_password"
        )
        cursor = conn.cursor()
        
        # Fetch data from Dataset 1
        cursor.execute("SELECT * FROM dataset1_table")
        dataset1_data = cursor.fetchall()
        
        # Perform join operation with Dataset 2
        cursor.execute("SELECT * FROM dataset1_table INNER JOIN dataset2_table ON dataset1_table.id = dataset2_table.id")
        joined_data = cursor.fetchall()
        
        conn.close()
        
        response = {
            "dataset1_data": dataset1_data,
            "joined_data": joined_data
        }
        
        return response


class Dataset2(Resource):
    def get(self):
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="your_database_name",
            user="your_username",
            password="your_password"
        )
        cursor = conn.cursor()
        
        # Fetch data from Dataset 2
        cursor.execute("SELECT * FROM dataset2_table")
        dataset2_data = cursor.fetchall()
        
        # Perform join operation with Dataset 1
        cursor.execute("SELECT * FROM dataset2_table INNER JOIN dataset1_table ON dataset2_table.id = dataset1_table.id")
        joined_data = cursor.fetchall()
        
        conn.close()
        
        response = {
            "dataset2_data": dataset2_data,
            "joined_data": joined_data
        }
        
        return response


if __name__ == "__main__":
    app.run(debug=True)