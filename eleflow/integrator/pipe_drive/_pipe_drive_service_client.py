import os
from .services import *

class PipeDriveServiceClient:
    
    URL_BASE = os.getenv('URL_BASE', 'https://api.pipedrive.com/v1')
    
    def __init__(self,api_token_key, api_token_value, base_url=URL_BASE) -> None:
        """ Initialize the PipeDriveServiceClient.
        """
        # Create the service clients
        self.activities_service = PipeDriveActivities(base_url,api_token_key, api_token_value)
        self.activity_types_service = PipeDriveActivityTypes(base_url,api_token_key, api_token_value)
        self.call_logs_service = PipeDriveCallLogs(base_url,api_token_key, api_token_value)
        self.deals_fields_service = PipeDriveDealsFields(base_url,api_token_key, api_token_value)
        self.deals_service = PipeDriveDeals(base_url,api_token_key, api_token_value)
        self.files_service = PipeDriveFiles(base_url,api_token_key, api_token_value)
        self.filters_service = PipeDriveFilters(base_url,api_token_key, api_token_value)
        self.global_messages_service = PipeDriveGlobalMessages(base_url,api_token_key, api_token_value)
        self.goals_service = PipeDriveGoals(base_url,api_token_key, api_token_value)
        self.item_search_service = PipeDriveItemSearch(base_url,api_token_key, api_token_value)
        self.lead_labels_service = PipeDriveLeadLabels(base_url,api_token_key, api_token_value)
        self.leads_service = PipeDriveLeads(base_url,api_token_key, api_token_value)
        self.mailbox_service = PipeDriveMailbox(base_url,api_token_key, api_token_value)
        self.notes_service = PipeDriveNotes(base_url,api_token_key, api_token_value)
        self.organization_fields_service = PipeDriveOrganizationFields(base_url,api_token_key, api_token_value)
        self.organization_relationships_service = PipeDriveOrganizationRelationships(base_url,api_token_key, api_token_value)
        self.organizations_service = PipeDriveOrganizations(base_url,api_token_key, api_token_value)
        self.permission_sets_service = PipeDrivePermissionSets(base_url,api_token_key, api_token_value)
        self.person_fields_service = PipeDrivePersonFields(base_url,api_token_key, api_token_value)
        self.products_service = PipeDriveProducts(base_url,api_token_key, api_token_value)
        self.roles_service = PipeDriveRoles(base_url,api_token_key, api_token_value)
        self.stages_service = PipeDriveStages(base_url,api_token_key, api_token_value)
        self.subscriptions_service = PipeDriveSubscriptions(base_url,api_token_key, api_token_value)
        self.teams_service = PipeDriveTeams(base_url,api_token_key, api_token_value)
        self.users_service = PipeDriveUsers(base_url,api_token_key, api_token_value)
        self.webhooks_service = PipeDriveWebhooks(base_url,api_token_key, api_token_value)
        self.activity_fields_service = PipeDriveActivityFields(base_url,api_token_key, api_token_value)
        self.currencies_service = PipeDriveCurrencies(base_url,api_token_key, api_token_value)
        self.lead_sources_service = PipeDriveLeadSources(base_url,api_token_key, api_token_value)
        self.note_fields_service = PipeDriveNoteFields(base_url,api_token_key, api_token_value)
        self.recents_service = PipeDriveRecents(base_url,api_token_key, api_token_value)
        self.user_connections_service = PipeDriveUserConnections(base_url,api_token_key, api_token_value)
        self.user_settings_service = PipeDriveUserSettings(base_url,api_token_key, api_token_value)