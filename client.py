class BidirectionalHumanAgentStateSyncCoordinatorClient:
    def synchronize_shared_workspace_state(self, session_id='copilot_sess_9918', human_delta_mutations=[{'path': 'document.title', 'val': 'Q4 Strategy Draft'}], agent_delta_mutations=[{'path': 'document.summary', 'val': 'Key focus: AI expansion'}]):
        return {
            'sync_event_id': 'st_syn_8812',
            'session_id': session_id,
            'conflict_detected': False,
            'merged_workspace_version': 42,
            'applied_mutations_count': len(human_delta_mutations) + len(agent_delta_mutations),
            'lock_ownership': 'SHARED_OPTIMISTIC_LOCK',
            'state_sync_telemetry_url': 'https://coagents.sync.genpark.ai/sessions/8812.json'
        }
