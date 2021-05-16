from rasa.core.policies.fallback import FallbackPolicy


class NLUFallbackPolicy(FallbackPolicy):

    def __init__(
        self,
        priority,
        fallback_action_name,
        nlu_threshold: float = 0.3,
        ambiguity_threshold: float = 0.1,
        core_threshold: float = 0.01
    ) -> None:

        core_threshold = 0.01
        super().__init__(
                priority=priority,
                nlu_threshold=nlu_threshold,
                ambiguity_threshold=ambiguity_threshold,
                core_threshold=core_threshold,
                fallback_action_name=fallback_action_name
            )


class PredictionFallbackPolicy(FallbackPolicy):

    def __init__(
        self,
        priority,
        core_threshold,
        fallback_action_name,
        nlu_threshold: float = 0.01,
        ambiguity_threshold: float = 0.01,
    ) -> None:

        nlu_threshold = 0.01
        ambiguity_threshold = 0.01
        super().__init__(
                priority=priority,
                nlu_threshold=nlu_threshold,
                ambiguity_threshold=ambiguity_threshold,
                core_threshold=core_threshold,
                fallback_action_name=fallback_action_name)
