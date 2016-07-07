"""Generated client library for cloudbilling version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from googlecloudsdk.third_party.apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudbilling.v1 import cloudbilling_v1_messages as messages


class CloudbillingV1(base_api.BaseApiClient):
  """Generated client library for service cloudbilling version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://cloudbilling.googleapis.com/'

  _PACKAGE = u'cloudbilling'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudbillingV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new cloudbilling handle."""
    url = url or self.BASE_URL
    super(CloudbillingV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.billingAccounts_projects = self.BillingAccountsProjectsService(self)
    self.billingAccounts = self.BillingAccountsService(self)
    self.projects = self.ProjectsService(self)

  class BillingAccountsProjectsService(base_api.BaseApiService):
    """Service class for the billingAccounts_projects resource."""

    _NAME = u'billingAccounts_projects'

    def __init__(self, client):
      super(CloudbillingV1.BillingAccountsProjectsService, self).__init__(client)
      self._method_configs = {
          'List': base_api.ApiMethodInfo(
              flat_path=u'v1/billingAccounts/{billingAccountsId}/projects',
              http_method=u'GET',
              method_id=u'cloudbilling.billingAccounts.projects.list',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[u'pageSize', u'pageToken'],
              relative_path=u'v1/{+name}/projects',
              request_field='',
              request_type_name=u'CloudbillingBillingAccountsProjectsListRequest',
              response_type_name=u'ListProjectBillingInfoResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists the projects associated with a billing account. The current.
authenticated user must be an [owner of the billing
account](https://support.google.com/cloud/answer/4430947).

      Args:
        request: (CloudbillingBillingAccountsProjectsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListProjectBillingInfoResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class BillingAccountsService(base_api.BaseApiService):
    """Service class for the billingAccounts resource."""

    _NAME = u'billingAccounts'

    def __init__(self, client):
      super(CloudbillingV1.BillingAccountsService, self).__init__(client)
      self._method_configs = {
          'Get': base_api.ApiMethodInfo(
              flat_path=u'v1/billingAccounts/{billingAccountsId}',
              http_method=u'GET',
              method_id=u'cloudbilling.billingAccounts.get',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}',
              request_field='',
              request_type_name=u'CloudbillingBillingAccountsGetRequest',
              response_type_name=u'BillingAccount',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'cloudbilling.billingAccounts.list',
              ordered_params=[],
              path_params=[],
              query_params=[u'pageSize', u'pageToken'],
              relative_path=u'v1/billingAccounts',
              request_field='',
              request_type_name=u'CloudbillingBillingAccountsListRequest',
              response_type_name=u'ListBillingAccountsResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Gets information about a billing account. The current authenticated user.
must be an [owner of the billing
account](https://support.google.com/cloud/answer/4430947).

      Args:
        request: (CloudbillingBillingAccountsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BillingAccount) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists the billing accounts that the current authenticated user.
[owns](https://support.google.com/cloud/answer/4430947).

      Args:
        request: (CloudbillingBillingAccountsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListBillingAccountsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(CloudbillingV1.ProjectsService, self).__init__(client)
      self._method_configs = {
          'GetBillingInfo': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/billingInfo',
              http_method=u'GET',
              method_id=u'cloudbilling.projects.getBillingInfo',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}/billingInfo',
              request_field='',
              request_type_name=u'CloudbillingProjectsGetBillingInfoRequest',
              response_type_name=u'ProjectBillingInfo',
              supports_download=False,
          ),
          'UpdateBillingInfo': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/billingInfo',
              http_method=u'PUT',
              method_id=u'cloudbilling.projects.updateBillingInfo',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}/billingInfo',
              request_field=u'projectBillingInfo',
              request_type_name=u'CloudbillingProjectsUpdateBillingInfoRequest',
              response_type_name=u'ProjectBillingInfo',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def GetBillingInfo(self, request, global_params=None):
      """Gets the billing information for a project. The current authenticated user.
must have [permission to view the
project](https://cloud.google.com/docs/permissions-overview#h.bgs0oxofvnoo
).

      Args:
        request: (CloudbillingProjectsGetBillingInfoRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ProjectBillingInfo) The response message.
      """
      config = self.GetMethodConfig('GetBillingInfo')
      return self._RunMethod(
          config, request, global_params=global_params)

    def UpdateBillingInfo(self, request, global_params=None):
      """Sets or updates the billing account associated with a project. You specify.
the new billing account by setting the `billing_account_name` in the
`ProjectBillingInfo` resource to the resource name of a billing account.
Associating a project with an open billing account enables billing on the
project and allows charges for resource usage. If the project already had a
billing account, this method changes the billing account used for resource
usage charges.

*Note:* Incurred charges that have not yet been reported in the transaction
history of the Google Cloud Console may be billed to the new billing
account, even if the charge occurred before the new billing account was
assigned to the project.

The current authenticated user must have ownership privileges for both the
[project](https://cloud.google.com/docs/permissions-overview#h.bgs0oxofvnoo
) and the [billing
account](https://support.google.com/cloud/answer/4430947).

You can disable billing on the project by setting the
`billing_account_name` field to empty. This action disassociates the
current billing account from the project. Any billable activity of your
in-use services will stop, and your application could stop functioning as
expected. Any unbilled charges to date will be billed to the previously
associated account. The current authenticated user must be either an owner
of the project or an owner of the billing account for the project.

Note that associating a project with a *closed* billing account will have
much the same effect as disabling billing on the project: any paid
resources used by the project will be shut down. Thus, unless you wish to
disable billing, you should always call this method with the name of an
*open* billing account.

      Args:
        request: (CloudbillingProjectsUpdateBillingInfoRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ProjectBillingInfo) The response message.
      """
      config = self.GetMethodConfig('UpdateBillingInfo')
      return self._RunMethod(
          config, request, global_params=global_params)
