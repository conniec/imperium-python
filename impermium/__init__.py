"""
impermium
~~~~~~~~~

:copyright: (c) 2011 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.

>>> from impermium import ImpermiumAPI
>>> impermium = ImpermiumAPI(api_key=api_key)

>>> response = impermium.checkComment(event_id, {
>>>     'uid_ref': '12341234',
>>>     'resource_url': 'http://example.com',
>>>     'content': 'Hello world!',
>>> })

>>> if response['spam']['label'] == 'spam':
>>>     print "Uh oh, it's spam!"

"""
try:
    __version__ = __import__('pkg_resources') \
        .get_distribution('impermium').version
except:
    __version__ = 'unknown'

import httplib
import simplejson

class APIError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return '%s: %s' % (self.code, self.message)

class ImpermiumAPI(object):
    HOST = 'api.impermium.com'
    
    def __init__(self, api_key, version='2.0'):
        self.api_key = api_key
        self.version = str(version)
    
    def request(self, http_method, object_type, event_id=None, params={}):
        
        path = '/%(object_type)s/%(version)s/%(api_key)s' % dict(
            object_type=object_type,
            version=self.version,
            api_key=self.api_key,
        )
        
        if event_id:
            path += '/%s' % (event_id,)
        conn = httplib.HTTPConnection(self.HOST)
        
        conn.request(http_method, path, simplejson.dumps(params), {
            'User-Agent': 'impermium-python/%s' % __version__,
            'Content-Type': 'application/json',
        })

        response = conn.getresponse()

        data = response.read()

        if data.startswith('{'):
            data = simplejson.loads(data)

        if response.status != 200:
            raise APIError(response.status, data)
        
        return data
    
    # Endpoints which check content
    checkAccount = lambda s, *a, **k: s.request('POST', 'account', *a, **k)
    checkAccountAttempt = lambda s, *a, **k: s.request('POST', 'account/attempt', *a, **k)
    checkAccountLogin = lambda s, *a, **k: s.request('POST', 'account/login', *a, **k)
    
    checkProfile = lambda s, *a, **k: s.request('POST', 'profile', *a, **k)
    #checkInvite = lambda s, *a, **k: s.request('POST', 'connection', 'invite', *a, **k)
    #checkInviteResponse = lambda s, *a, **k: s.request('POST', 'connection', 'invite_response', *a, **k)
    checkBlogEntry = lambda s, *a, **k: s.request('POST', 'blog_post', *a, **k)
    #checkChatMessage = lambda s, *a, **k: s.request('POST', 'content', 'chat_message', *a, **k)
    #checkChatroomMessage = lambda s, *a, **k: s.request('POST', 'content', 'chatroom_message', *a, **k)
    checkComment = lambda s, *a, **k: s.request('POST', 'comment', *a, **k)
    #checkForumMessage = lambda s, *a, **k: s.request('POST', 'content', 'forum_message', *a, **k)
    #checkGeneric = lambda s, *a, **k: s.request('POST', 'content', 'generic', *a, **k)
    #checkMessage = lambda s, *a, **k: s.request('POST', 'content', 'message', *a, **k)
    
    # Endpoints which train with content
    #trainAnalyst = lambda s, *a, **k: s.request('POST', 'feedback', 'analyst', *a, **k)
    #trainEnduser = lambda s, *a, **k: s.request('POST', 'feedback', 'enduser', *a, **k)
    checkBookmark = lambda s, *a, **k: s.request('POST', 'bookmark', *a, **k)
    bookmarkLike = lambda s, *a, **k: s.request('POST', 'bookmark/like', *a, **k)

    checkListing = lambda s, *a, **k: s.request('POST', 'listing', *a, **k)

    # API 3.1 endpoints
    def trainAnalyst(self, object_type, analyst_type, *args, **kwargs):
        assert self.version == '3.1'
        return self.request('POST', '%s/%s' % (object_type, analyst_type), *args, **kwargs)



    # def trainAnalystProfile(self, *args, **kwargs):
    #     assert self.version == '3.1'
    #     return self.request('POST', 'profile', 'analyst_feedback', *args, **kwargs)
    
    # def trainEnduserProfile(self, *args, **kwargs):
    #     assert self.version == '3.1'
    #     return self.request('POST', 'profile', 'user_feedback', *args, **kwargs)

    # def trainAnalystAccount(self, *args, **kwargs):
    #     assert self.version == '3.1'
    #     return self.request('POST', 'account', 'analyst_feedback', *args, **kwargs)
    
    # def trainEnduserAccount(self, *args, **kwargs):
    #     assert self.version == '3.1'
    #     return self.request('POST', 'account', 'user_feedback', *args, **kwargs)

    # def trainAnalystListing(self, *args, **kwargs):
    #     assert self.version == '3.1'
    #     return self.request('POST', 'listing', 'analyst_feedback', *args, **kwargs)
    
    # def trainEnduserListing(self, *args, **kwargs):
    #     assert self.version == '3.1'
    #     return self.request('POST', 'listing', 'user_feedback', *args, **kwargs)

    # def trainAnalystBookmark(self, *args, **kwargs):
    #     assert self.version == '3.1'
    #     return self.request('POST', 'bookmark', 'analyst_feedback', *args, **kwargs)
    
    # def trainEnduserBookmark(self, *args, **kwargs):
    #     assert self.version == '3.1'
    #     return self.request('POST', 'bookmark', 'user_feedback', *args, **kwargs)

    # def trainAnalystComment(self, *args, **kwargs):
    #     assert self.version == '3.1'
    #     return self.request('POST', 'comment', 'analyst_feedback', *args, **kwargs)

    # def trainEnduserComment(self, *args, **kwargs):
    #     assert self.version == '3.1'
    #     return self.request('POST', 'comment', 'user_feedback', *args, **kwargs)

    # def trainAnalystBlogPost(self, *args, **kwargs):
    #     assert self.version == '3.1'
    #     return self.request('POST', 'blog_post', 'analyst_feedback', *args, **kwargs)
    
    # def trainEnduserBlogPost(self, *args, **kwargs):
    #     assert self.version == '3.1'
    #     return self.request('POST', 'blog_post', 'user_feedback', *args, **kwargs)

    # API 3.0 endpoints
    def trainAnalystComment(self, *args, **kwargs):
        assert self.version == '3.0'
        return self.request('POST', 'content/comment/analystfeedback', *args, **kwargs)

    def trainEnduserComment(self, *args, **kwargs):
        assert self.version == '3.0'
        return self.request('POST', 'content/comment/userfeedback', *args, **kwargs)
