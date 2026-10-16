from flask import Flask,render_template,request
app =Flask(__name__)## it tells flask where application is located
import joblib
model=joblib.load(r'C:\Users\Win 11\Desktop\data science\6-months-data-science\machine learning\loan_project\loan project\model\dt_loan_system_model.lb')
@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/predict",methods=['POST','GET'])
def predict():

    if request.method =='POST':

        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        phone= request.form['phone']
        email= request.form['email']

        ## loan information
        income=int(request.form['income'])
        credit_score=int(request.form['credit_score'])
        loan_amount=int(request.form['loan_amount'])
        years_employed=int(request.form['years_employed'])
        
       

        print("Loan information:-",[[income,credit_score,loan_amount,years_employed]])
        data=[[income,credit_score,loan_amount,years_employed]]
        pred=model.predict(data)
        print("type of prediction:-",type(pred))
        pred=int (pred[0])

        pred_dict={
            1:"yes",0:"no"
        }

        pred=pred_dict.get(int(pred))

        print("prediction:-",pred)
        return render_template("form.html",result=pred)

if __name__=="__main__":
    app.run(debug=True) ## automatically reads the server when we change the code

