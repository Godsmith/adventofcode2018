from . import day7

def test_time_to_complete_steps():
    lines = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""".splitlines()
    assert day7.time_to_complete_steps(lines, 2, 0) == 15