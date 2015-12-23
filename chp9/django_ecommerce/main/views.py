# Create your views here.
from django.shortcuts import render_to_response
from payments.models import User
from main.models import MarketingItem

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
    market_items=MarketingItem.objects.all()
    if uid is None:
        return render_to_response('main/index.html',
        {'marketing_items': market_items})
    else:
        return render_to_response(
            'main/user.html',
            {'marketing_items':market_items,
            'user': User.get_by_id(uid)}
        )
