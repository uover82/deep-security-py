import unittest
import deepsecurity, json

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        global mgr
        mgr = deepsecurity.dsm.Manager(hostname="dsm.cleardata.com", port="443", username="john.harrison@cleardata.com", password="QFD!C*#bHEr5", tenantname="primary", ignore_ssl_validation=True)
        mgr.sign_in()

    '''
    def test_add_tenant(self):
        global mgr
        response = mgr.tenant.add(admin_acct='testadmin', admin_pw='Ou812345!', admin_eml='test@mytest.com', name='tenanttest22')
        self.assertEqual(response['status'], 200)
    '''

    def test_get_tenant(self):
        global mgr, response
        response = mgr.tenant.get(tenant_id=11)
        self.assertEqual(response['status'], 200)

    def test_add_tenant_template(self):
        global mgr, response
        response = mgr.tenanttemplate.add(tenant_id=11)
        self.assertEqual(response['status'], 200)

    def test_get_tenant_template(self):
        global mgr, response
        response = mgr.tenanttemplate.get()
        self.assertEqual(response['status'], 200)

    def tearDown(self):
        global mgr
        mgr.sign_out()

if __name__ == '__main__':
    unittest.main()
