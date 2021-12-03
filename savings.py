print("")
print("PROJECT SAVINGS")
print("")
print("Please select what savings data you want to analyze. :-")
print("")
print("Money Saved in Accordance to Female and Male")
print("Money Saved in Accordance to Highschool Completion")
print("Money Saved in Accordance to Wealthiness")
print("")
save = input("Please enter your choice : ").lower()

if(save == "money saved in accordance to female and male"):

  import pandas as pd
  import plotly.express as px
  import statistics

  #importing

  from google.colab import files
  media = files.upload()

  df = pd.read_csv("gender_savings.csv")
  fig = px.scatter(df, y = "quant_saved", color = "female", title = "Money Saved in Accordance to Female and Male")
  fig.show()

  #mean, median, mode, stdev



  import csv 

  with open("gender_savings.csv", newline = "") as file:
    reader = csv.reader(file)
    data = list(reader)

  data.pop(0)

  savings_data = []

  for i in data:
    savings_data.append(float(i[0]))

  print(f"Mean of Savings is {statistics.mean(savings_data)}")
  print(f"Median of Savings is {statistics.median(savings_data)}")
  print(f"Mode of Savings is {statistics.mode(savings_data)}")
  print(f"STDEV of Savings is {statistics.stdev(savings_data)}")

  #savings according to gender

  male_savings = []
  female_savings = []

  for i in data:
    if(int(i[1]) == 1):
      female_savings.append(float(i[0]))

    else:
      male_savings.append(float(i[0]))

  print("These are the results of females who saved : ")
  print(f"Mean of Savings is {statistics.mean(female_savings)}")
  print(f"Median of Savings is {statistics.median(female_savings)}")
  print(f"Mode of Savings is {statistics.mode(female_savings)}")
  print("")
  print("These are the results of males who saved : ")
  print(f"Mean of Savings is {statistics.mean(male_savings)}")
  print(f"Median of Savings is {statistics.median(male_savings)}")
  print(f"Mode of Savings is {statistics.mode(male_savings)}")

  #Sampling

  import plotly.figure_factory as ff
  import plotly.graph_objects as go
  import random

  import random 
  all_savings = df['quant_saved'].tolist()

  sampling_means = []



  for i in range(1000):
    temp_list = []
    
    for j in range(100):
      temp_list.append(random.choice(all_savings))
    
    sampling_means.append(statistics.mean(temp_list))

  head_mean = statistics.mean(sampling_means)

  fig = ff.create_distplot([sampling_means], ['Sample of Savings'], show_hist = False)
  fig.add_trace(go.Scatter(x = [head_mean, head_mean], y = [0, 0.1], mode = "lines", name = "Mean of all Samples"))

  fig.show()

  print(f"Mean of Savings is {statistics.mean(sampling_means)}")
  print(f"Median of Savings is {statistics.median(sampling_means)}")

  print(f"STDEV of Savings is {statistics.stdev(sampling_means)}")

  #Correlation

  import numpy as np

  gender = []
  savings = []

  for i in data:
    
    gender.append(float(i[1]))
    savings.append(float(i[0]))

  correlation = np.corrcoef(gender, savings)

  print("Correlation is ", correlation[0, 1])

#####Savings on highschool completion

