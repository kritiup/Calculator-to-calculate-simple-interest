first project
def simple_interest(principal, rate, time):
  return (principal * rate * time) / 100

principal = 10000
rate = 7.5
time = 5

interest = simple_interest(principal, rate, time)
print(f"Simple interest: {interest}")