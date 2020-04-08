# goal: track and detect spikes in COVID outbreaks

# import modules
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression as LR

# 1. grab data about COVID-19 statistics
content = urllib.request.urlopen("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv").read()
content = str(content)
print(content)

# 2. process data 
# print(type(content))
complete_list = content.split("\\n")
# print(type(complete_list))

# print(complete_list[0:5])

print(len(complete_list))
print(type(complete_list[0]))
content_list = complete_list[1:]
print(len(content_list))
# print(content_list[0])
print()

infection_dict = dict()

for row in content_list:
  try:
    infections = [int(x) for x in row.split(',')[4:]]
    location = row.split(',')[1]+'-'+row.split(',')[0]
    # print(location + ': ' + str(infections))
    infection_dict[location] = infections
  except ValueError:
    pass
  except IndexError:
    pass

list_of_keys = list(infection_dict.keys())

for key in list_of_keys:
  if "canada" in key.lower():
    plt.plot(infection_dict[key], label=key)
  if "china" in key.lower():
    plt.plot(infection_dict[key], label=key)

# 3. detect spikes
plt.legend()
plt.savefig("foo.png")

# bonus: prediction 
infection_list = list()
for key in list_of_keys:
  infection_list.append(infection_dict[key])


X_data = np.array(list(range(len(infection_dict["Canada-Quebec"]))))
y_data = np.array(infection_dict["Canada-Quebec"])

model = LR()
model.fit(X=X_data.reshape(-1,1), y=y_data)

predictions = model.predict([[x] for x in range(200)])

plt.close() 
plt.plot(predictions, label="Predictions")
# plt.plot(infection_dict["Canada-Quebec"])
plt.savefig("foo.png")
print("Done!")
print()

counter = 0
for x in predictions:
  print(counter, x)
  counter += 1
