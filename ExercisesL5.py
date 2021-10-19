@my_decorator
def f(x=0.7,y=8.8):
  return sum(x,y)

print(f)


#Variable in path names: providing multiple inputs eg. input_age and input_name

@app.route("/name/<input_name>/age/<int:input_age>")
def my_func(input_name, input_age):
  return f" <b>Hellow</b> {input_name}! Looking good for {input_age}!"

#run flask -> will pass this into variables for function we are working with
