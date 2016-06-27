from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta, date
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter, MonthLocator, WeekdayLocator, DayLocator, MO, TU, WE, TH, FR, SA, SU

# from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


# def db(request):

#     greeting = Greeting()
#     greeting.save()

#     greetings = Greeting.objects.all()

#     return render(request, 'db.html', {'greetings': greetings})

def generateGraphView(request, graph_title=None):
    
    # from matplotlib import pyplot as plt
    weekdays = [MO, TU, WE, TH, FR, SA, SU]
    now = datetime.now()


    fig=Figure()
    ax=fig.add_subplot(111)
    xdata=[]
    ydata=[int(obs) for obs in request.GET.get('y', "").split(',') if obs and len(obs) > 0]

    x = request.GET.get('x', 'm')
    anchorTimeString = request.GET.get('a', now.strftime('%Y%m%d'))
    anchorTime = datetime.strptime(anchorTimeString, '%Y%m%d')
    figureWidth = int(request.GET.get('px', '600'))
    figureHeight = int(request.GET.get('py', '300'))

    dateInterval = 30
    if x == 'm': 
        dateInterval = 30
        dateMax = (anchorTime.replace(day=15) + timedelta(days=30)).replace(day=1) - timedelta(days=1)
        locator = MonthLocator()
        dateFormat = '%b %Y'
        barWidth = dateInterval/3
    if x =='w':
        dateInterval = 7
        dateMax = anchorTime + timedelta(days=6)
        locator = WeekdayLocator(weekdays[anchorTime.weekday()]) 
        dateFormat = '%m/%d/%Y'
        barWidth = dateInterval/3
    if x == 'd':
        dateInterval = 1
        dateMax = anchorTime + timedelta(days=0.8)
        locator = DayLocator()
        dateFormat = '%m/%d'
        barWidth = dateInterval

    
    delta=timedelta(days=dateInterval)

    ydata.reverse()
    for obs in ydata:
        if x == 'm':
            anchorTime = anchorTime.replace(day=15)
            xdata.append(anchorTime)
        elif x == 'w':
            xdata.append(anchorTime + timedelta(days=3))
        elif x == 'd':
            xdata.append(anchorTime)
        anchorTime = anchorTime - delta

    if x == 'm': 
        dateMin = (anchorTime + timedelta(days=dateInterval)).replace(day=1)
    elif x == 'w': 
        dateMin = anchorTime + timedelta(days=6)
    elif x == 'd': 
        dateMin = anchorTime + timedelta(days=0)
    
    ydata.reverse()
    xdata.reverse()

    # ax.plot_date(xdata, ydata, '-')
    ax.bar(xdata, ydata, width=barWidth, align="center")

    for i,j in zip(xdata,ydata):
        ax.annotate('%s' %j, xy=(i,j), xytext=(0,5), horizontalalignment='center', textcoords='offset points')

    ax.xaxis.set_major_formatter(DateFormatter(dateFormat))
    ax.xaxis.set_major_locator(locator)
    # ax.grid(True)
    ax.set_xlim(dateMin, dateMax)
    ax.set_ylim(0, max(ydata) * 1.3)
    fig.patch.set_facecolor('white')
    if graph_title:
        title = graph_title.replace('_', ' ').title()
        fig.suptitle(title, fontsize=14)

    DPI = fig.get_dpi()
    fig.set_size_inches(figureWidth/float(DPI), figureHeight/float(DPI))

    fig.autofmt_xdate(ha='left')
    canvas=FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response