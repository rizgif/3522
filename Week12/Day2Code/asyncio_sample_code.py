"""
This module depicts the use of asyncio to allow multiple async coroutines to
run in parallel. An async coroutine is a block of code that takes a variable
amount of time to run and may not be executed in sequence.
"""
import asyncio
import time

async def get_data_from_database():
    """
    An async coroutine that simulates an asynchronous database query
    :return: A fake database result.
    """
    await asyncio.sleep(2)
    return "some data"


async def main():
    # gather starts a number of async couroutines in parallel waits until they
    # are all finished and collects their results.
    result = await asyncio.gather(get_data_from_database(),
                            get_data_from_database(),
                            get_data_from_database())
    #when asyncio.gather is finished, continue code from here
    print(f"The result: {result}")


if __name__ == '__main__':
    print("--Running a single async couroutine--")
    start = time.time()
    result = asyncio.run(get_data_from_database())
    duration = time.time() - start
    print(f"The result: {result} arrived in {duration} seconds")

    print("--------------")

    print("--Running multiple async couroutines--")
    start = time.time()
    asyncio.run(main())
    duration = time.time() - start
    print("Time taken", duration, "seconds")

