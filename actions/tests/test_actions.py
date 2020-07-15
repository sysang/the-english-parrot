from actions.actions import ActionQuestion

events = [
    {'event': 'action', 'timestamp': 1594546157.707311, 'name': 'action_session_start', 'policy': None, 'confidence': None},
    {'event': 'session_started', 'timestamp': 1594546157.7073178},
    {'event': 'action', 'timestamp': 1594546157.7073298, 'name': 'action_listen', 'policy': None, 'confidence': None}, 
    {'event': 'user', 'timestamp': 1594546159.4461524, 'text': 'hi', 'parse_data': {'intent': {'name': 'a_kiss__answer_11', 'confidence': 0.4644474387168884}, 'entities': [], 'intent_ranking': [{'name': 'a_kiss__answer_11', 'confidence': 0.4644474387168884}, {'name': 'a_kiss__answer_7', 'confidence': 0.3114343583583832}, {'name': 'out_of_scope', 'confidence': 0.10659883171319962}, {'name': 'a_kiss__answer_6', 'confidence': 0.06404183804988861}, {'name': 'a_kiss__answer_14', 'confidence': 0.05347764119505882}], 'response_selector': {'out_of_scope': {'response': {'name': 'utter_out_of_scope_other', 'confidence': 1.0}, 'ranking': [{'name': 'utter_out_of_scope_other', 'confidence': 1.0, 'full_retrieval_intent': 'out_of_scope/other'}, {'name': 'utter_out_of_scope_no_english', 'confidence': 2.0827356937853447e-27, 'full_retrieval_intent': 'out_of_scope/non_english'}], 'full_retrieval_intent': 'out_of_scope/other'}}, 'text': 'hi'}, 'input_channel': 'cmdline', 'message_id': '55d57da05d5243e591257efc79fb50dd', 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546159.4744291, 'name': 'action_question', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.7586797475814819}, 
    {'event': 'bot', 'timestamp': 1594546159.4744363, 'text': 'Hello from action!', 'data': {'elements': None, 'quick_replies': None, 'buttons': None, 'attachment': None, 'image': None, 'custom': None}, 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546159.4813998, 'name': 'action_listen', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.9310653209686279}, 
    {'event': 'user', 'timestamp': 1594546423.7930706, 'text': 'hi', 'parse_data': {'intent': {'name': 'a_kiss__answer_11', 'confidence': 0.46444734930992126}, 'entities': [], 'intent_ranking': [{'name': 'a_kiss__answer_11', 'confidence': 0.46444734930992126}, {'name': 'a_kiss__answer_7', 'confidence': 0.3114342987537384}, {'name': 'out_of_scope', 'confidence': 0.10659883916378021}, {'name': 'a_kiss__answer_6', 'confidence': 0.06404182314872742}, {'name': 'a_kiss__answer_14', 'confidence': 0.05347764492034912}], 'response_selector': {'out_of_scope': {'response': {'name': 'utter_out_of_scope_other', 'confidence': 1.0}, 'ranking': [{'name': 'utter_out_of_scope_other', 'confidence': 1.0, 'full_retrieval_intent': 'out_of_scope/other'}, {'name': 'utter_out_of_scope_no_english', 'confidence': 2.0827356937853447e-27, 'full_retrieval_intent': 'out_of_scope/non_english'}], 'full_retrieval_intent': 'out_of_scope/other'}}, 'text': 'hi'}, 'input_channel': 'cmdline', 'message_id': '23c903b997c14e5884c0623d058b3c2d', 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546423.8086581, 'name': 'action_question', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.7713236212730408}, 
    {'event': 'action', 'timestamp': 1594546423.815452, 'name': 'action_listen', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.9345898032188416}, 
    {'event': 'user', 'timestamp': 1594546513.0255625, 'text': 'hi', 'parse_data': {'intent': {'name': 'a_kiss__answer_11', 'confidence': 0.4644474387168884}, 'entities': [], 'intent_ranking': [{'name': 'a_kiss__answer_11', 'confidence': 0.4644474387168884}, {'name': 'a_kiss__answer_7', 'confidence': 0.311434268951416}, {'name': 'out_of_scope', 'confidence': 0.10659883916378021}, {'name': 'a_kiss__answer_6', 'confidence': 0.0640418529510498}, {'name': 'a_kiss__answer_14', 'confidence': 0.053477659821510315}], 'response_selector': {'out_of_scope': {'response': {'name': 'utter_out_of_scope_other', 'confidence': 1.0}, 'ranking': [{'name': 'utter_out_of_scope_other', 'confidence': 1.0, 'full_retrieval_intent': 'out_of_scope/other'}, {'name': 'utter_out_of_scope_no_english', 'confidence': 2.0827435900981167e-27, 'full_retrieval_intent': 'out_of_scope/non_english'}], 'full_retrieval_intent': 'out_of_scope/other'}}, 'text': 'hi'}, 'input_channel': 'cmdline', 'message_id': '69e300b00e334de79e1e978844880486', 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546513.0417497, 'name': 'action_question', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.7695697546005249}, 
    {'event': 'bot', 'timestamp': 1594546513.0417564, 'text': 'Hello from action!', 'data': {'elements': None, 'quick_replies': None, 'buttons': None, 'attachment': None, 'image': None, 'custom': None}, 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546513.0492718, 'name': 'action_listen', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.9344760775566101}, 
    {'event': 'user', 'timestamp': 1594546597.003516, 'text': 'hi', 'parse_data': {'intent': {'name': 'a_kiss__answer_11', 'confidence': 0.46444740891456604}, 'entities': [], 'intent_ranking': [{'name': 'a_kiss__answer_11', 'confidence': 0.46444740891456604}, {'name': 'a_kiss__answer_7', 'confidence': 0.3114343285560608}, {'name': 'out_of_scope', 'confidence': 0.10659883171319962}, {'name': 'a_kiss__answer_6', 'confidence': 0.06404180824756622}, {'name': 'a_kiss__answer_14', 'confidence': 0.053477656096220016}], 'response_selector': {'out_of_scope': {'response': {'name': 'utter_out_of_scope_other', 'confidence': 1.0}, 'ranking': [{'name': 'utter_out_of_scope_other', 'confidence': 1.0, 'full_retrieval_intent': 'out_of_scope/other'}, {'name': 'utter_out_of_scope_no_english', 'confidence': 2.0827435900981167e-27, 'full_retrieval_intent': 'out_of_scope/non_english'}], 'full_retrieval_intent': 'out_of_scope/other'}}, 'text': 'hi'}, 'input_channel': 'cmdline', 'message_id': 'c52a2bb52c7142458cf85e07c685b2a0', 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546597.019852, 'name': 'action_question', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.7690250873565674}, 
    {'event': 'bot', 'timestamp': 1594546597.0198596, 'text': 'Hello from action!', 'data': {'elements': None, 'quick_replies': None, 'buttons': None, 'attachment': None, 'image': None, 'custom': None}, 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546597.027912, 'name': 'action_listen', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.9327910542488098}, 
    {'event': 'user', 'timestamp': 1594546703.6814814, 'text': 'test', 'parse_data': {'intent': {'name': 'out_of_scope', 'confidence': 0.9998618364334106}, 'entities': [], 'intent_ranking': [{'name': 'out_of_scope', 'confidence': 0.9998618364334106}, {'name': 'a_kiss__answer_6', 'confidence': 8.611064549768344e-05}, {'name': 'a_kiss__answer_4', 'confidence': 2.2095815438660793e-05}, {'name': 'a_kiss__answer_13', 'confidence': 1.835992770793382e-05}, {'name': 'a_kiss__answer_10', 'confidence': 1.1630237167992163e-05}], 'response_selector': {'out_of_scope': {'response': {'name': 'utter_out_of_scope_other', 'confidence': 1.0}, 'ranking': [{'name': 'utter_out_of_scope_other', 'confidence': 1.0, 'full_retrieval_intent': 'out_of_scope/other'}, {'name': 'utter_out_of_scope_no_english', 'confidence': 2.605428414285831e-35, 'full_retrieval_intent': 'out_of_scope/non_english'}], 'full_retrieval_intent': 'out_of_scope/other'}}, 'text': 'test'}, 'input_channel': 'cmdline', 'message_id': 'e335f5f28e2d49208e13b3170c5277a9', 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546703.690415, 'name': 'respond_out_of_scope', 'policy': 'policy_2_MappingPolicy', 'confidence': 1}, 
    {'event': 'bot', 'timestamp': 1594546703.69042, 'text': 'utter_out_of_scope_other', 'data': {'elements': None, 'quick_replies': None, 'buttons': None, 'attachment': None, 'image': None, 'custom': None}, 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546703.6988943, 'name': 'action_listen', 'policy': 'policy_2_MappingPolicy', 'confidence': 1}, 
    {'event': 'user', 'timestamp': 1594546710.551593, 'text': 'carlos', 'parse_data': {'intent': {'name': 'a_kiss__answer_7', 'confidence': 0.524255633354187}, 'entities': [], 'intent_ranking': [{'name': 'a_kiss__answer_7', 'confidence': 0.524255633354187}, {'name': 'a_kiss__answer_11', 'confidence': 0.21477578580379486}, {'name': 'a_kiss__answer_12', 'confidence': 0.16989126801490784}, {'name': 'a_kiss__answer_10', 'confidence': 0.04993639141321182}, {'name': 'a_kiss__answer_2', 'confidence': 0.041140973567962646}], 'response_selector': {'out_of_scope': {'response': {'name': 'utter_out_of_scope_other', 'confidence': 0.9999313950538635}, 'ranking': [{'name': 'utter_out_of_scope_other', 'confidence': 0.9999313950538635, 'full_retrieval_intent': 'out_of_scope/other'}, {'name': 'utter_out_of_scope_no_english', 'confidence': 6.862949521746486e-05, 'full_retrieval_intent': 'out_of_scope/non_english'}], 'full_retrieval_intent': 'out_of_scope/other'}}, 'text': 'carlos'}, 'input_channel': 'cmdline', 'message_id': 'ed7a159168ba4b1782fcd1d745a0b04a', 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546710.5696702, 'name': 'action_question', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.8443589210510254}, 
    {'event': 'action', 'timestamp': 1594546710.5791872, 'name': 'action_listen', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.9316968321800232}, 
    {'event': 'user', 'timestamp': 1594546765.851614, 'text': 'he did', 'parse_data': {'intent': {'name': 'out_of_scope', 'confidence': 0.6195554137229919}, 'entities': [], 'intent_ranking': [{'name': 'out_of_scope', 'confidence': 0.6195554137229919}, {'name': 'a_kiss__answer_13', 'confidence': 0.1607973277568817}, {'name': 'a_kiss__answer_3', 'confidence': 0.08184392750263214}, {'name': 'a_kiss__answer_4', 'confidence': 0.07767438888549805}, {'name': 'a_kiss__answer_12', 'confidence': 0.06012895330786705}], 'response_selector': {'out_of_scope': {'response': {'name': 'utter_out_of_scope_other', 'confidence': 1.0}, 'ranking': [{'name': 'utter_out_of_scope_other', 'confidence': 1.0, 'full_retrieval_intent': 'out_of_scope/other'}, {'name': 'utter_out_of_scope_no_english', 'confidence': 9.830756289694067e-28, 'full_retrieval_intent': 'out_of_scope/non_english'}], 'full_retrieval_intent': 'out_of_scope/other'}}, 'text': 'he did'}, 'input_channel': 'cmdline', 'message_id': '13d0d881184149d4a28ff2c8316e3f2e', 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546765.8619375, 'name': 'respond_out_of_scope', 'policy': 'policy_2_MappingPolicy', 'confidence': 1}, 
    {'event': 'bot', 'timestamp': 1594546765.861942, 'text': 'utter_out_of_scope_other', 'data': {'elements': None, 'quick_replies': None, 'buttons': None, 'attachment': None, 'image': None, 'custom': None}, 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546765.8717988, 'name': 'action_listen', 'policy': 'policy_2_MappingPolicy', 'confidence': 1}, 
    {'event': 'user', 'timestamp': 1594546770.2689085, 'text': 'the girl', 'parse_data': {'intent': {'name': 'a_kiss__answer_14', 'confidence': 0.6223345994949341}, 'entities': [], 'intent_ranking': [{'name': 'a_kiss__answer_14', 'confidence': 0.6223345994949341}, {'name': 'out_of_scope', 'confidence': 0.13785520195960999}, {'name': 'a_kiss__answer_7', 'confidence': 0.11383644491434097}, {'name': 'a_kiss__answer_9', 'confidence': 0.06679439544677734}, {'name': 'a_kiss__answer_6', 'confidence': 0.05917937681078911}], 'response_selector': {'out_of_scope': {'response': {'name': 'utter_out_of_scope_other', 'confidence': 1.0}, 'ranking': [{'name': 'utter_out_of_scope_other', 'confidence': 1.0, 'full_retrieval_intent': 'out_of_scope/other'}, {'name': 'utter_out_of_scope_no_english', 'confidence': 0.0, 'full_retrieval_intent': 'out_of_scope/non_english'}], 'full_retrieval_intent': 'out_of_scope/other'}}, 'text': 'the girl'}, 'input_channel': 'cmdline', 'message_id': '12e50c8ee662419fbd37c0fd0fad24f4', 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546770.2873085, 'name': 'action_question', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.7835409641265869}, 
    {'event': 'bot', 'timestamp': 1594546770.2873154, 'text': 'Hello from action!', 'data': {'elements': None, 'quick_replies': None, 'buttons': None, 'attachment': None, 'image': None, 'custom': None}, 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546770.2989266, 'name': 'action_listen', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.9256837964057922}, 
    {'event': 'user', 'timestamp': 1594546883.0484447, 'text': 'hi', 'parse_data': {'intent': {'name': 'a_kiss__answer_11', 'confidence': 0.46444740891456604}, 'entities': [], 'intent_ranking': [{'name': 'a_kiss__answer_11', 'confidence': 0.46444740891456604}, {'name': 'a_kiss__answer_7', 'confidence': 0.3114343285560608}, {'name': 'out_of_scope', 'confidence': 0.10659882426261902}, {'name': 'a_kiss__answer_6', 'confidence': 0.06404178589582443}, {'name': 'a_kiss__answer_14', 'confidence': 0.05347765237092972}], 'response_selector': {'out_of_scope': {'response': {'name': 'utter_out_of_scope_other', 'confidence': 1.0}, 'ranking': [{'name': 'utter_out_of_scope_other', 'confidence': 1.0, 'full_retrieval_intent': 'out_of_scope/other'}, {'name': 'utter_out_of_scope_no_english', 'confidence': 2.0827435900981167e-27, 'full_retrieval_intent': 'out_of_scope/non_english'}], 'full_retrieval_intent': 'out_of_scope/other'}}, 'text': 'hi'}, 'input_channel': 'cmdline', 'message_id': 'e464aa8002e64b0885e51fb1f4f381f3', 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546883.0697165, 'name': 'action_question', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.7586212158203125}, 
    {'event': 'bot', 'timestamp': 1594546883.0697243, 'text': 'Hello from action!', 'data': {'elements': None, 'quick_replies': None, 'buttons': None, 'attachment': None, 'image': None, 'custom': None}, 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594546883.0840547, 'name': 'action_listen', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.9252796173095703}, 
    {'event': 'user', 'timestamp': 1594547519.5766914, 'text': 'hello', 'parse_data': {'intent': {'name': 'out_of_scope', 'confidence': 0.8106293082237244}, 'entities': [], 'intent_ranking': [{'name': 'out_of_scope', 'confidence': 0.8106293082237244}, {'name': 'a_kiss__answer_11', 'confidence': 0.07692992687225342}, {'name': 'a_kiss__answer_14', 'confidence': 0.04581451043486595}, {'name': 'a_kiss__answer_7', 'confidence': 0.04258867725729942}, {'name': 'a_kiss__answer_10', 'confidence': 0.02403753250837326}], 'response_selector': {'out_of_scope': {'response': {'name': 'utter_out_of_scope_other', 'confidence': 1.0}, 'ranking': [{'name': 'utter_out_of_scope_other', 'confidence': 1.0, 'full_retrieval_intent': 'out_of_scope/other'}, {'name': 'utter_out_of_scope_no_english', 'confidence': 2.106985224336627e-38, 'full_retrieval_intent': 'out_of_scope/non_english'}], 'full_retrieval_intent': 'out_of_scope/other'}}, 'text': 'hello'}, 'input_channel': 'cmdline', 'message_id': '726b951ed644460481025c9db2a1e492', 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594547519.5886035, 'name': 'respond_out_of_scope', 'policy': 'policy_2_MappingPolicy', 'confidence': 1}, 
    {'event': 'bot', 'timestamp': 1594547519.588608, 'text': 'utter_out_of_scope_other', 'data': {'elements': None, 'quick_replies': None, 'buttons': None, 'attachment': None, 'image': None, 'custom': None}, 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594547519.5999076, 'name': 'action_listen', 'policy': 'policy_2_MappingPolicy', 'confidence': 1}, 
    {'event': 'user', 'timestamp': 1594547525.6686862, 'text': 'hi', 'parse_data': {'intent': {'name': 'a_kiss__answer_11', 'confidence': 0.4644474685192108}, 'entities': [], 'intent_ranking': [{'name': 'a_kiss__answer_11', 'confidence': 0.4644474685192108}, {'name': 'a_kiss__answer_7', 'confidence': 0.311434268951416}, {'name': 'out_of_scope', 'confidence': 0.10659882426261902}, {'name': 'a_kiss__answer_6', 'confidence': 0.06404181569814682}, {'name': 'a_kiss__answer_14', 'confidence': 0.053477637469768524}], 'response_selector': {'out_of_scope': {'response': {'name': 'utter_out_of_scope_other', 'confidence': 1.0}, 'ranking': [{'name': 'utter_out_of_scope_other', 'confidence': 1.0, 'full_retrieval_intent': 'out_of_scope/other'}, {'name': 'utter_out_of_scope_no_english', 'confidence': 2.0827435900981167e-27, 'full_retrieval_intent': 'out_of_scope/non_english'}], 'full_retrieval_intent': 'out_of_scope/other'}}, 'text': 'hi'}, 'input_channel': 'cmdline', 'message_id': 'aca874875ce0407ab27c61c2605af081', 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594547525.692071, 'name': 'action_question', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.7590750455856323}, 
    {'event': 'bot', 'timestamp': 1594547525.6920779, 'text': 'Hello from action!', 'data': {'elements': None, 'quick_replies': None, 'buttons': None, 'attachment': None, 'image': None, 'custom': None}, 'metadata': {}}, 
    {'event': 'action', 'timestamp': 1594547525.7075071, 'name': 'action_listen', 'policy': 'policy_0_TEDPolicy', 'confidence': 0.9245674014091492}, 
    {'event': 'user', 'timestamp': 1594547600.7766209, 'text': 'hi', 'parse_data': {'intent': {'name': 'a_kiss__answer_11', 'confidence': 0.4644474685192108}, 'entities': [], 'intent_ranking': [{'name': 'a_kiss__answer_11', 'confidence': 0.4644474685192108}, {'name': 'a_kiss__answer_7', 'confidence': 0.311434268951416}, {'name': 'out_of_scope', 'confidence': 0.10659882426261902}, {'name': 'a_kiss__answer_6', 'confidence': 0.06404183804988861}, {'name': 'a_kiss__answer_14', 'confidence': 0.053477637469768524}], 'response_selector': {'out_of_scope': {'response': {'name': 'utter_out_of_scope_other', 'confidence': 1.0}, 'ranking': [{'name': 'utter_out_of_scope_other', 'confidence': 1.0, 'full_retrieval_intent': 'out_of_scope/other'}, {'name': 'utter_out_of_scope_no_english', 'confidence': 2.0827435900981167e-27, 'full_retrieval_intent': 'out_of_scope/non_english'}], 'full_retrieval_intent': 'out_of_scope/other'}}, 'text': 'hi'}, 'input_channel': 'cmdline', 'message_id': '47085af01d4e40ab9d3a31634f57594d', 'metadata': {}}
]

actor = ActionQuestion()

user_events = actor._filter_user_events(events)

print(len(user_events))
print(user_events[0]['event'])

print(user_events[0]['parse_data']['intent'])

