import falcon
import json
from astropy.coordinates import SkyCoord
from astropy import units as u
import numpy as np
from astropy.coordinates import EarthLocation
from astropy.time import Time
from astropy.coordinates import AltAz


nijmegen = EarthLocation(lat=51.841680, lon=5.846410, height=0)
observing_time = Time.now()
aa = AltAz(location=nijmegen, obstime=observing_time)
print(aa)

def sink(req, resp):
  print(req)
  print(req.params)

def build_response_body(req, value=None):
  resp_dict = {    
    "ClientTransactionID": req.params["ClientTransactionID"],
    "ServerTransactionID": 0,
    "ErrorNumber": 0,
    "ErrorMessage": ""
  }
  if value is not None:
    resp_dict["Value"] = value
  return json.dumps(resp_dict)

class TelescopeConnectedResource(object):
  def on_put(self, req, resp, device_number):
    print(req.params)
    print(device_number)
    resp.body = build_response_body(req)

class TelescopeNameResource(object):
  def on_get(self, req, resp, device_number):
    print(req.params)
    resp.body = build_response_body(req, "telescope")

class TelescopeCanPulseGuideResource(object):
  def on_get(self, req, resp, device_number):
    resp.body = build_response_body(req, True)

class TelescopeCanSlewResource(object):
  def on_get(self, req, resp, device_number):
    print(req.params)
    resp.body = build_response_body(req, True)

class TelescopeCanSlewAsyncResource(object):
  def on_get(self, req, resp, device_number):
    print(req.params)
    resp.body = build_response_body(req, True)

class TelescopeSideOfPierResource(object):
  def on_get(self, req, resp, device_number):
    print(req.params)
    resp.body = build_response_body(req, 0)

class TelescopeDeclinationResource(object):
  def on_get(self, req, resp, device_number):
    print(req.params)
    resp.body = build_response_body(req, 45)
class TelescopeRAResource(object):
  def on_get(self, req, resp, device_number):
    print(req.params)
    resp.body = build_response_body(req, 0)



app = falcon.API()
app.req_options.auto_parse_form_urlencoded = True
app.add_sink(sink, "/")

app.add_route('/api/v1/telescope/{device_number}/connected', TelescopeConnectedResource())
app.add_route('/api/v1/telescope/{device_number}/name', TelescopeNameResource())

app.add_route('/api/v1/telescope/{device_number}/canpulseguide', TelescopeCanPulseGuideResource())

app.add_route('/api/v1/telescope/{device_number}/canslew', TelescopeCanSlewResource())
app.add_route('/api/v1/telescope/{device_number}/canslewasync', TelescopeCanSlewAsyncResource())
app.add_route('/api/v1/telescope/{device_number}/sideofpier', TelescopeSideOfPierResource())
app.add_route('/api/v1/telescope/{device_number}/declination', TelescopeDeclinationResource())
app.add_route('/api/v1/telescope/{device_number}/rightascension', TelescopeRAResource())



# PHD2:
# <Request: GET 'http://localhost:5000/api/v1/telescope/0/canpulseguide?ClientTransactionID=59&ClientID=20083'>
# <Request: GET 'http://localhost:5000/api/v1/telescope/0/canslew?ClientTransactionID=60&ClientID=20083'>
# <Request: GET 'http://localhost:5000/api/v1/telescope/0/canslewasync?ClientTransactionID=61&ClientID=20083'>
# <Request: GET 'http://localhost:5000/api/v1/telescope/0/declination?ClientTransactionID=62&ClientID=20083'>
# <Request: GET 'http://localhost:5000/api/v1/telescope/0/sideofpier?ClientTransactionID=63&ClientID=20083'>