if(save == "money saved in accordance to highschool completion"):

  import pandas as pd
  import plotly.express as px
  import statistics

  #importing

  from google.colab import files
  media = files.upload()

  df = pd.read_csv("gender_savings.csv")
  fig = px.scatter(df, y = "quant_saved", color = "highschool_completed", title = "Money Saved in Accordance to Highschool Completion")
  fig.show()

  #mean, median, mode, stdev

  import csv 

  with open("gender_savings.csv", newline = "") as file:
    reader = csv.reader(file)
    data = list(reader)

  data.pop(0)

  savings_data = []

  for i in data:
    savings_data.append(float(i[0]))

  print(f"Mean of Savings is {statistics.mean(savings_data)}")
  print(f"Median of Savings is {statistics.median(savings_data)}")
  print(f"Mode of Savings is {statistics.mode(savings_data)}")
  print(f"STDEV of Savings is {statistics.stdev(savings_data)}")

  #savings according to highschool completion

  complete_savings = []
  incomplete_savings = []

  for i in data:
    if(int(i[2]) == 1):
      complete_savings.append(float(i[0]))

    else:
      incomplete_savings.append(float(i[0]))

  print("These are the results of highschool graduates who saved : ")
  print(f"Mean of Savings is {statistics.mean(complete_savings)}")
  print(f"Median of Savings is {statistics.median(complete_savings)}")
  print(f"Mode of Savings is {statistics.mode(complete_savings)}")
  print("")
  print("These are the results of highschool drop-outs who saved : ")
  print(f"Mean of Savings is {statistics.mean(incomplete_savings)}")
  print(f"Median of Savings is {statistics.median(incomplete_savings)}")
  print(f"Mode of Savings is {statistics.mode(incomplete_savings)}")

  #Sampling

  import plotly.figure_factory as ff
  import plotly.graph_objects as go
  import random

  import random 
  all_savings = df['quant_saved'].tolist()

  sampling_means = []



  for i in range(1000):
    temp_list = []
    
    for j in range(100):
      temp_list.append(random.choice(all_savings))
    
    sampling_means.append(statistics.mean(temp_list))

  head_mean = statistics.mean(sampling_means)

  fig = ff.create_distplot([sampling_means], ['Sample of Savings'], show_hist = False)
  fig.add_trace(go.Scatter(x = [head_mean, head_mean], y = [0, 0.1], mode = "lines", name = "Mean of all Samples"))

  fig.show()

  print(f"Mean of Savings is {statistics.mean(sampling_means)}")
  print(f"Median of Savings is {statistics.median(sampling_means)}")

  print(f"STDEV of Savings is {statistics.stdev(sampling_means)}")

  #Correlation

  import numpy as np

  completion = []
  savings = []

  for i in data:
    
    completion.append(float(i[2]))
    savings.append(float(i[0]))

  correlation = np.corrcoef(completion, savings)

  print("Correlation is ", correlation[0, 1])


#####Savings on wealthiness

if(save == "money saved in accordance to wealthiness"):


  import pandas as pd
  import plotly.express as px
  import statistics

  #importing

  from google.colab import files
  media = files.upload()

  df = pd.read_csv("gender_savings.csv")
  fig = px.scatter(df, y = "quant_saved", color = "wealthy", title = "Money Saved in Accordance to Wealthiness")
  fig.show()

  #mean, median, mode, stdev

  import csv 

  with open("gender_savings.csv", newline = "") as file:
    reader = csv.reader(file)
    data = list(reader)

  data.pop(0)

  savings_data = []

  for i in data:
    savings_data.append(float(i[0]))

  print(f"Mean of Savings is {statistics.mean(savings_data)}")
  print(f"Median of Savings is {statistics.median(savings_data)}")
  print(f"Mode of Savings is {statistics.mode(savings_data)}")
  print(f"STDEV of Savings is {statistics.stdev(savings_data)}")

  #savings according to highschool completion

  wealthy_savings = []
  mid_savings = []

  for i in data:
    if(int(i[3]) == 1):
      wealthy_savings.append(float(i[0]))

    else:
      mid_savings.append(float(i[0]))

  print("These are the results of Wealthy people who saved : ")
  print(f"Mean of Savings is {statistics.mean(wealthy_savings)}")
  print(f"Median of Savings is {statistics.median(wealthy_savings)}")
  print(f"Mode of Savings is {statistics.mode(wealthy_savings)}")
  print("")
  print("These are the results of Middle class people who saved : ")
  print(f"Mean of Savings is {statistics.mean(mid_savings)}")
  print(f"Median of Savings is {statistics.median(mid_savings)}")
  print(f"Mode of Savings is {statistics.mode(mid_savings)}")

  #Sampling

  import plotly.figure_factory as ff
  import plotly.graph_objects as go
  import random

  import random 
  all_savings = df['quant_saved'].tolist()

  sampling_means = []



  for i in range(1000):
    temp_list = []
    
    for j in range(100):
      temp_list.append(random.choice(all_savings))
    
    sampling_means.append(statistics.mean(temp_list))

  head_mean = statistics.mean(sampling_means)

  fig = ff.create_distplot([sampling_means], ['Sample of Savings'], show_hist = False)
  fig.add_trace(go.Scatter(x = [head_mean, head_mean], y = [0, 0.1], mode = "lines", name = "Mean of all Samples"))

  fig.show()

  print(f"Mean of Savings is {statistics.mean(sampling_means)}")
  print(f"Median of Savings is {statistics.median(sampling_means)}")

  print(f"STDEV of Savings is {statistics.stdev(sampling_means)}")

  #Correlation

  import numpy as np

  wealthy = []
  savings = []

  for i in data:
    
    wealthy.append(float(i[3]))
    savings.append(float(i[0]))

  correlation = np.corrcoef(wealthy, savings)

  print("Correlation is ", correlation[0, 1])
