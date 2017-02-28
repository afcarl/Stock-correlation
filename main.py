from yahoo_finance import Share
from pprint import pprint
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.svm import SVR

def plot_produce(share_name):
    stock = Share(share_name)
    yahoo_data = (stock.get_historical('2014-04-25', '2017-02-28'))
    stock_history = [];
    x_axis = [];
    y_axis = []
    for date in yahoo_data[::-1]:
        stock_history.append((date['Close'], datetime.strptime(date['Date'], '%Y-%m-%d')))
        x_axis.append(datetime.strptime(date['Date'], '%Y-%m-%d'))
        y_axis.append(date['Close'])
    return x_axis, y_axis

def main():
    yh_x_axis, yh_y_axis = plot_produce("YHOO")
    gg_x_axis, gg_y_axis = plot_produce("GOOGL")
    clf = SVR(C=1.0, epsilon=0.2)
    clf.fit(yh_x_axis, gg_x_axis)

    plt.plot(clf, yh_y_axis)
    plt.show()

if __name__ == '__main__':
    main()