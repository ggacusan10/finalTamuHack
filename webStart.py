from flask import Flask, render_template, request
app = Flask(__name__, static_url_path="/static, /static/css")
import sys
import restaurants
import museums

@app.route('/')
def index():
    return render_template("landing_page.html")

@app.route('/itinerary')
def itinerary():
    return render_template("query_page.html")

@app.route('/result')
def result():
    i = random.randint(0,1)
    return render_template("result_page.html", i11= resArr[0], i12="he", i13="ho", i21="hu", i22="he", i23="ha ", i31=" ", i32=" ", i33=" ")

@app.route('/handle-form', methods=['POST'])
def registerForm():
    print("Hello")
    if request.method == 'POST':

        res = restaurants.restaurantData()
        mus = museums.museumData()
        resArr = []
        musArr = []

        for i in range(0,3):
            #r1 = request.form.get("city")
            #resArr.append(res.getRestaurant(r1).title())
            resArr.append(res.getRestaurant(request.form.get("city").title()))

            #r2 = request.form.get("city")
            #musArr.append(res.getMuseum(r2).title())
            #print(request.form.get())
            musArr.append(mus.getMuseum(request.form.get("city").upper()))


        #return str(request.form.get('city'))
        #print(resArr[0])
        i11Str = "9:00-10:00- "+ str(resArr[0])
        i21Str = "9:00-10:00- "+ str(resArr[1])
        i31Str = "9:00-10:00- "+ str(resArr[2])
        i12Str = "3:30-5:00- "+ str(musArr[0])
        i22Str = "3:30-5:00- "+ str(musArr[1])
        i32Str = "3:30-5:00- "+ str(musArr[2])
        return render_template("result_page.html", i11= i11Str, i12=i12Str, i13= " " , i21= i21Str, i22=i22Str, i23=" ", i31=i31Str, i32= i32Str, i33=" ")
    #return render_template("result_page.html", i11="hi ", i12="he", i13="ho", i21="hu", i22="he", i23="ha ", i31=" ", i32=" ", i33=" ")

    return "Nothin"
if __name__ == "__main__":
    app.run()
