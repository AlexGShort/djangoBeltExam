from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Count
from .models import User, Poke

# Create your views here.
def index(request):
    # allUsers = User.objects.all()
    allUsers = User.objects.annotate(num_pokes=Count('poked__poked')).exclude(id=request.session['user_id'])
    pokedYou = User.objects.filter(poker__poked = request.session['user_id']).annotate(num_pokes=Count('poker__poked')).order_by('-num_pokes')
    numPokers = len(pokedYou)
    print "#"*50
    print "pokedYou length: {}".format(len(pokedYou))


    allPokes = Poke.objects.all()

    context = {
        'users': allUsers,
        'pokedYou': pokedYou,
        'pokes': allPokes,
        'numPokers': numPokers
    }

    return render(request, 'beltexam/index.html', context)

def poke(request):
    # print "@"*50
    # print "poker_user: {}, poked_user: {}".format(request.session['user_id'], request.POST)
    poker_user = User.objects.get(id=request.session['user_id'])
    # print "poked_id: {}".format(request.POST['poked_user'])
    poked_user = User.objects.get(id=request.POST['poked_user'])
    newPoke = Poke.objects.create(poker=poker_user, poked=poked_user)


    return redirect(reverse('beltexam:index'))
