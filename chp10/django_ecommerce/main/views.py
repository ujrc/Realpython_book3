# Create your views here.
from django.shortcuts import render_to_response,RequestContext
from payments.models import User
from main.models import MarketingItem, StatusReport, Announcement
from datetime import date, timedelta
class MarketItem(object):
    """docstring for MarketItem"""
    def __init__(self, img_name, heading,caption, button_title='View details', button_link='register' ):
        super(MarketItem, self).__init__()
        self.img_name=img_name
        self.heading=heading
        self.caption=caption
        self.button_title=button_title
        self.button_link=button_link

market_items=[

    MarketItem(
        img_name="yoda.jpg",
        heading="Hone your Jedi Skills",
        caption="All members have access to our unique \
         training and achievements latters. Progress through the \
        levels and show everyone who the top Jedi Master is!",
        button_title="Sign Up Now"),

    MarketItem(
        img_name="clone_army.jpg",
        heading="Build your Clan",
        caption="Engage in meaningful conversation, or \
        bloodthirsty battle! If it's related to \
        Star Wars, in any way, you better believe we do it.",
        button_title="Sign Up Now"),
    MarketItem(
        img_name="leia.jpg",
        heading="Find Love",
        caption="Everybody knows Star Wars fans are the \
        best mates for Star Wars fans. Find your \
        Princess Leia or Han Solo and explore the \
        stars together.",
        button_title="Sign Up Now"
    ),
    ]

def index(request):
    uid = request.session.get('user')
    if uid is None:
        #main landing page
        market_items=MarketingItem.objects.all()
        return render_to_response('main/index.html',
        {'marketing_items': market_items})
    else:
        #membership page
        status=StatusReport.objects.all().order_by('-when')[:20]
        announce_date=date.today()-timedelta(days=30)
        announces=(Announcement.objects.filter(publication_date__gt=announce_date).order_by('-publication_date'))

        usr=User.get_by_id(uid)
        badges=usr.badges.all()

        return render_to_response(
            'main/user.html',
            #{
            # 'marketing_items':market_items,
            #'user': User.get_by_id(uid),'reports':status},

            {
            'user':usr,
            'badges':badges,
            'reports':status,
            'announces':announces
            },
            context_instance=RequestContext(request)
        )

# def report(request):
#     if request.method == "POST":
#         status = request.POST.get("status", "")
#         #update the database with the status
#         if status:
#             uid = request.session.get('user')
#             user = User.get_by_id(uid)
#             StatusReport(user=user, status=status).save()
#
#         #always return something
#         return index(request)
def report(request):
    if request.method =='POST':
        status=request.POST.get("status", "")
        #update the database with the status
        if status:
            uid=request.session.get('user')
            user=User.get_by_id(uid)
            StatusReport(user=user, status=status).save()
    return index(request)
