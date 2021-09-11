# Lessons Learned
- Place utterance action immediately after intention
- One example leads to unexpected behavior because it easily might be interfered by other cases
- Slot has weight -> [0, 1] and feature (dimension)
- To be mindful of the symmetry of intention-case frequency in between many stories
- To be mindful of over learning.
- To be mindful of values loss and acc, when acc quickly reaches 1 but loss still hight, experience in practice has shown that it's time to make the NN bigger or deeper
- To strength the flow of scrips, make the representative vector of feature slot bigger and denser
- Bigger max_history makes result worse
- Low max_history value may make model focuses on slots and entities feature more than long history
- MemoizationPolicy somehow has relation to TEDPolicy, because when not registered the performance of Core significantly affected. \
(implicitly they should be independent according to the document)
- Increasing 'max_history' has impact on model's performance (higher action prediction confidence)
- When prediction confidence is low, making NN bigger is good to try
- Lower value of epoch may make model less confidence when predicting but may make model "smarter" (better in  processing abstract data)
- Increase the size of slots feature to balance with the size of sbert wordvector
- The acc metrics of training time is very good (0.99) but the performance at testing time is not correct in repsect to story's instruction, \
is that because the training story is composed improperly?? Is that because of executing unexpectedly actions??
- The higher acc value the higher prediction confidence value
- Increase the size of dense dimension layer can improve the training acc.
- Increse the size of dialogue block of trainsform layer can improm the training acc.
- core_fallback_threshold, how to determine its value? Start at lowers first, just increase this value when wrong action with low confidence occurs. \
If right action is predicted with low confidence story should by improved, fallback_threshold should be used when there is no option to improve the sittuation.
- Remember a sittuation as perfect evidence of size of dimension of slot has significant influence on action selection. It was when "stm_bot_verbal_intention" was added \
to the story but action had not yet implemented appropriately, the consequence of that was action "action_initialize_a_kiss_story" was always chosen. Why? Because \
"stm_bot_verbal_intention" is None at starting point and is dominant to others.
- If prediction confidence is high most of the time, it's very good chance to decrease training time (epoch) to improve model generalizing ability.
