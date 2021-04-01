import sys
from parlai.core.params import ParlaiParser
from parlai.core.agents import create_agent
from parlai.core.worlds import create_task
from parlai.core.script import ParlaiScript, register_script
from parlai.utils.world_logging import WorldLogger
from parlai.agents.local_speech.local_speech import LocalSpeechAgent
import parlai.utils.logging as logging
import random
import os

#  Execute :  python ai.py  --model-file zoo:dodecadialogue/all_tasks_mt/model
#  python ai.py  --model-file zoo:dodecadialogue/wizard_of_wikipedia_ft/model --inference beam --beam-size 10 --beam-min-length 10 --beam-block-ngram 3 --beam-context-block-ngram 3 -t wizard_of_wikipedia

def setup_args(parser=None):
    if parser is None:
        parser = ParlaiParser(
            True, True, 'Interactive chat with a model on the command line'
        )
    parser.add_argument('-d', '--display-examples', type='bool', default=False)
    parser.add_argument(
        '--display-prettify',
        type='bool',
        default=False,
        help='Set to use a prettytable when displaying '
        'examples with text candidates',
    )
    parser.add_argument(
        '--display-add-fields',
        type=str,
        default='',
        help='Display these fields when verbose is off (e.g., "--display-add-fields label_candidates,beam_texts")',
    )
    parser.add_argument(
        '-it',
        '--interactive-task',
        type='bool',
        default=True,
        help='Create interactive version of task',
    )
    parser.add_argument(
        '--outfile',
        type=str,
        default='',
        help='Saves a jsonl file containing all of the task examples and '
        'model replies. Set to the empty string to not save at all',
    )
    parser.add_argument(
        '--save-format',
        type=str,
        default='conversations',
        choices=['conversations', 'parlai'],
        help='Format to save logs in. conversations is a jsonl format, parlai is a text format.',
    )
    parser.set_defaults(interactive_mode=True, task='interactive')
    LocalSpeechAgent.add_cmdline_args(parser, partial_opt=None)
    WorldLogger.add_cmdline_args(parser, partial_opt=None)
    return parser


def interactive(opt):
    if isinstance(opt, ParlaiParser):
        logging.error('interactive should be passed opt not Parser')
        opt = opt.parse_args()

    # Create model and assign it to the specified task
    agent = create_agent(opt, requireModelExists=True)
    agent.opt.log()
    human_agent = LocalSpeechAgent(opt)
    # set up world logger
    world_logger = WorldLogger(opt) if opt.get('outfile') else None
    world = create_task(opt, [human_agent, agent])

    # Show some example dialogs:

    os.system("C:\Python27\python setupNao.py")


    while not world.epoch_done():
        text = world.parley()
        waarde = world.display()
        print (waarde)
        waardePositie = waarde.find('ImageSeq2seq', 0, 100) + 23
        TextInhoud =  waarde[waardePositie:-1]
        print (TextInhoud)
        char = ""
        for x in TextInhoud:
            if x.isalpha():
                char = "".join([char, x])
            if x == " ":
                char = "".join([char, x])
        char = char[1:200]
        char=char.replace("mImageSeqseqm","")
        char = char.replace("m m", "")
        char = char.replace("  ", " ")
        char = char.replace("m  m", "")
        char = char.replace("m   m", "")
        char = char.replace("m    m", "")
        char = char.replace("m     m", "")

        list = os.system("C:\Python27\python -W ignore nao.py \" "+ char + "\" ")


        if world.epoch_done() or world.get_total_parleys() <= 0:
            # chat was reset with [DONE], [EXIT] or EOF
            if world_logger is not None:
                world_logger.reset()
            continue

        if world_logger is not None:
            world_logger.log(world)
        if opt.get('display_examples'):
            print("---")
            #print(world.display())

    if world_logger is not None:
        # dump world acts to file
        world_logger.write(opt['outfile'], world, file_format=opt['save_format'])


@register_script('interactive', aliases=['i'])
class Interactive(ParlaiScript):
    @classmethod
    def setup_args(cls):
        return setup_args()

    def run(self):
        return interactive(self.opt)


if __name__ == '__main__':
    random.seed(42)
    Interactive.main()