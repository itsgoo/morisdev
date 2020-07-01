

def index(self, request):
    hi_all = 'hi all'
    ctx = {
        'hi_all': hi_all,
    }
    return ctx