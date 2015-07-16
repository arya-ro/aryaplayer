import util, urllib2

def playVideo(params):
    response = urllib2.urlopen(params['video'])
    if response and response.getcode() == 200:
        content = response.read()
        videoLink = util.extract(content, 'flashvars.File = "', '"')
        util.playMedia(params['title'], params['image'], videoLink, 'Video')
    else:
        util.showError(ADDON_ID, 'Could not open URL %s to get video information' % (params['video']))
    
def buildMenu():
    url = WEB_PAGE_BASE + 'index.html'
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        videos = util.extractAll(content, '<st>', '<-st>')
        for video in videos:
            params = {'play':1}
            params['video'] = util.extract(video, '<video>', '<-video>')
            params['image'] = util.extract(video, '<img>', '<-img>')
            params['title'] = util.extract(video, '<text>', '<-text>')
            util.addMenuItem(params['title'], params['video'], 'DefaultVideo.png', params['image'], False)
        util.endListing()
    else:
        util.showError(ADDON_ID, 'Could not open URL %s to create menu' % (url))

WEB_PAGE_BASE = 'http://arya.ro/xbmc/'
ADDON_ID = 'plugin.video.aryaro'

parameters = util.parseParameters()
if 'play' in parameters:
    playVideo(parameters)
else:
    buildMenu()
