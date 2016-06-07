#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import jinja2
import webapp2
import json as json2
from time import strftime
from google.appengine.ext import db



template_dir = os.path.join(os.path.dirname(__file__),'Template')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                              autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)
def database():

        data = Postskate(titlemax = "Skateboard",
                      titleminu = "street skate", 
                      titlemind = "sla Skate",
                      textu = "Everyone sees what you appear, but few see what you really are", 
                      textd = "A friend comes early, others when they have time",
                      imageu= "imagen/skate/girl.jpg",
                      imaged = "imagen/skate/ho.jpg",
                      imaget = "imagen/skate/large.jpg")
        data.put()

        data1 = Postskate(titlemax = "Hello",
                     titleminu = "street code", 
                     titlemind = "code debelop",
                     textu = "A friend comes early, others when they have time", 
                     textd = "When you lose, do not look at what you lost, but what's left to win ...",
                     imageu = "imagen/skate/maxresdefault.jpg",
                     imaged = "imagen/skate/nyjah.jpg",
                     imaget = "imagen/skate/free.jpg")
        data1.put()

        data2 = Postskate(titlemax = "hardcode",
                     titleminu = "title nice", 
                     titlemind = "very crazy",
                     textu = "Living is the only thing worth dying", 
                     textd = "If you can dream it, you can do it.",
                     imageu = "imagen/skate/oneilll.jpg",
                     imaged = "imagen/skate/redbull.jpg",
                     imaget = "imagen/skate/skatecc.jpg")
        data2.put()

        data3 = Postskate(titlemax = "fullcode",
                     titleminu = "final title", 
                     titlemind = "welcome",
                     textu = "Never, never, never give up", 
                     textd = "Only I can change my life. No one can do it for me.",
                     imageu = "imagen/skate/skate-street1.jpg",
                     imaged = "imagen/skate/trucos.jpg",
                     imaget = "imagen/skate/zapatillas-skate.jpg")
        data3.put()

    
class MainHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        return render_str(template, **params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
    def get(self):
               
        self.render('welcome.html')
    # def post(self):
        
        
        # data = Postskate(titlemax = "Skate",
        #              titlemin = "street", 
        #              text = "Watch Romeo Beckham in This Crazy-Adorable Burberry Video", 
        #              image = "imagen/skate/zapatillas-skate.jpg")
        # data.put()

    def enviar_json(self, datos):
        # self.response.headers['content-type'] = 'aplication/json; charset=UFT-8'
        post= json2.dumps(datos)
        self.response.write(post)


class Postskate(db.Model):
    titlemax = db.StringProperty(required = True)
    titleminu = db.StringProperty(required = True)
    titlemind = db.StringProperty(required = True)
    textu = db.StringProperty(required = True)
    textd = db.StringProperty(required = True)
    imageu = db.TextProperty(required = True)
    imaged = db.TextProperty(required = True)
    imaget = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class Casualpage(MainHandler):
    def get(self):
        self.render('casualclosetpage.html')
        pass
    

class Skatepage(MainHandler):
    def get(self):
        
        self.render('skateboardpage.html')
    # def post(self):
        
    # def as_dict(self):
        
    #     d ={'titlemax':self.titlemax,
    #        'titlemin':self.titlemin,
    #        'text':self.text,
    #        'image':self.image
           

    #     }
class json(MainHandler):
    def get(self):
        database()
        conten = []
        posts = db.GqlQuery('SELECT * FROM Postskate ORDER BY created DESC LIMIT 4')

        if posts:
            # self.write(posts.get())
            for p in posts:
                data = {'titlemax':p.titlemax,'titleminu':p.titleminu,'titlemind':p.titlemind,
                        'textu':p.textu,'textd':p.textd,'imageu':p.imageu,'imaged':p.imaged,
                        'imaget':p.imaget, 'created':p.created.strftime('%b %d,%Y %I:%M:%S')}

                # self.write(data)
                conten.append(data)      
            # self.write(len(conten))
            return self.enviar_json(conten)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/skateboardpage', Skatepage),
    ('/casualclosetpage',Casualpage),
    ('/skateboardpage/.json', json)
    # ('/ajax', AjaxHandler)
], debug=True)
