import mysql.connector
import pickle
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='rafaelcyin',
    database='register'
)

cursor = mydb.cursor()


def create_patient_table():
    sql = "CREATE TABLE IF NOT EXISTS patients (id SERIAL PRIMARY KEY, f_name VARCHAR(255), l_name VARCHAR(255), " \
          "birth VARCHAR(255), cpf VARCHAR(255), gender VARCHAR(10))"
    cursor.execute(sql)
    mydb.commit()


def register_patient(f_name, l_name, birth, cpf, gender):
    sql = "INSERT INTO patients (f_name, l_name, birth, cpf, gender) VALUES (%s, %s, %s, %s, %s)"
    patient = (f_name, l_name, birth, cpf, gender)
    cursor.execute(sql, patient)
    mydb.commit()


def search_patient(id):
    try:
        sql = "SELECT * FROM patients WHERE id = (%s)"
        patient_id = (id,)
        cursor.execute(sql, patient_id)
        result = cursor.fetchall()
        # for r in result:
        #     patient_info = r
        mydb.commit()
        return result
    except:
        print("Error")


def create_classifications_table():
    sql = "CREATE TABLE IF NOT EXISTS classifications (id INTEGER, class VARCHAR)"
    cursor.execute(sql)
    mydb.commit()


def classify_patient(id):
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    file_name = 'images/'+str(id)+'.png'
    img = cv2.imread(file_name)
    # print(plt.imshow(img))
    # plt.show()

    resize = tf.image.resize(img, (256, 256))
    # plt.imshow(resize.numpy().astype(int))
    # plt.show()

    prediction = model.predict(np.expand_dims(resize / 255, 0))
    prob = prediction[0]
    return float(prob)



# sql = "DROP TABLE patients"
# cursor.execute(sql)
# mydb.commit()
