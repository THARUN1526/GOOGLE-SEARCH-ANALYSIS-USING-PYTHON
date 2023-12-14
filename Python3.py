data.reset_index().plot(x="geoName", 
                        y="Machine Learning", 
                        figsize=(15,12), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()