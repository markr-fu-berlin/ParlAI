from parlai.core.teachers import FixedDialogTeacher
from .build import build

import os
import json



#   teacher that reads hotpotqa-data:

#   .text -> <T>titel</T>context
#   .id_ -> id
#   .episode_done -> true
#   .labels -> answer

#   .suporting_facts -> supporting_fact|number||
#   .question -> question



# bash docker_build.sh
# bash docker_exec.sh

# export LANG=C.UTF-8
# cd examples
# python display_data.py -t hotpotqaintegrationtest


def _path(opt):
    # ensure data is built
    build(opt)

    # set up path to data (specific to each dataset)
    dt = opt['datatype'].split(':')[0]
    if dt == 'valid':
        dt = 'dev'
    return os.path.join(opt['datapath'], 'hotpot_{type}_v1.1'.format(type=dt),
                        'hotpot_{type}_v1.1.json'.format(type=dt))

class DTeacher(FixedDialogTeacher):

    def __init__(self, opt, shared=None):
        build(opt)
        super().__init__(opt)

        if shared and 'ques' in shared:
            # another instance was set up already, just reference its data
            self.ques = shared['ques']

        else:
            data_path = _path(opt)
            self._setup_data(data_path)

        self.reset()

    def _setup_data(self, data_path):
        print('loading: ' + data_path)
        with open(data_path, encoding='utf-8') as data_file:
            self.ques = json.load(data_file)

    def share(self):
        shared = super().share()
        shared['ques'] = self.ques
        return shared

    def num_examples(self):
        return len(self.ques)

    def num_episodes(self):
        return self.num_examples()

    def get(self, episode_idx, entry_idx=0):
        qa = self.ques[episode_idx]
        print(episode_idx)

        text = ''
        for con in qa['context']:
            text = text + " <t> " + con[0] + " </t> "
            for line in range(len(con[1])):
                text = text + con[1][line]

        s_facts = []
        for s in qa['supporting_facts']:
            s_facts.append(s[0])

        action = {
            'id': qa['_id'],
            'text': text,
            'episode_done': True,
            'lables': qa['answer'],
            'question': qa['question'],
            'supporting_facts': s_facts
        }

        return action


class DefaultTeacher(DTeacher):
    pass