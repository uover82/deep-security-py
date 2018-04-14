import core
import translation
import json
import urllib

class TenantTemplate(core.CoreObject):
  def __init__(self, manager=None, api_response=None, log_func=None):
    core.CoreObject.__init__(self)
    self.manager = manager
    self.log = self.manager.log if self.manager else None
    if api_response: self._set_properties(api_response, log_func)

  def add(self, tenant_id=None):
    """
    Add a Tenant Template
    """

    rest_call = self.manager._get_request_format(api=self.manager.API_TYPE_REST)

    rest_call['call'] = 'tenanttemplate'
    rest_call['data'] = {
        'createTenantTemplateRequest': {
            'tenantId': tenant_id,
            'sessionId': self.manager._sessions[self.manager.API_TYPE_REST]
        }
    }

    response = self.manager._request(rest_call, auth_required=False)

    return response

  def get(self):
    """
    Describe a Tenant Template
    """

    rest_call = self.manager._get_request_format(api=self.manager.API_TYPE_REST)

    rest_call['query'] = {}
    rest_call['query']['sID'] = self.manager._sessions[self.manager.API_TYPE_REST]

    rest_call['call'] = 'tenanttemplate'

    response = self.manager._request(rest_call, auth_required=False)

    return response
