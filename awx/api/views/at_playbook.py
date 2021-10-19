# Python
import logging

# Django
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

# AWX
from awx.main.models import (
    ActivityStream,
    Inventory,
    Host,
    Project,
    ExecutionEnvironment,
    JobTemplate,
    WorkflowJobTemplate,
    Organization,
    NotificationTemplate,
    Role,
    User,
    Team,
    InstanceGroup,
    Credential,
    AtPlaybook,
)
from awx.api.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    SubListAPIView,
    SubListCreateAttachDetachAPIView,
    SubListAttachDetachAPIView,
    SubListCreateAPIView,
    ResourceAccessList,
    BaseUsersList,
)

from awx.api.serializers import (
    OrganizationSerializer,
    InventorySerializer,
    UserSerializer,
    TeamSerializer,
    ActivityStreamSerializer,
    RoleSerializer,
    NotificationTemplateSerializer,
    InstanceGroupSerializer,
    ExecutionEnvironmentSerializer,
    ProjectSerializer,
    JobTemplateSerializer,
    WorkflowJobTemplateSerializer,
    CredentialSerializer,
    AtPlaybookSerializer,
)
from awx.api.views.mixin import RelatedJobsPreventDeleteMixin, OrganizationCountsMixin

logger = logging.getLogger('awx.api.views.at_playbook')

# get and post
class AtPlaybookList(ListCreateAPIView):
    
    # always_allow_superuser = False
    model = AtPlaybook
    serializer_class = AtPlaybookSerializer
    always_allow_superuser = False

    def post(self, request, *args, **kwargs):
        logger.debug('post method self: ', self)
        ret = super(AtPlaybookList, self).post(request, *args, **kwargs)
        if ret.status_code == 201:
            job_template = AtPlaybook.objects.get(id=ret.data['id'])
            job_template.admin_role.members.add(request.user)
        return ret

class AtPlaybookDetail(RelatedJobsPreventDeleteMixin, RetrieveUpdateDestroyAPIView):

    model = AtPlaybook
    serializer_class = AtPlaybookSerializer
    always_allow_superuser = False