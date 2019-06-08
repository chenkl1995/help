from collections import namedtuple

Score = namedtuple('Score', [
    'acc',
    'acc_cls',
    'mean_acc',
    'iou_cls',
    'mean_iou',
])

score = Score(
    0.,
    None,
    None,
    [],
    0.,
)

print(score)
print(score.acc)