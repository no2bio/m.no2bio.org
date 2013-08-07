CSV_FILENAME = u'menu.csv'
API_URL = u'http://no2bio.org/api'
import csv,json,urllib2,logging
logging.basicConfig(level=logging.DEBUG) # maybe do syslog, mail, or something fancier later on
logger=logging.getLogger('make-m')

def _make_item(keys,row):
    item = {}
    for k,v in zip(keys,row):
        item[k]=v
    return item

def _item_by_id(menu,item_id):
    for item in menu['items']:
        if item['id'] == item_id:
            return item
        if item.get('items'):
            found = _item_by_id(item,item_id)
            if found:
                return found
    return None

def _load_category(slug):
    logger.info( u"getting category: {0}".format(slug))
    return json.load(urllib2.urlopen(u'{0}/get_category_posts?slug={1}'.format(API_URL,slug)))

def _hilite_menu(menu,path):
    for m in menu.get('items',[]):
        _hilite_menu_aux(m,path)
def _hilite_menu_aux(menu,path):
    if path and menu.get('id')==path[0]:
        menu['active'] = True
        for m in menu.get('items',[]):
            _hilite_menu_aux(m,path[1:])
    else:
        menu['active'] = False
        for m in menu.get('items',[]):
            _hilite_menu_aux(m,[])

def make_menu(csv_filename=CSV_FILENAME):
    menu = {'items':[],'path':[]}
    categories = {}
    table = csv.reader(file(CSV_FILENAME))
    keys = table.next()
    for r in table:
        item = _make_item(keys,r)
        parent = item['parent'] and _item_by_id(menu,item['parent']) or menu
        item['path'] = parent['path']+[item['id']]
        parent['items'].append(item)
        if item['type']=='submenu':
            item['items'] = []
        if item['type']=='category':
            cat = _load_category(item['id'])
            first = filter(lambda x: x['slug']==item['arg'],cat['posts'])
            rest = filter(lambda x: x['slug']!=item['arg'],cat['posts'])
            posts = first+sorted(rest,key=lambda x:x['title'])
            item['items'] = [{
              'id':p['slug'],
              'path':item['path']+[p['slug']],
              'name':p['title'],
              'type':'post',
              'parent':item['id'],
              'url':u'posts/{0}.html'.format(p['slug'])
            } for p in posts]
            categories[item['id']] = posts
        elif item['type'] in ['homepage','iframe']:
            item['url']=item['id']+'.html'
    return menu,categories

if __name__=='__main__':
    menu,categories = make_menu()
    _hilite_menu(menu,_item_by_id(menu,'karine-nahon')['path'])
    print json.dumps(menu,indent=1)
    #print json.dumps(categories,indent=1)


