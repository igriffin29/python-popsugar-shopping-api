import urllib
import urllib2
import simplejson

BASE_URL = 'http://api.shopstyle.com/action/%s/'

class ShopStyle(object):
    api_version = 'v1'
    def __init__(self, api_key, format='json'):
        self.api_key = api_key
        self.format = format
        self.params = {'format':format, 'pid':self.api_key}
        self.opener = urllib2.build_opener()
    
    def request(self, method):
        url = BASE_URL % method
        req = urllib2.Request(url)
        req.data = urllib.urlencode(self.params)
        opener = self.opener.open(req)
        return simplejson.load(opener)        
    
    def return_json(self, request):
        self.params = {'format':format, 'pid':self.api_key}
    
    def search(self, fts=None, cat=None, 
                    fl=None, pdd=None, prodid=None, min=None, count=None):
        params = {}
        if fts:
            self.params.update({'fts':fts})
        if cat:
            self.params.update({'cat':cat})
        if fl:
            self.params.update({'fl':fl})
        if pdd:
            self.params.update({'pdd':pdd})
        if prodid:
            self.params.update({'prodid':prodid})
        if min:
            self.params.update({'min':min})
        if count:
            self.params.update({'count':count})
        return self.return_json(request=
                    self.request(method='apiSearch')
                    )
        
    def get_category_histogram(self, fts=None, cat=None, 
                    fl=None, pdd=None, prodid=None):
        if fts:
            self.params.update({'fts':fts})
        if cat:
            self.params.update({'cat':cat})
        if fl:
            self.params.update({'fl':fl})
        if pdd:
            self.params.update({'pdd':pdd})
        if prodid:
            self.params.update({'prodid':prodid})
        return self.return_json(request=
            self.request(method='apiGetCategoryHistogram')
            )

    def get_filter_histogram(self, fts=None, cat=None, 
                    fl=None, pdd=None, prodid=None):
        if fts:
            self.params.update({'fts':fts})
        if cat:
            self.params.update({'cat':cat})
        if fl:
            self.params.update({'fl':fl})
        if pdd:
            self.params.update({'pdd':pdd})
        if prodid:
            self.params.update({'prodid':prodid})        
        return self.return_json(request=
            self.request(method='apiGetFilterHistogram')
            )

    def get_brands(self):
        return self.request(method='apiGetBrands')

    def get_look(self, look):
        self.params.update({'look':look})
        return self.request(method='apiGetLook')

    def get_retailers(self):
        return self.request(method='apiGetRetailers')
        
    def get_stylebook(self, handle):
        self.params.update({'handle':handle})
        return self.request(method='apiGetStylebook')

    def get_looks(self, min=None, count=None, new=False, 
                    top=False, celeb=False, featured=False):
        if min:
            self.params.update({'min':min})
        if count:
            self.params.update({'count':count})
        if new:
            self.params.update({'type':'New'})
        if top:
            self.params.update({'type':'TopRated'})
        if celeb:
            self.params.update({'type':'Celebrities'})
        if featured:
            self.params.update({'type':'Featured'})            
        return self.request(method='apiGetLooks')

    def visit_retailer(self, id):
        self.params.update({'id':id})
        url = BASE_URL % 'apiVisitRetailer'
        req = urllib2.Request(url)
        req.data = urllib.urlencode(self.params)
        opener = self.opener.open(req)
        return opener.read()

    def get_trends(self, cat):
        self.params.update({'cat':cat})
        return self.request(method='apiGetTrends')
        
        
        