import core
import translation
import json
import urllib

class Tenants(core.CoreDict):
  def __init__(self, manager=None):
    core.CoreDict.__init__(self)
    self.manager = manager
    self.log = self.manager.log if self.manager else None

  def get(self):
    """
    Get all of the Tenants from Deep Security
    """

    rest_call = self.manager._get_request_format(api=self.manager.API_TYPE_REST)

    rest_call['call'] = 'tenants'
    rest_call['query'] = {}
    rest_call['query']['sID'] = self.manager._sessions[self.manager.API_TYPE_REST]

    response = self.manager._request(rest_call, auth_required=False)

    return response

class Tenant(core.CoreObject):
  def __init__(self, manager=None, api_response=None, log_func=None):
    core.CoreObject.__init__(self)
    self.manager = manager
    self.log = self.manager.log if self.manager else None
    if api_response: self._set_properties(api_response, log_func)

  def add(self, admin_acct=None, admin_pw=None, admin_eml=None, name=None):
    """
    Add a Tenant
    """

    rest_call = self.manager._get_request_format(api=self.manager.API_TYPE_REST)

    rest_call['call'] = 'tenants'
    rest_call['data'] = {
      'createTenantRequest': {
        'createOptions': {
          'adminAccount': admin_acct,
          'adminPassword': admin_pw,
          'adminEmail': admin_eml,
          'activationCodes': [ 'AM' ]
        },
        'tenantElement': {
          #'tenantID': 11,
          'name': name,
          'language': 'en',
          'country': 'US',
          'timeZone': 'US/Pacific',
          'modulesVisible': ['AM']
        },
        'sessionId': self.manager._sessions[self.manager.API_TYPE_REST]
      }
    }

    response = self.manager._request(rest_call, auth_required=False)

    return response
  
  def get(self, tenant_id=None, tenant_name=None, tenant_state=None, max_items=None, tenant_idop=None):
    """
    Describe one/ more Tenants
    """

    rest_call = self.manager._get_request_format(api=self.manager.API_TYPE_REST)

    rest_call['query'] = {}
    rest_call['query']['sID'] = self.manager._sessions[self.manager.API_TYPE_REST]

    if tenant_state:
      rest_call['call'] = 'tenants/state/'+tenant_state
      if max_items:
        rest_call['query']['maxItems'] = max_items
      if tenant_id:
        rest_call['query']['tenantID'] = str(tenant_id)
      if tenant_idop:
        rest_call['query']['tenantIDOp'] = tenant_idop
    elif tenant_id:
      rest_call['call'] = 'tenants/id/'+str(tenant_id)
    elif tenant_name:
      rest_call['call'] = 'tenants/name/'+urllib.quote(tenant_name)
    else:
      rest_call['call'] = 'tenants'

    response = self.manager._request(rest_call, auth_required=False)

    return response
  
  def update(self, tenant_name=None, modules_visible=None):
    """
    Update a Tenant by name
    """

    rest_call = self.manager._get_request_format(api=self.manager.API_TYPE_REST)

    rest_call['query'] = {}
    rest_call['query']['sID'] = self.manager._sessions[self.manager.API_TYPE_REST]
    rest_call['call'] = 'tenants/name/'+urllib.quote(tenant_name)

    rest_call['data'] = {
      'updateTenantRequest': {
        'tenantElement': {
          'modulesVisible': modules_visible
        },
        'sessionId': self.manager._sessions[self.manager.API_TYPE_REST]
      }
    }

    response = self.manager._request(rest_call, auth_required=False)

    return response
