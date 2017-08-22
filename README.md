# Plot template

This repo contains different type of plots in python.

What are the choices for ploting data?

1.  Seaborn
2.  pandas
3.  Matplotlib


# Seaborn
Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.

Seaborn provides a very high-level interface. It's versy hard and imposible in some cases to customize the plot, for instance it's not easily possible to plot `stack plot`.


# Pandas
Pandas provides basics to easily create decent looking plots.
For instance, to plot stack or bra plot we can draw it in just few lines:

``` python
# Plot type
matplotlib.style.use('ggplot')

# Loading input DataFrame

input_data = pd.read_csv('../data/01-test.csv', index_col='name')

#Bar plo
input_data.plot.bar()

#Stack plot
input_data.plot.bar(stacked=True)

```
But again there is not enough control on the labels and places bars.

Therefore, I prefer using `matplotlib`.

# Matplotlib

Matplotlib provides a fine control on all the options. At the begining it's hard to start with matplotlib but after a while it becomes very handy. (Remember learning curve!!).

That's the reason which I have provided this repository to include most of the plots which I needed during my _Graduate studies_.
