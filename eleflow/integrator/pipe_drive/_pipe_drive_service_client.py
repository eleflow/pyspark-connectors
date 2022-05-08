import os
import pipe_drive.services as service

class PipeDriveServiceClient:
    
    URL_BASE = os.getenv('URL_BASE', 'https://api.pipedrive.com/v1')
    
    def __init__(self,api_token_key, api_token_value, base_url=URL_BASE) -> None:
        """ Initialize the PipeDriveServiceClient.
        """
        # Create the service clients
        self.activities_service = service.PipeDriveActivities(base_url,api_token_key, api_token_value)
        self.activity_types_service = service.PipeDriveActivityTypes(base_url,api_token_key, api_token_value)
        self.call_logs_service = service.PipeDriveCallLogs(base_url,api_token_key, api_token_value)
        self.deals_fields_service = service.PipeDriveDealsFields(base_url,api_token_key, api_token_value)
        self.deals_service = service.PipeDriveDeals(base_url,api_token_key, api_token_value)
        self.files_service = service.PipeDriveFiles(base_url,api_token_key, api_token_value)
        self.filters_service = service.PipeDriveFilters(base_url,api_token_key, api_token_value)
        self.global_messages_service = service.PipeDriveGlobalMessages(base_url,api_token_key, api_token_value)
        self.goals_service = service.PipeDriveGoals(base_url,api_token_key, api_token_value)
        self.item_search_service = service.PipeDriveItemSearch(base_url,api_token_key, api_token_value)
        self.lead_labels_service = service.PipeDriveLeadLabels(base_url,api_token_key, api_token_value)
        self.leads_service = service.PipeDriveLeads(base_url,api_token_key, api_token_value)
        self.mailbox_service = service.PipeDriveMailbox(base_url,api_token_key, api_token_value)
        self.notes_service = service.PipeDriveNotes(base_url,api_token_key, api_token_value)
        self.organization_fields_service = service.PipeDriveOrganizationFields(base_url,api_token_key, api_token_value)
        self.organization_relationships_service = service.PipeDriveOrganizationRelationships(base_url,api_token_key, api_token_value)
        self.organizations_service = service.PipeDriveOrganizations(base_url,api_token_key, api_token_value)
        self.permission_sets_service = service.PipeDrivePermissionSets(base_url,api_token_key, api_token_value)
        self.person_fields_service = service.PipeDrivePersonFields(base_url,api_token_key, api_token_value)
        self.products_service = service.PipeDriveProducts(base_url,api_token_key, api_token_value)
        self.roles_service = service.PipeDriveRoles(base_url,api_token_key, api_token_value)
        self.stages_service = service.PipeDriveStages(base_url,api_token_key, api_token_value)
        self.subscriptions_service = service.PipeDriveSubscriptions(base_url,api_token_key, api_token_value)
        self.teams_service = service.PipeDriveTeams(base_url,api_token_key, api_token_value)
        self.users_service = service.PipeDriveUsers(base_url,api_token_key, api_token_value)
        self.webhooks_service = service.PipeDriveWebhooks(base_url,api_token_key, api_token_value)
        self.activity_fields_service = service.PipeDriveActivityFields(base_url,api_token_key, api_token_value)
        self.currencies_service = service.PipeDriveCurrencies(base_url,api_token_key, api_token_value)
        self.lead_sources_service = service.PipeDriveLeadSources(base_url,api_token_key, api_token_value)
        self.note_fields_service = service.PipeDriveNoteFields(base_url,api_token_key, api_token_value)
        self.recents_service = service.PipeDriveRecents(base_url,api_token_key, api_token_value)
        self.user_connections_service = service.PipeDriveUserConnections(base_url,api_token_key, api_token_value)
        self.user_settings_service = service.PipeDriveUserSettings(base_url,api_token_key, api_token_value)