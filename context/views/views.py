from rest_framework import permissions, viewsets

from context.models.access_prereq_types import AccessPrereqTypes
from context.models.check_status_types import CheckStatusTypes
from context.models.composite_hash_types import CompositeHashTypes
from context.models.contributor_types import ContributorTypes
from context.models.dataset_consent_types import DatasetConsentTypes
from context.models.dataset_deidentification_levels import DatasetDeidentificationLevels
from context.models.dataset_recordkey_types import DatasetRecordkeyTypes
from context.models.date_types import DateTypes
from context.models.description_types import DescriptionTypes
from context.models.doi_status_types import DoiStatusTypes
from context.models.dtp_status_types import DtpStatusTypes
from context.models.dup_status_types import DupStatusTypes
from context.models.gender_eligibility_types import GenderEligibilityTypes
from context.models.geog_entity_types import GeogEntityTypes
from context.models.identifier_types import IdentifierTypes
from context.models.language_usage_types import LanguageUsageTypes
from context.models.legal_status_types import LegalStatusTypes
from context.models.link_types import LinkTypes
from context.models.object_access_types import ObjectAccessTypes
from context.models.object_classes import ObjectClasses
from context.models.object_filter_types import ObjectFilterTypes
from context.models.object_instance_types import ObjectInstanceTypes
from context.models.object_relationship_types import ObjectRelationshipTypes
from context.models.object_types import ObjectTypes
from context.models.org_attribute_datatypes import OrgAttributeDatatypes
from context.models.org_attribute_types import OrgAttributeTypes
from context.models.org_classes import OrgClasses
from context.models.org_link_types import OrgLinkTypes
from context.models.org_names_qualifier_types import OrgNameQualifierTypes
from context.models.org_relationship_types import OrgRelationshipTypes
from context.models.org_types import OrgTypes
from context.models.prereq_types import PrereqTypes
from context.models.repo_access_types import RepoAccessTypes
from context.models.resource_types import ResourceTypes
from context.models.rms_user_types import RmsUserTypes
from context.models.role_classes import RoleClasses
from context.models.role_types import RoleTypes
from context.models.size_units import SizeUnits
from context.models.study_feature_categories import StudyFeatureCategories
from context.models.study_feature_types import StudyFeatureTypes
from context.models.study_relationship_types import StudyRelationshipTypes
from context.models.study_statuses import StudyStatuses
from context.models.study_types import StudyTypes
from context.models.time_units import TimeUnits
from context.models.title_types import TitleTypes
from context.models.topic_types import TopicTypes
from context.models.topic_vocabularies import TopicVocabularies
from context.models.trial_registries import TrialRegistries
from context.models.user_types import UserTypes
from context.serializers.access_prereq_types_dto import AccessPrereqTypesSerializer
from context.serializers.check_status_types_dto import CheckStatusTypesSerializer
from context.serializers.composite_hash_types_dto import CompositeHashTypesSerializer
from context.serializers.contributor_types_dto import ContributorTypesSerializer
from context.serializers.dataset_consent_types_dto import DatasetConsentTypesSerializer
from context.serializers.dataset_deidentification_levels_dto import DatasetDeidentificationLevelsSerializer
from context.serializers.dataset_recordkey_types_dto import DatasetRecordkeyTypesSerializer
from context.serializers.date_types_dto import DateTypesSerializer
from context.serializers.description_types_dto import DescriptionTypesSerializer
from context.serializers.doi_status_types_dto import DoiStatusTypesSerializer
from context.serializers.dtp_status_types_dto import DtpStatusTypesSerializer
from context.serializers.dup_status_types_dto import DupStatusTypesSerializer
from context.serializers.gender_eligibility_types_dto import GenderEligibilityTypesSerializer
from context.serializers.geog_entity_types_dto import GeogEntityTypesSerializer
from context.serializers.identifier_types_dto import IdentifierTypesSerializer
from context.serializers.language_usage_types_dto import LanguageUsageTypesSerializer
from context.serializers.legal_status_types_dto import LegalStatusTypesSerializer
from context.serializers.link_types_dto import LinkTypesSerializer
from context.serializers.object_access_types_dto import ObjectAccessTypesSerializer
from context.serializers.object_classes_dto import ObjectClassesSerializer
from context.serializers.object_filter_types_dto import ObjectFilterTypesSerializer
from context.serializers.object_instance_types_dto import ObjectInstanceTypesSerializer
from context.serializers.object_relationship_types_dto import ObjectRelationshipTypesSerializer
from context.serializers.object_types_dto import ObjectTypesSerializer
from context.serializers.org_attribute_datatypes_dto import OrgAttributeDatatypesSerializer
from context.serializers.org_attribute_types_dto import OrgAttributeTypesSerializer
from context.serializers.org_classes_dto import OrgClassesSerializer
from context.serializers.org_link_types_dto import OrgLinkTypesSerializer
from context.serializers.org_names_qualifier_types_dto import OrgNameQualifierTypesSerializer
from context.serializers.org_relationship_types_dto import OrgRelationshipTypesSerializer
from context.serializers.org_types_dto import OrgTypesSerializer
from context.serializers.prereq_types_dto import PrereqTypesSerializer
from context.serializers.repo_access_types_dto import RepoAccessTypesSerializer
from context.serializers.resource_types_dto import ResourceTypesSerializer
from context.serializers.rms_user_types_dto import RmsUserTypesSerializer
from context.serializers.role_classes_dto import RoleClassesSerializer
from context.serializers.role_types_dto import RoleTypesSerializer
from context.serializers.size_units_dto import SizeUnitsSerializer
from context.serializers.study_feature_categories_dto import StudyFeatureCategoriesSerializer
from context.serializers.study_feature_types_dto import StudyFeatureTypesSerializer
from context.serializers.study_relationship_types_dto import StudyRelationshipTypesSerializer
from context.serializers.study_statuses_dto import StudyStatusesSerializer
from context.serializers.study_types_dto import StudyTypesSerializer
from context.serializers.time_units_dto import TimeUnitsSerializer
from context.serializers.title_types_dto import TitleTypesSerializer
from context.serializers.topic_types_dto import TopicTypesSerializer
from context.serializers.topic_vocabularies_dto import TopicVocabulariesSerializer
from context.serializers.trial_registries_dto import TrialRegistriesSerializer
from context.serializers.user_types_dto import UserTypesSerializer


