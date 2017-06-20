from django.shortcuts import render, redirect

img_basepath = 'imgs/'
colors = ['red','blue','orange','purple']

def index(request):
    
    return render(request, "ninjas/index.html")

def ninjas(request):
    turtles = {
        'image': 'ninjas/{}tmnt.jpg'.format(img_basepath)
        }
    return render(request, "ninjas/ninjas.html", turtles)

def ninjascolor(request, color):
    if color in colors:
        turtles = {
            'image': 'ninjas/{}{}.jpg'.format(img_basepath, color)
        }
    else:
        turtles = {
            'image': 'ninjas/{}notapril.jpg'.format(img_basepath)
        }
    return render(request, "ninjas/ninjas.html", turtles)