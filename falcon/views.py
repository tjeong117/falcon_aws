from django.shortcuts import render
from django.db import connection
import pandas
import matplotlib.pyplot as plt
import datetime
import matplotlib
matplotlib.use('Agg')

import pandas_datareader.data as pdr
# Create your views here.



# Create your views here.
def index(request):
    return render(request, 'index.html')


def top(request):
    return render(request, 'common/top.html')


def computational_science(request):
    return render(request, 'projects/computation/computation_science.html')


def introduction(request):
    print("introduction")
    return render(request, 'introduce/introduction.html')


def main(request):
    print("main")
    return render(request, 'main.html')


def stock(request):
    return render(request, 'projects/datascience/stock/stock.html')

def stock_demo(request):

    select_query = "SELECT ssymbol, sname FROM stock_tb"
    print(select_query)
    cursor = connection.cursor()
    cursor.execute(select_query)

    dic = {'sym': cursor.fetchall(),
           'dyear':  [x for x in range(2010, datetime.datetime.now().year + 1)],
           'dmonth': [y for y in range(1, 13)],
           'dday': [z for z in range(1, 32)]}

    return render(request, "projects/datascience/stock/stock_demo.html", dic)


def stock_graph(request):
    if 'symbol' in list(request.POST.keys()):
        # print("0")
        sym = request.POST['symbol']
        # print(sym)
        s_month = request.POST['s_month']
        # print(s_month)
        s_day = request.POST['s_day']
        # print(s_day)
        s_year = request.POST['s_year']
        # print(s_year)

        e_month = request.POST['e_month']
        # print(e_month)
        e_day = request.POST['e_day']
        # print(e_day)
        e_year = request.POST['e_year']
        # print(type(e_year))
        start = datetime.datetime(int(s_year), int(s_month), int(s_day))
        # print(start)
        end = datetime.datetime(int(e_year), int(e_month), int(e_day))
        # print("=======")
        axis = request.POST["checked_ax"]
        # print("========")
        axis = axis[:-1]

        print(axis)
        axis = axis.split(",")

        print("aaaaaaaa" ,sym)
        print("s:",start, "e:", end)
        try:
            data = pdr.DataReader(sym, 'yahoo', start=start.strftime("%Y-%m-%d"), end=end.strftime("%Y-%m-%d"))
        except KeyError as e:
            print(e)
            e_img_path = 'projects/datascience/images.png'
            e_img_root = 'falcon/static/'
            dic = {'src': e_img_path}
            return render(request, 'projects/datascience/stock/stock_graph.html', dic)

        # print(data.head())
        data = data[data['Volume'] != 0]

        ma20 = data["Adj Close"].rolling(window=20).mean()
        ma60 = data['Adj Close'].rolling(window=60).mean()

        data.insert(len(data.columns), "MA20", ma20)
        data.insert(len(data.columns), "MA60", ma60)
        # print(data.head())

        img_path = 'projects/datascience/result/mygraph.png'
        img_root = 'falcon/static/'
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        for i in axis:
            plt.plot(data.index, data[i], label=i)

        plt.legend(loc="best")
        plt.savefig(img_root + img_path)
        dic = {'src': img_path}
        return render(request, 'projects/datascience/stock/stock_graph.html', dic)
    else:
        img_path = 'projects/datascience/307.jpg'
        img_root = 'falcon/static/'
        dic = {'src': img_path}
        return render(request, 'projects/datascience/stock/stock_graph.html', dic)


def resume(request):
    return render(request, 'resume/resume.html')


def award(request):
    return render(request, 'award/award.html')