# Create your views here.
class AccessPrereqTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = AccessPrereqTypes.objects.all()
    serializer_class = AccessPrereqTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CheckStatusTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = CheckStatusTypes.objects.all()
    serializer_class = CheckStatusTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CompositeHashTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = CompositeHashTypes.objects.all()
    serializer_class = CompositeHashTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ContributorTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = ContributorTypes.objects.all()
    serializer_class = ContributorTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DatasetConsentTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = DatasetConsentTypes.objects.all()
    serializer_class = DatasetConsentTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DatasetDeidentificationLevelsList(viewsets.ReadOnlyModelViewSet):
    queryset = DatasetDeidentificationLevels.objects.all()
    serializer_class = DatasetDeidentificationLevelsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DatasetRecordkeyTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = DatasetRecordkeyTypes.objects.all()
    serializer_class = DatasetRecordkeyTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DateTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = DateTypes.objects.all()
    serializer_class = DateTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DescriptionTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = DescriptionTypes.objects.all()
    serializer_class = DescriptionTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DoiStatusTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = DoiStatusTypes.objects.all()
    serializer_class = DoiStatusTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DtpStatusTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = DtpStatusTypes.objects.all()
    serializer_class = DtpStatusTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DupStatusTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = DupStatusTypes.objects.all()
    serializer_class = DupStatusTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GenderEligibilityTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = GenderEligibilityTypes.objects.all()
    serializer_class = GenderEligibilityTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GeogEntityTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = GeogEntityTypes.objects.all()
    serializer_class = GeogEntityTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IdentifierTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = IdentifierTypes.objects.all()
    serializer_class = IdentifierTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LanguageUsageTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = LanguageUsageTypes.objects.all()
    serializer_class = LanguageUsageTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LegalStatusTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = LegalStatusTypes.objects.all()
    serializer_class = LegalStatusTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LinkTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = LinkTypes.objects.all()
    serializer_class = LinkTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectAccessTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = ObjectAccessTypes.objects.all()
    serializer_class = ObjectAccessTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectClassesList(viewsets.ReadOnlyModelViewSet):
    queryset = ObjectClasses.objects.all()
    serializer_class = ObjectClassesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectFilterTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = ObjectFilterTypes.objects.all()
    serializer_class = ObjectFilterTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectInstanceTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = ObjectInstanceTypes.objects.all()
    serializer_class = ObjectInstanceTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectRelationshipTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = ObjectRelationshipTypes.objects.all()
    serializer_class = ObjectRelationshipTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = ObjectTypes.objects.all()
    serializer_class = ObjectTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgAttributeDatatypesList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgAttributeDatatypes.objects.all()
    serializer_class = OrgAttributeDatatypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgAttributeTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgAttributeTypes.objects.all()
    serializer_class = OrgAttributeTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgClassesList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgClasses.objects.all()
    serializer_class = OrgClassesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgLinkTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgLinkTypes.objects.all()
    serializer_class = OrgLinkTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgNameQualifierTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgNameQualifierTypes.objects.all()
    serializer_class = OrgNameQualifierTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgRelationshipTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgRelationshipTypes.objects.all()
    serializer_class = OrgRelationshipTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgTypes.objects.all()
    serializer_class = OrgTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PrereqTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = PrereqTypes.objects.all()
    serializer_class = PrereqTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RepoAccessTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = RepoAccessTypes.objects.all()
    serializer_class = RepoAccessTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResourceTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = ResourceTypes.objects.all()
    serializer_class = ResourceTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RmsUserTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = RmsUserTypes.objects.all()
    serializer_class = RmsUserTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RoleClassesList(viewsets.ReadOnlyModelViewSet):
    queryset = RoleClasses.objects.all()
    serializer_class = RoleClassesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RoleTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = RoleTypes.objects.all()
    serializer_class = RoleTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SizeUnitsList(viewsets.ReadOnlyModelViewSet):
    queryset = SizeUnits.objects.all()
    serializer_class = SizeUnitsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudyFeatureCategoriesList(viewsets.ReadOnlyModelViewSet):
    queryset = StudyFeatureCategories.objects.all()
    serializer_class = StudyFeatureCategoriesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudyFeatureTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = StudyFeatureTypes.objects.all()
    serializer_class = StudyFeatureTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudyRelationshipTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = StudyRelationshipTypes.objects.all()
    serializer_class = StudyRelationshipTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudyStatusesList(viewsets.ReadOnlyModelViewSet):
    queryset = StudyStatuses.objects.all()
    serializer_class = StudyStatusesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudyTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = StudyTypes.objects.all()
    serializer_class = StudyTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TimeUnitsList(viewsets.ReadOnlyModelViewSet):
    queryset = TimeUnits.objects.all()
    serializer_class = TimeUnitsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TitleTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = TitleTypes.objects.all()
    serializer_class = TitleTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TopicTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = TopicTypes.objects.all()
    serializer_class = TopicTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TopicVocabulariesList(viewsets.ReadOnlyModelViewSet):
    queryset = TopicVocabularies.objects.all()
    serializer_class = TopicVocabulariesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TrialRegistriesList(viewsets.ReadOnlyModelViewSet):
    queryset = TrialRegistries.objects.all()
    serializer_class = TrialRegistriesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserTypesList(viewsets.ReadOnlyModelViewSet):
    queryset = UserTypes.objects.all()
    serializer_class = UserTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
