# Taken from https://pymotw.com/3/asyncio/executors.html

import asyncio
import concurrent.futures
import logging
import sys
import time
import random
import multiprocessing
import click


def this_func_blocks(n, print_log=False):
    """
    Ordinary python function that's executed procedurally
    """
    log = logging.getLogger('this_func_blocks({})'.format(n))
    log.info('running')
    time.sleep(0.1 * random.random() * n)
    log.info('done')
    result = n ** 2
    if print_log == True:
        print(f'{result}')
    return result


async def run_blocking_tasks(executor, blocking_function, num_tasks:int):
    """
    Async function that invokes run_in_executor to run a blocking function through multiple threads, and waits until they're all done

    executor: Thread or Process pool that will run our tasks
    blocking_function: Function object that will run on our process pool
    num_tasks: How many tasks to queue up on our executor
    """ 
    log = logging.getLogger('run_blocking_tasks')
    log.info('starting')

    log.info('creating executor tasks')
    loop = asyncio.get_event_loop()
    blocking_tasks = [
        loop.run_in_executor(executor, blocking_function, i)
        for i in range(num_tasks)
    ]
    log.info('waiting for executor tasks')
    completed, pending = await asyncio.wait(blocking_tasks)
    results = [t.result() for t in completed]
    log.info('results: {!r}'.format(results))

    log.info('exiting')


# Take a path as a click command
@click.command()
@click.argument('path')  # Path of file to upload to Usenet.
def main(path):
    """
    We want to do a POC where we pull a queue of tasks and payloads form SQLite, and process them asyncronously as they arrive
    """
    # Configure logging to show the id of the process where the log message originates.
    logging.basicConfig(level=logging.INFO, format='PID %(process)5s %(name)18s: %(message)s', stream=sys.stderr)
    
    # Determine CPU core count
    cpu_count = multiprocessing.cpu_count()
    log = logging.getLogger('main')
    log.info(f'CPUcount={cpu_count}')
    # Use available cores to determine the number of simultaneous workers to run
    thread_count = cpu_count * 2

    # Create a process pool limited by max workers (thread count) using a context manager
    with concurrent.futures.ProcessPoolExecutor(max_workers=thread_count) as executor:
        # Use the current event loop to spawn a bunch of blocking tasks with our run_blocking_tasks function
        asyncio.run(run_blocking_tasks(executor, blocking_function=this_func_blocks, num_tasks=thread_count*5, ))


if __name__ == '__main__':
    main()

