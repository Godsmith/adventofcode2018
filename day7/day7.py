from typing import Dict, Set
from .. import util


class Step:
    def __init__(self, name, plustime):
        self.name = name
        self.next_steps = []
        self.time_to_complete = ord(name) - ord('A') + 1 + plustime
        self.worked_time = 0

    def add_next(self, step: 'Step'):
        self.next_steps.append(step)

    def work(self):
        self.worked_time += 1

    @property
    def is_complete(self):
        return self.worked_time >= self.time_to_complete

    def __repr__(self):
        return "Step('%s', %s, %s)" % (self.name, self.time_to_complete,
                                       [step.name for step in self.next_steps])


def find_first_step(steps: Dict[str, Step]):
    return sorted(available_steps(steps), key=lambda step: step.name)[0]


def available_steps(steps: Dict[str, Step]) -> Set[Step]:
    all_steps = set(steps.values())
    all_next_steps = set()
    for step in steps.values():
        for next_step in step.next_steps:
            all_next_steps.add(next_step)
    return all_steps - all_next_steps


def create_steps(lines, plustime=0):
    steps = {}
    for line in lines:
        previous_step = line.split()[1]
        next_step = line.split()[7]

        for step in (previous_step, next_step):
            if step not in steps:
                steps[step] = Step(step, plustime)
        steps[previous_step].add_next(steps[next_step])
    return steps


def time_to_complete_steps(lines, workers, plustime):
    steps = create_steps(lines, plustime=plustime)
    seconds = 0
    current_work_steps = set()
    while steps:
        available = available_steps(steps)
        while (len(current_work_steps) < workers and
                   (available - current_work_steps)):
            first_step = sorted(available - current_work_steps,
                                key=lambda step: step.name)[0]

            current_work_steps.add(first_step)
        steps_to_delete = []
        for step in current_work_steps:
            step.work()
            if step.is_complete:
                steps_to_delete.append(step)
        for step in steps_to_delete:
            current_work_steps.remove(step)
            del steps[step.name]
        seconds += 1
    return seconds


lines = util.input_lines(7)

steps = create_steps(lines)
while len(steps) > 0:
    step = find_first_step(steps)
    print(step.name, end='')
    del steps[step.name]
print()

print(time_to_complete_steps(lines, 5, 60))
