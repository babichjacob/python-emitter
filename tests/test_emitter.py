"Test emitters"

import pytest

from emitter import emittable, mapped, successor


@pytest.mark.asyncio
async def test_successor():
    "Ensure that `successor` reports the next event emitted after it's called"

    an_emitter = emittable()

    next_event = successor(an_emitter)

    an_emitter.emit(15)

    assert (await next_event) == 15


def test_mapped():
    "Test that `mapped` maps events by calling the function on each one and emitting that result"

    strings = ["hi", "there", "this", "is", "test", "data"]

    expected_mapped_events = [2, 5, 4, 2, 4, 4]
    actual_mapped_events = []

    strings_emitter = emittable()
    lengths_emitter = mapped(strings_emitter, len)

    lengths_emitter.listen(actual_mapped_events.append)

    for string in strings:
        strings_emitter.emit(string)

    assert actual_mapped_events == expected_mapped_events
