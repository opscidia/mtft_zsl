from fslks import sink

sink.register('bioasq',
              prompt=sink.Constant('summarize'),
              input=sink.Sequence([
                  sink.Feature('question'),
                  sink.Feature('article')
              ]),
              output=sink.Feature('summary'))

sink.register('scientific_papers',
              prompt=sink.Constant('summarize'),
              input=sink.Feature('article'),
              output=sink.Feature('abstract'))

sink.register('movie_rationales',
              prompt=sink.Constant('summarize'),
              input=sink.Sequence('evidences'),
              output=sink.Feature('review'))

sink.register('cnn_dailymail',
              prompt=sink.Constant('summarize'),
              input=sink.Feature('article'),
              output=sink.Feature('highlights'))

sink.register('super_glue/copa',
              prompt=sink.Sequence([
                  sink.Constant('choose'),
                  sink.Feature('question'),
              ]),
              input=sink.Sequence([
                  sink.Feature('premise'),
                  sink.Feature('choice1'),
                  sink.Feature('choice2'),
              ]),
              output=sink.LabelMapping('label', {
                  0: sink.Feature('choice1'),
                  1: sink.Feature('choice2')
              }))

_eviconv_stance_mapping = sink.LabelMapping('stance', {
    0: sink.Constant('PRO :'),
    1: sink.Constant('CON :'),
})
sink.register('eviconv',
              prompt='argue',
              input=sink.Sequence([
                  sink.DictEntry('evidence_1', _eviconv_stance_mapping),
                  sink.DictEntry('evidence_1', sink.Feature('text')),
                  sink.DictEntry('evidence_2', _eviconv_stance_mapping),
                  sink.DictEntry('evidence_2', sink.Feature('text')),
              ]),
              output=sink.LabelMapping('_LABEL', {
                  0: sink.DictEntry('evidence_1', sink.Feature('text')),
                  1: sink.DictEntry('evidence_2', sink.Feature('text'))
              }))
