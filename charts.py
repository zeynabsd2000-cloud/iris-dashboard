import matplotlib.pyplot as plt
import seaborn as sns

def pie_chart(df):
    fig, ax = plt.subplots()
    df["species"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_title("Species Distribution")
    return fig


def histogram(df):
    fig, ax = plt.subplots()
    ax.hist(df["sepal_length"], bins=10)
    ax.set_title("Sepal Length Distribution")
    return fig


def scatter(df):
    fig, ax = plt.subplots()
    ax.scatter(df["sepal_length"], df["petal_length"])
    ax.set_title("Sepal Length vs Petal Length")
    return fig


def heatmap(df):
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True), annot=True, ax=ax)
    ax.set_title("Correlation Heatmap")
    return fig


def boxplot(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="species", y="sepal_length", ax=ax)
    ax.set_title("Box Plot")
    return fig


def bar_chart(df):
    fig, ax = plt.subplots()
    df["species"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Species Count")
    return fig


def line_chart(df):
    fig, ax = plt.subplots()
    ax.plot(df.index, df["sepal_length"])
    ax.set_title("Sepal Length Trend")
    return fig


def area_chart(df):
    fig, ax = plt.subplots()
    ax.fill_between(df.index, df["petal_length"], alpha=0.5)
    ax.set_title("Area Chart")
    return fig


def count_plot(df):
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="species", ax=ax)
    ax.set_title("Count Plot")
    return fig


def violin_plot(df):
    fig, ax = plt.subplots()
    sns.violinplot(data=df, x="species", y="sepal_length", ax=ax)
    return fig