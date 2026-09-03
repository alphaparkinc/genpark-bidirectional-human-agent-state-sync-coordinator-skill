from client import BidirectionalHumanAgentStateSyncCoordinatorClient

def main():
    client = BidirectionalHumanAgentStateSyncCoordinatorClient()
    res = client.synchronize_shared_workspace_state('sess_01', [{'p': 'form.email', 'v': 'user@ex.com'}], [{'p': 'form.autofill', 'v': True}])
    print('Bidirectional State Sync Coordinator: ' + res['sync_event_id'] + ' (Version: ' + str(res['merged_workspace_version']) + ')')
    print('Mutations: ' + str(res['applied_mutations_count']) + ' | Conflict: ' + str(res['conflict_detected']))
    print('Telemetry URL: ' + res['state_sync_telemetry_url'])

if __name__ == '__main__':
    main()
