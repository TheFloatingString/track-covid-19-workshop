# import modules
import urllib.request
import matplotlib.pyplot as plt

# scrape GitHub page
contents = urllib.request.urlopen("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv").read()

# process content
contents = str(contents)
content_list = list(contents.split('\\r\\n'))
header_list = content_list[0]
body_list = content_list[1:]
print(len(content_list))

# define dictionaries
time_dict = {}
body_dict = {}

# loop and process
for row in body_list:
  b = 0
  row_list = row.split(',')
  # print(row_list[0])
  if row_list[0]=="\"Bonaire":
    # print(True)
    b = 1
  if row_list[0] != '':
    print(row_list[1]+'-'+row_list[0])
  else:
    print(row_list[1])
  # print([int(x.replace("'",'')) for x in row_list[4+b:]])
  plt.plot([int(x.replace("'",'')) for x in row_list[4+b:]])

# save image
plt.savefig("test.png")


